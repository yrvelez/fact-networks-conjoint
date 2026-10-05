# Who Shares What From Whom: An Ego-Network Conjoint of Misinformation Sharing

Study repository in the [filedrawer](https://github.com/yrvelez/filedrawer) layout. The package
(report, tidy data, scripts, results, provenance) is generated at the root of this repository by
the pipeline; the inputs live in `inputs/`.

Depositing with an AI coding agent, or by hand: follow `AGENTS.md` in this repository. It says what
must never be committed (the raw export), how to strip identifiers, and what the models see.

## Inputs (`inputs/`)

- `export.csv`  Qualtrics export (raw; **gitignored**, it contains identifiers)
- `survey.qsf`  survey schema
- `pap.md`      pre-analysis plan as text

## Data (`data/`)

- `raw_tidy.csv`  12,000 rows (one per conjoint profile shown; 1,500 respondents x 4 trials x 2 profiles) and 45
  analysis fields. Built by `inputs/prepare_export.R` from a trimmed, pseudonymized YouGov file: no YouGov ids,
  no contact names, no headline text, no open-ended answers. `resp_id` is a sequential index (1-1500). The only
  respondent attributes are those the analysis uses: age, five-point ideology, media trust, survey language and
  nativity (with their tertiles), plus the survey weight. The full YouGov dataset is not included.
- `clean.csv`     `raw_tidy.csv` plus the analysis columns `scripts/02_clean.py` derives from it.

`filedrawer reproduce .` re-runs the scripts from `raw_tidy.csv` and checks every table in `results/` is identical.

## Run

```bash
pip install "filedrawer @ git+https://github.com/yrvelez/filedrawer"
export OPENROUTER_API_KEY=sk-or-...
./run.sh            # or: filedrawer run --csv inputs/export.csv --qsf inputs/survey.qsf --pap inputs/pap.md \
                    #        --slug fact-networks-conjoint --title "Who Shares What From Whom: An Ego-Network Conjoint of Misinformation Sharing" --authors "Yamil R. Velez" --package-dir . --review
REVIEW=light,advanced ./run.sh   # review modes: light (default), advanced, coarse, refine (manual upload)
filedrawer reproduce .
git add -A && git commit -m "Study package" && git push
```

Then file it: paste `https://github.com/yrvelez/fact-networks-conjoint` on the Submit page at https://filedrawer.org (or `filedrawer submit https://github.com/yrvelez/fact-networks-conjoint --server https://filedrawer.org`).
After reading the report: `filedrawer attest . --step "..." --by "..."`, and `filedrawer release .` before making the repository public.
