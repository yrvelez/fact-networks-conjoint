# Automated review: light pass

Models: light `anthropic/claude-sonnet-5.5`, orchestrator `anthropic/claude-sonnet-5.5`. The registered contrasts are internally consistent with the tables: Misinformation and Fact-check headlines were chosen less often than True/neutral for both sharing and plausibility, with tight intervals. The text understates two things, though. The comparison is against True/neutral content rather than a no-treatment baseline. The estimates also come from a covariate-adjusted model that deviates from the plan, and the deviation is undocumented. The most important caveat is that the unit of analysis and the coding of the paired forced choice are unclear, so the percentage-point magnitudes are hard to interpret. The exploratory trial and theme analyses use different estimators from the registered models and are over-interpreted in places.

- **high** R1 (analytical) [address] — H1/H2 deviation: Both hypotheses are tagged as deviations (sharer_trust, sharer_knowledge, sharer_disputed added as covariates; registered covariate set is null) with no justification, and the report says the effect is 'unknown' without checking it.
  - Suggested fix: Report the registered specification (arm only, or the registered covariates) alongside the deviating model, and state why covariates were added.
  - Disposition: Re-fitting the registered covariate specification (arm only) alongside the adjusted model is a robustness re-fit on the same data.
- **medium** R2 (analytical) [editorial] — Design and data / Results: The 12,000 'responses' are described as respondents but the conjoint has four trials per respondent (E2 n≈2,972 per trial). Arm n's (3,822 + 3,915 + 4,145) are rows. The unit and the number of respondents are unclear. Binary forced choice between headlines also means shares are not independent across the pair. Control and arm shares of about 60%, 42% and 47% are not clearly interpretable.
  - Suggested fix: State the number of respondents, rows per respondent, and how the choice outcome is coded for paired headlines. Check that clustering handles within-pair dependence.
  - Disposition: The report needs to state respondent counts, rows per respondent, and how the choice outcome is coded; the models are already clustered on resp_id.
- **medium** R3 (presentational) [editorial] — Design and data: The design says 'two treatment arms and a control', but the covariates are about a 'sharer' in an ego network (title: 'Who shares what from whom'). The ego-network and source dimension is never described or analysed, and the covariates are not explained.
  - Suggested fix: Describe the conjoint attributes and the sharer variables, and explain why only the information-type effect is reported.
  - Disposition: The conjoint attributes and sharer variables need to be described, and the report should explain why only the information-type effect is reported.
- **medium** R4 (analytical) [address] — E1: E1 uses IPW with HC2, not the cluster-robust SEs of the registered models, so the repeated trials per respondent are ignored. The sample is reduced to n=9,910. The prose says 'significantly weaker' without any multiplicity caveat. The 'is_conservative' coding is undefined. The table's term labels are truncated and do not distinguish main effects from interactions.
  - Suggested fix: Re-fit with respondent clustering, define the conservative coding, label the interaction terms, and describe the result as suggestive.
  - Disposition: E1 can be re-fit with respondent clustering, and the conservative coding and term labels can be defined.
- **medium** R5 (analytical) [address] — E2: The E2 finding claims 'ruling out order effects or fatigue' and also says a 'mild fatigue/order effect' exists. This is contradictory. No formal test of trial×arm interaction is given. The weights and SE types differ from the registered models.
  - Suggested fix: Fit a trial×arm interaction with clustering and reword the claim.
  - Disposition: A clustered trial×arm interaction can be fit on the existing data, and the claim can be reworded.
- **medium** R6 (presentational) [declined] — E3: E3 runs 30 theme-by-arm estimates without multiplicity correction. The prose says the overall result is 'driven by a subset of themes' and that the range includes +0.152, but that positive value (Debt, p=0.026) is likely noise. Most of the table is truncated ('18 more rows').
  - Suggested fix: Show the full table, apply a correction or a heterogeneity test, and soften the 'driven by a subset' claim.
  - Disposition: The plan specifies no multiple-testing correction, so a correction is not applied; E3 is exploratory, and the full table and a heterogeneity test can still be shown with softer wording.
- **low** R7 (analytical) [address] — H2 / Abstract: The report says Misinformation's drop is larger than Fact-check's on plausibility, but gives no direct test of the difference. The abstract's 'all four tests p<0.001' is fine, but the 'Fact-check lowered sharing' result may reflect the placebo's own content differences.
  - Suggested fix: Add a Wald test of Misinformation vs Fact-check, and note that the control is 'True/neutral' content, not a no-treatment baseline.
  - Disposition: A Wald test of Misinformation vs Fact-check is an additional estimate on the same model; the control caveat is a wording fix.
- **low** R8 (presentational) [editorial] — Related work: The retrieved literature is mostly irrelevant, and the section adds little.
  - Suggested fix: Trim it or replace it with relevant misinformation-sharing literature.
  - Disposition: The related-work section should be trimmed or replaced with relevant literature.
