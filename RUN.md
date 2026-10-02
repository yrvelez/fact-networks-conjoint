# Reproducing `fact-networks-conjoint`

All scripts run from this folder with Python 3.11 and pandas, numpy, statsmodels, scipy, matplotlib.

```bash
pip install pandas numpy statsmodels scipy matplotlib
python scripts/01_tidy.py        # only if the raw export is placed at ./raw_export.csv (not shipped: it contains identifiers)
python scripts/02_clean.py       # data/raw_tidy.csv -> data/clean.csv
python scripts/03_registered.py  # registered tests -> results/, figures/registered_effects.png
python scripts/04_exploratory.py # exploratory analyses (EXPLORATORY — not pre-registered)
```

Or, with the tool installed: `filedrawer reproduce .` re-runs scripts 02-04 and verifies every table in
`results/` is byte-identical to the shipped version.
