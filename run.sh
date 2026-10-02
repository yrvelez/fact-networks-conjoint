#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
: "${OPENROUTER_API_KEY:?set OPENROUTER_API_KEY (bring your own token)}"
filedrawer run --csv inputs/export.csv --qsf inputs/survey.qsf --pap inputs/pap.md \
  --slug "fact-networks-conjoint" --title "Who Shares What From Whom: An Ego-Network Conjoint of Misinformation Sharing" --authors "Yamil R. Velez" \
  --package-dir . --review "${REVIEW:-light}" "$@"
