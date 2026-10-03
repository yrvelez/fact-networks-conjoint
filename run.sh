#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
: "${OPENROUTER_API_KEY:?set OPENROUTER_API_KEY (bring your own token)}"
# inputs/export.csv is built by inputs/prepare_export.R; inputs/pap.json by inputs/build_pap.py
filedrawer run --csv inputs/export.csv --qsf inputs/survey.qsf --pap inputs/pap.md --pap-json inputs/pap.json \
  --config inputs/config.yaml \
  --slug "fact-networks-conjoint" --title "Who Shares What From Whom: An Ego-Network Conjoint of Misinformation Sharing" \
  --authors "Yamil R. Velez" --repo-url "https://github.com/yrvelez/fact-networks-conjoint" \
  --package-dir . --review "${REVIEW:-light,advanced}" "$@"
