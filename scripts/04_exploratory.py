import importlib.util, pathlib
_spec = importlib.util.spec_from_file_location('reg', pathlib.Path(__file__).with_name('03_registered.py'))
reg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reg)

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Load & prep ──────────────────────────────────────────────────────────────
df = pd.read_csv('data/clean.csv')
for col in ['share', 'plausibility', 'ideo5_self', 'trial', 'weight']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Registered H1 specification (from results/H1.csv)
outcome_h1 = 'share'
covariates = ['close_tie', 'sharer_native_us', 'sharer_ideology',
              'sharer_trust', 'sharer_knowledge', 'sharer_disputed']
arm_term = "C(arm_code, Treatment(reference='True/neutral'))"
cov_str = ' + '.join(
    [f"C({c})" if c in ['close_tie', 'sharer_native_us', 'sharer_ideology'] else c
     for c in covariates]
)
base_formula = f"{outcome_h1} ~ {arm_term} + {cov_str}"

def fit_arm_model(d_sub):
    """Fit the registered H1 model (arm_code Treatment coding, IPW, HC2) on a subset."""
    d = d_sub.dropna(subset=[outcome_h1] + covariates).copy()
    d['ipw'] = d['weight']
    res = smf.wls(base_formula, data=d, weights=d['ipw']).fit(cov_type='HC2')
    return res, d

def extract_arm_estimates(res, arms=['Misinformation', 'Fact-check']):
    """Extract arm-specific estimates from a fitted model."""
    rows = []
    for arm in arms:
        match = [t for t in res.params.index if arm in t and 'arm_code' in t]
        if match:
            t = match[0]
            rows.append({
                'arm': arm,
                'estimate': res.params[t],
                'std_error': res.bse[t],
                'p_value': res.pvalues[t],
                'conf_low': res.conf_int().loc[t, 0],
                'conf_high': res.conf_int().loc[t, 1],
            })
    return rows

ACCENT = '#D62828'
INK = '#222222'

# ── E1: Heterogeneity by respondent ideology ─────────────────────────────────
# Rationale: Tests whether the negative effect of misinformation/fact-check on
# sharing is stronger among conservative respondents, who may be more receptive
# to partisan misinformation.

df['is_conservative'] = (df['ideo5_self'] >= 4).astype(float)
df.loc[df['ideo5_self'].isna(), 'is_conservative'] = np.nan

df_e1 = df.dropna(subset=['share', 'ideo5_self'] + covariates).copy()
df_e1['ipw'] = df_e1['weight']

formula_e1 = f"share ~ {arm_term} * C(is_conservative) + {cov_str}"
res_e1 = smf.wls(formula_e1, data=df_e1, weights=df_e1['ipw']).fit(cov_type='HC2')

rows_e1 = []
for term in res_e1.params.index:
    if 'arm_code' in term:
        rows_e1.append({
            'term': term,
            'estimate': res_e1.params[term],
            'std_error': res_e1.bse[term],
            'p_value': res_e1.pvalues[term],
            'conf_low': res_e1.conf_int().loc[term, 0],
            'conf_high': res_e1.conf_int().loc[term, 1],
        })
e1_df = pd.DataFrame(rows_e1)
e1_df.to_csv('results/E1_ideology_heterogeneity.csv', index=False)

# Figure: forest plot
fig, ax = plt.subplots(figsize=(9, 4.5))

display = []
main_terms = [t for t in res_e1.params.index
              if 'arm_code' in t and 'is_conservative' not in t]
inter_terms = [t for t in res_e1.params.index
               if 'arm_code' in t and 'is_conservative' in t]

for t in main_terms:
    arm = 'Misinformation' if 'Misinformation' in t else 'Fact-check'
    display.append((f'{arm} (non-conservative)',
                    res_e1.params[t],
                    res_e1.conf_int().loc[t, 0],
                    res_e1.conf_int().loc[t, 1], INK))

for t in inter_terms:
    arm = 'Misinformation' if 'Misinformation' in t else 'Fact-check'
    display.append((f'{arm} (cons − non-cons)',
                    res_e1.params[t],
                    res_e1.conf_int().loc[t, 0],
                    res_e1.conf_int().loc[t, 1], ACCENT))

v = res_e1.cov_params()
for t in main_terms:
    arm = 'Misinformation' if 'Misinformation' in t else 'Fact-check'
    it = [x for x in inter_terms if arm in x][0]
    total = res_e1.params[t] + res_e1.params[it]
    se = np.sqrt(v.loc[t, t] + v.loc[it, it] + 2 * v.loc[t, it])
    display.append((f'{arm} (conservative total)',
                    total, total - 1.96 * se, total + 1.96 * se, ACCENT))

y = np.arange(len(display))
for i, (label, est, lo, hi, c) in enumerate(display):
    ax.hlines(i, lo, hi, color=c, linewidth=1.8)
    ax.scatter(est, i, color=c, s=40, zorder=5)
    ax.text(max(hi, est) + 0.005, i, f'{est:+.3f}', va='center', fontsize=9, color=INK)

