# Pre-analysis plan: Who Shares What From Whom: An Ego-Network Conjoint of Misinformation Sharing

Pre-registered: AsPredicted #132,508, "Social Network Conjoint (May 2023)", 2023/05/17 08:17 (PT).
URL: https://aspredicted.org/8njc-mpqw.pdf
Bundled with AsPredicted #132,123 ("Latino Issue Publics - Study 3 (2023)").

Transcribed verbatim below.

## 1) Have any data been collected for this study already?

No, no data have been collected for this study yet.

## 2) What's the main question being asked or hypothesis being tested in this study?

How do social factors influence both the self-reported likelihood of sharing various types of information and plausibility ratings?

## 3) Describe the key dependent variable(s) specifying how they will be measured.

Sharing and plausibility ratings of 8 randomly selected headline pairs (15 total)

## 4) How many and which conditions will participants be assigned to?

A social network-informed conjoint analysis where the manipulated features are names, but I collect meta-data on closeness, national origin/nativity, perceived trustworthiness, perceived knowledge in politics, ideology, and beliefs in disputed claims. I use these meta-data as additional features in a conjoint setting.

## 5) Specify exactly which analyses you will conduct to examine the main question/hypothesis.

Regress DV on information type (placebo, misinformation, fact-check), closeness of tie, national origin/nativity, perceived trust, perceived political knowledge, ideology, and beliefs in disputed claims, where DV is sharing and plausibility. Standard errors are clustered by respondent. AMCE is the main estimand.

## 6) Describe exactly how outliers will be defined and handled, and your precise rule(s) for excluding observations.

No exclusions

## 7) How many observations will be collected or what will determine sample size?

1500

## 8) Anything else you would like to pre-register?

Possible analyses: (1) conducting subset analyses using age, ideology, beliefs in disputed claims, trust in media, and survey language (marginal means). Tertile splits comparing upper and lower tertiles will be used to assess differences in marginal means, (2) re-weighting the AMCE to account for different assignment probabilities associated with the meta-data fields.

---

## Notes on the data file and the structured plan (not part of the registration)

Added by the depositor. They describe the data and how the registration was operationalized; they do not
add to the registered analysis.

- **Sample and design.** YouGov sample of 1,500 U.S. Hispanic adults, English or Spanish survey. No
  Qualtrics file exists; `inputs/survey.qsf` is reconstructed from the YouGov variable and value labels.
  Respondents named three close contacts ("people with whom you discussed matters important to you") and
  three distant contacts ("people you interact with on a regular basis, but do not consider a close
  contact") and rated each. In each of 4 forced-choice trials they saw two headlines (Message 1 and 2),
  each attributed to one of their six contacts, and chose which they would share and which was more
  plausible. The fielded instrument used 4 trials per respondent, not the 8 stated in item 3.
- **What is randomized.** The headline (and so its information type) and its assignment to a contact.
  The six source attributes are the respondent's own ratings of real people, so they are measured, not
  randomized, and correlated with each other; their AMCEs average over that realized joint distribution.
- **Unit and estimand.** One row per shown profile (1,500 × 4 × 2 = 12,000), `resp_id` = cluster.
  Outcomes `chosen_share`, `chosen_belief`. Features, coded as in the authors' analysis: `infotype`
  (True/neutral = the registration's placebo), `tie`, `sharer_origin`, `sharer_ideology`, `sharer_trust`,
  `sharer_knowledge`, `sharer_conspiracy` (see `survey.qsf` for levels and wording).
- **Structured plan.** `inputs/pap.json` is written by the depositor (`inputs/build_pap.py`), not read
  from this text by a model. Registered: the AMCE of every feature on both outcomes (H1–H14), the
  per-field re-weighting of item 8(2) (R1–R12) and the item 8(1) subgroup marginal means (S1–S10).
  Implemented only, so tagged exploratory: the authors' post hoc analyses (X1–X13 and their subgroups).
- **Data construction.** `inputs/prepare_export.R` builds `inputs/export.csv` from the authors' analysis
  repository and documents every derived column (weights, tertiles, congruence, slant, network aggregates).
