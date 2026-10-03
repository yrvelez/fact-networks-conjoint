import importlib.util, pathlib
_spec = importlib.util.spec_from_file_location('reg', pathlib.Path(__file__).with_name('03_registered.py')); reg = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(reg)
import pandas as pd, numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

df = pd.read_csv('data/clean.csv')
h1 = [h for h in reg.HYPOTHESES if h['id'] == 'H1'][0]
est = h1['estimator']; cov = est['covariates']

def run(sub):
    out = {}
    for arm in ['Misinformation', 'Fact-check']:
        d = sub[sub.infotype.isin([arm, 'True/neutral'])].copy()
        d = d.dropna(subset=['share', 'resp_id'] + cov).reset_index(drop=True)
        d['treat'] = (d.infotype == arm).astype(int)
        f, d2 = reg.build_formula('share', est, cov, d)
        res = reg.fit(d2, f, est)
        out[arm] = (float(res.params['treat']), float(res.bse['treat']), int(res.nobs))
    return out

o = run(df); a = run(df[df.trial > 1])
rows = [dict(arm=k, est_orig=o[k][0], se_orig=o[k][1], n_orig=o[k][2], est_alt=a[k][0], se_alt=a[k][1], n_alt=a[k][2]) for k in o]
pd.DataFrame(rows).to_csv('results/E1_h1_drop_trial1.csv', index=False)
print('E1 H1 drop trial1: ' + '; '.join(f"{r['arm']} {r['est_orig']:.3f}->{r['est_alt']:.3f} (se {r['se_orig']:.3f}->{r['se_alt']:.3f})" for r in rows))

rows2 = []
for lv in ['Lowest', 'Middle', 'Highest']:
    r = run(df[df.age_t == lv])
    for arm in r:
        rows2.append(dict(age_tertile=lv, arm=arm, estimate=r[arm][0], std_error=r[arm][1], n=r[arm][2]))
t = pd.DataFrame(rows2); t.to_csv('results/E2_h1_by_age.csv', index=False)
m = t[t.arm == 'Misinformation']
print('E2 misinfo AMCE by age tertile: ' + ', '.join(f"{x.age_tertile} {x.estimate:.3f}" for x in m.itertuples()))

fig, ax = plt.subplots(figsize=(5, 3))
for s in ['top', 'right', 'left']: ax.spines[s].set_visible(False)
ax.grid(False)
for i, x in enumerate(m.itertuples()):
    ax.errorbar(x.estimate, i, xerr=1.96 * x.std_error, fmt='o', color='#c0392b', ecolor='#c0392b')
    ax.text(x.estimate, i + 0.2, x.age_tertile, ha='center', color='black')
ax.axvline(0, color='black', lw=0.8); ax.set_yticks([])
ax.set_xlabel('Misinformation AMCE on sharing')
fig.savefig('figures/E2_age.png', dpi=200, facecolor='white', bbox_inches='tight')