ax.axvline(0, color='#AAAAAA', linewidth=0.6, linestyle='--')
ax.set_yticks(y)
ax.set_yticklabels([d[0] for d in display], fontsize=10)
ax.set_xlabel('Effect on probability of sharing', fontsize=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(left=False)
ax.set_xlim(-0.35, 0.05)
plt.tight_layout()
plt.savefig('figures/E1_ideology_heterogeneity.png', dpi=200, bbox_inches='tight')
plt.close()

mis_inter = [t for t in inter_terms if 'Misinformation' in t][0]
fc_inter = [t for t in inter_terms if 'Fact-check' in t][0]
print(f"E1: Ideology heterogeneity (n={len(df_e1)}): "
      f"Misinfo cons−noncons={res_e1.params[mis_inter]:+.4f} (SE={res_e1.bse[mis_inter]:.4f}, p={res_e1.pvalues[mis_inter]:.4f}); "
      f"Fact-check cons−noncons={res_e1.params[fc_inter]:+.4f} (SE={res_e1.bse[fc_inter]:.4f}, p={res_e1.pvalues[fc_inter]:.4f})")

# ── E2: Treatment effect by trial (manipulation / order check) ───────────────
# Rationale: Verifies that the treatment effect is stable across the four
# conjoint trials, ruling out order effects or respondent fatigue as
# alternative explanations for the registered estimates.

rows_e2 = []
for trial_num in [1, 2, 3, 4]:
    d_sub = df[df['trial'] == trial_num]
    res_t, d2_t = fit_arm_model(d_sub)
    for row in extract_arm_estimates(res_t):
        row['trial'] = trial_num
        row['n'] = len(d2_t)
        rows_e2.append(row)

e2_df = pd.DataFrame(rows_e2)
e2_df.to_csv('results/E2_trial_consistency.csv', index=False)

# Figure: effect by trial with direct labels
fig, ax = plt.subplots(figsize=(7, 4))
for arm, color in [('Misinformation', INK), ('Fact-check', ACCENT)]:
    sub = e2_df[e2_df['arm'] == arm].sort_values('trial')
    ax.errorbar(sub['trial'], sub['estimate'],
                yerr=[(sub['estimate'] - sub['conf_low']).values,
                      (sub['conf_high'] - sub['estimate']).values],
                fmt='o-', color=color, capsize=5, linewidth=1.5, markersize=6)
    for _, r in sub.iterrows():
        ax.annotate(f"{r['estimate']:+.3f}", (r['trial'], r['estimate']),
                    textcoords='offset points', xytext=(0, 10),
                    ha='center', fontsize=8, color=color)

ax.axhline(0, color='#AAAAAA', linewidth=0.6, linestyle='--')
ax.set_xlabel('Conjoint trial', fontsize=10)
ax.set_ylabel('Effect on sharing', fontsize=10)
ax.set_xticks([1, 2, 3, 4])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(left=False)
ax.text(4.15, e2_df[e2_df['arm']=='Misinformation']['estimate'].mean(),
        'Misinformation', fontsize=9, color=INK, va='center')
ax.text(4.15, e2_df[e2_df['arm']=='Fact-check']['estimate'].mean(),
        'Fact-check', fontsize=9, color=ACCENT, va='center')
ax.set_xlim(0.7, 4.8)
plt.tight_layout()
plt.savefig('figures/E2_trial_consistency.png', dpi=200, bbox_inches='tight')
plt.close()

mis_trials = e2_df[e2_df['arm'] == 'Misinformation']['estimate'].values
print(f"E2: Trial consistency (n per trial ≈{int(e2_df['n'].iloc[0])}): "
      f"Misinfo by trial = {', '.join(f'T{int(r)}={v:+.3f}' for r, v in zip(e2_df[e2_df.arm=='Misinformation']['trial'], mis_trials))}; "
      f"range = [{mis_trials.min():+.3f}, {mis_trials.max():+.3f}]")

# ── E3: Treatment effect by headline theme ───────────────────────────────────
# Rationale: Tests whether the negative effect is concentrated in specific
# topic areas, which would suggest the result is content-dependent rather
# than a general response to information type.

rows_e3 = []
for theme in sorted(df['headline_theme'].dropna().unique()):
    d_sub = df[df['headline_theme'] == theme]
    res_th, d2_th = fit_arm_model(d_sub)
    if len(d2_th) < 100:
        continue
    for row in extract_arm_estimates(res_th):
        row['headline_theme'] = theme
        row['n'] = len(d2_th)
        rows_e3.append(row)

e3_df = pd.DataFrame(rows_e3)
e3_df.to_csv('results/E3_theme_heterogeneity.csv', index=False)

mis_e3 = e3_df[e3_df['arm'] == 'Misinformation']['estimate']
fc_e3 = e3_df[e3_df['arm'] == 'Fact-check']['estimate']
print(f"E3: Theme heterogeneity ({len(e3_df)} arm-theme cells, {e3_df['headline_theme'].nunique()} themes): "
      f"Misinfo range [{mis_e3.min():+.3f}, {mis_e3.max():+.3f}], "
      f"Fact-check range [{fc_e3.min():+.3f}, {fc_e3.max():+.3f}]")
