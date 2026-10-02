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

## Notes on the data file (not part of the registration)

Added by the depositor to map the registration onto `inputs/export.csv`. These notes describe the
data; they do not add to or change the registered analysis.

- **Sample and design.** YouGov sample of 1,500 U.S. Hispanic adults, English or Spanish survey. No
  Qualtrics file exists for this survey. Respondents first named three close contacts ("people with
  whom you discussed matters important to you") and three distant contacts ("people you interact
  with on a regular basis, but do not consider a close contact"), then rated each contact. In each
  of 4 forced-choice trials they saw two headlines (profiles A and B), each attributed to one of their
  six named contacts, and chose which one they would share and which was more plausible. The fielded
  instrument used 4 trials per respondent, not the 8 stated in item 3.
- **Unit of analysis.** One row per shown profile: 1,500 respondents × 4 trials × 2 profiles = 12,000
  rows. `resp_id` is the respondent (cluster) identifier.
- **Outcomes.** `chosen_share` = 1 if this profile was chosen in "which would you share" (sharing);
  `chosen_belief` = 1 if chosen in "which is more plausible" (plausibility). Missing = item nonresponse.
- **Information type** (randomized headline): `infotype` = "True/neutral" (the registration's
  "placebo"), "Misinformation", or "Fact-check". Headlines were randomly assigned to contacts.
- **Source attributes** (respondent's ratings of the contact the headline was attributed to; not
  randomized themselves, only the headline-to-contact assignment is):
  - `close_tie`: 1 = close contact, 0 = distant contact (closeness of tie).
  - `sharer_native_us`: 1 = contact is from the continental U.S., 0 = otherwise (national origin/nativity).
  - `sharer_trust`: 1-5, 5 = most trusted (perceived trust).
  - `sharer_knowledge`: 1-5, 5 = most knowledgeable about politics (perceived political knowledge).
  - `sharer_ideology`: Liberal / Moderate / Conservative ("Don't know" coded Moderate).
  - `sharer_disputed`: share of six disputed claims the respondent thinks the contact believes, 0-1
    (beliefs in disputed claims).
- **Respondent covariates for the registered subset analyses:** `age` (years), `ideo5_self` (1 = very
  liberal … 5 = very conservative; "not sure" is missing), `disputed_self` (share of six disputed
  claims the respondent believes, 0-1), `media_trust` (mean of six media-trust items), and
  `survey_language` (English / Spanish).
- **Other columns:** `trial`, `profile`, `headline_theme` (topic of the headline). `weight` is the
  YouGov survey weight; the registration does not mention survey weights.