- **medium** K1 (presentational, claims) [editorial] — H2: Overstated claim: "Misinformation's drop is larger than Fact-check's, though the intervals are close". H2_arms.csv: -0.186 vs -0.124. The CIs overlap only slightly, but no direct test of the difference is reported.
  - Suggested fix: Add a Wald test of Misinformation vs Fact-check, or say the difference was not formally tested.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K2 (presentational, claims) [editorial] — H1: Overstated claim: "Both treatment arms lowered the chance that a headline was chosen for sharing". The reference is True/neutral content, not a no-treatment baseline. The estimates are differences between headline types in forced choices, and the model is covariate-adjusted, which departs from the plan.
  - Suggested fix: Say that Misinformation and Fact-check headlines were chosen less often than True/neutral headlines.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K3 (presentational, claims) [editorial] — Key findings: Overstated claim: "Fact-check headlines lowered the sharing choice, so both information types lowered it". H1_arms.csv shows -0.133 for Fact-check. This is a contrast with the True/neutral placebo headlines and may reflect content differences between headline types.
  - Suggested fix: Describe it as a difference relative to True/neutral headlines, not a causal lowering by information type.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K4 (presentational, claims) [editorial] — E1 / Key findings: Overstated claim: "The sharing effects vary by respondent ideology: weaker among conservatives". E1 interactions: +0.104 [0.041,0.166], +0.112 [0.050,0.173]. The model is IPW with HC2 errors rather than clustered errors, on a reduced n=9,910 sample, so the intervals are likely too narrow.
  - Suggested fix: Re-fit with respondent clustering and call the result suggestive.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K5 (presentational, claims) [editorial] — E2: Overstated claim: "Misinformation effect declines modestly from −0.200 in trial 1 to −0.140 in trial 4, ruling out order effects or fatigue". E2 table: -0.200 to -0.140. The paper itself calls this a mild fatigue/order effect, which contradicts 'ruling out', and no trial×arm interaction test is given.
  - Suggested fix: Drop 'ruling out'. Report the decline and add an interaction test.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K6 (presentational, claims) [editorial] — E3: Overstated claim: "Overall negative result is driven by a subset of themes; range −0.325 to +0.152". E3 table: range is correct, but Debt's +0.152 has p=0.026 with 30 uncorrected estimates, and most of the table is truncated. 'Driven by a subset' is not tested.
  - Suggested fix: Show the full table, test heterogeneity formally, and describe the variation as exploratory.
  - Disposition: claim checked against the tables by the orchestrator

## Claim checks (review orchestrator)

- **supported** (Abstract): "Misinformation was chosen for sharing 18.2 percentage points less often (95% CI [−20.4, −16.0])" — H1_arms.csv Misinformation: -0.182, CI [-0.204,-0.160]; control 0.603 vs 0.421.
- **supported** (Abstract): "Fact-check 13.3 points less often (95% CI [−15.6, −11.1])" — H1_arms.csv Fact-check: -0.133, CI [-0.156,-0.111]; 0.603 vs 0.470.
- **supported** (Abstract): "Misinformation was 18.6 points lower and Fact-check 12.4 points lower on plausibility" — H2_arms.csv: -0.186 [-0.208,-0.164]; -0.124 [-0.147,-0.102].
- **supported** (Abstract): "All four tests were two-sided with p<0.001" — registered_summary.csv p-values range from 8.61e-59 to 1.7e-27, all two-sided.
- **overstated** (H2): "Misinformation's drop is larger than Fact-check's, though the intervals are close" — H2_arms.csv: -0.186 vs -0.124. The CIs overlap only slightly, but no direct test of the difference is reported.
- **overstated** (H1): "Both treatment arms lowered the chance that a headline was chosen for sharing" — The reference is True/neutral content, not a no-treatment baseline. The estimates are differences between headline types in forced choices, and the model is covariate-adjusted, which departs from the plan.
- **overstated** (Key findings): "Fact-check headlines lowered the sharing choice, so both information types lowered it" — H1_arms.csv shows -0.133 for Fact-check. This is a contrast with the True/neutral placebo headlines and may reflect content differences between headline types.
- **overstated** (E1 / Key findings): "The sharing effects vary by respondent ideology: weaker among conservatives" — E1 interactions: +0.104 [0.041,0.166], +0.112 [0.050,0.173]. The model is IPW with HC2 errors rather than clustered errors, on a reduced n=9,910 sample, so the intervals are likely too narrow.
- **overstated** (E2): "Misinformation effect declines modestly from −0.200 in trial 1 to −0.140 in trial 4, ruling out order effects or fatigue" — E2 table: -0.200 to -0.140. The paper itself calls this a mild fatigue/order effect, which contradicts 'ruling out', and no trial×arm interaction test is given.
- **overstated** (E3): "Overall negative result is driven by a subset of themes; range −0.325 to +0.152" — E3 table: range is correct, but Debt's +0.152 has p=0.026 with 30 uncorrected estimates, and most of the table is truncated. 'Driven by a subset' is not tested.

## Editorial guidance

- Document the undocumented deviation: state that trust, knowledge and disputed covariates were added, why, and report the registered specification next to it.
- State the number of respondents, rows per respondent, and how the paired forced-choice outcome is coded.
- Describe all arms as contrasts with True/neutral content, not as effects of 'lowering' sharing relative to no information.
- Fix E2 wording that both rules out and finds a fatigue effect, and soften the E3 'driven by a subset' claim.
- Define is_conservative, label E1 interaction terms, and print the full E3 table.
- Trim the irrelevant related-work list.

## Unresolved questions (candidates for extensions)

- U1: Does real-world sharing of misinformation and fact-checks on social platforms differ from forced-choice headline selection, and by how much? (The study measures only binary forced choices between headlines, not actual sharing behavior.)
- U2: Is the Fact-check vs True/neutral difference due to information type or to differences in the content of the placebo headlines? (The design has no no-information baseline and headline content is not randomized independently of type.)

Analytical issues can be answered with robustness addenda: `filedrawer address <study>` proposes one per issue for approval.
