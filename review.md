# Automated review: light pass, advanced pass (methodology + statistics)

Models: light `anthropic/claude-sonnet-5.5`, advanced:methodology `anthropic/claude-sonnet-5.5`, advanced:statistics `anthropic/claude-sonnet-5.5`, orchestrator `anthropic/claude-sonnet-5.5`. The randomized information-type effects are large, precise and consistent across sharing and plausibility: misinformation -18.2 points and fact-checks -13.3 points on sharing. The sharer-trait estimates are measured contrasts and are weaker. Close ties and high trust are the stable ones, and the trait nulls are mostly imprecise. The moderate-sharer result is borderline (p=0.034) and does not hold in the reweighted fit (p=0.056). The key caveat is that the traits are not randomized and the subgroup battery of about 180 contrasts is uncorrected. The paired forced-choice structure is also not modelled, though the report calls the information-type estimates causal.

**Review outcome (round 1): 11 of 12 claims supported by the results after the authors' revision; 11 analytical issues open for a robustness round.**

- **high** R1 (analytical) [address] — Design / H1 / Abstract: Design says respondents compare two profiles per task and choose one, yet outcomes are modeled as per-profile OLS with all 12,000 rows treated as independent choices. Paired-choice dependence within tasks is not handled, and the rating/forced-choice structure is unclear. Mean control shares (~0.5) hint at forced choice.
  - Suggested fix: State clearly how the outcome is constructed. Cluster at respondent and task, or include task fixed effects, and show the AMCEs are robust.
  - Disposition: Re-fit with task fixed effects or task-level clustering as a robustness check, and describe how the outcome is constructed.
- **high** R2 (analytical) [address] — Design / H2-H7, H9-H14: Six sharer traits are measured and not randomized, yet they are called AMCEs and pre-registered as effects. They are confounded with respondent-contact selection and each other. The trust effect (+5.7) rests on only 817 low-trust profiles. Mid and high trust are similar in size, which suggests a non-monotone or noisy pattern.
  - Suggested fix: Label these as conditional associations everywhere, including headings and the abstract. Add respondent fixed effects or respondent-covariate adjustment as a robustness check.
  - Disposition: Add respondent fixed effects or covariate adjustment as a robustness fit; relabel the trait estimates as associations.
- **high** R3 (analytical) [declined] — Abstract / Key findings / H4, H11: About 14 registered tests, 10 subgroup families with 18 contrasts each, and many exploratory tests are uncorrected. Findings such as moderate sharer (p=0.034, p=0.026) and the S-table single-cell differences are presented as effects despite being near threshold. The abstract highlights the moderate-sharer result.
  - Suggested fix: Add multiplicity-adjusted p-values (e.g. Holm or BH by family). Drop or flag the moderate-sharer result as fragile.
  - Disposition: The plan specifies no multiple-testing correction, so adding Holm or BH would change the registered analysis; flag the moderate-sharer result as fragile in prose instead.
- **medium** R4 (analytical) [address] — Key findings / S3: The subgroup result is described as 'Registered subgroup tests show misinformation was shared more by respondents who believe more disputed claims'. These are tertile contrasts of marginal means with no interaction test. The respondent moderator is not randomized, and the true/neutral decline mirrors the rise (a compositional shift in a forced-choice setting).
  - Suggested fix: Report formal interaction tests and describe the pattern as a relative reordering of the information types, not an increase in misinformation sharing.
  - Disposition: Interaction tests on the same data can be reported alongside the registered tertile contrasts.
- **medium** R5 (presentational) [editorial] — Results prose (H6, H13, H12, X8): Several prose figures do not match the tables or are loosely worded. Knowledge mid is '−0.0', and the conspiracy effect is 'at −0.03 points' on a coefficient of −0.000 (−0.034 points is the exact value). X8 and X9 say 'differed by information type (see XS8)', but no XS8 appears. H1 says 'about ±2 to 4 points' for the nulls.
  - Suggested fix: Round consistently, remove the dangling XS8 reference, and make the interval statements match the tables.
  - Disposition: Rounding, the dangling XS8 reference and the interval statements need fixing.
- **medium** R6 (presentational) [editorial] — Design: Missing-data handling is mentioned only in passing: 11,882 of 12,000 profiles are used in the share models, and the report gives no explanation for the 118 dropped. Re-weighting is described as 'very close' even though trust-high moves from 5.7 to 6.7 points.
  - Suggested fix: Report missingness by attribute and the exclusion rule. Describe the re-weighting change accurately.
  - Disposition: Report the missingness rule and describe the reweighting change accurately.
- **medium** R7 (presentational) [address] — Exploratory X1-X11: Exploratory models use a 'treat' term and raw continuous predictors. Descriptions say 'by information type' but the models include no interactions. X6 uses a network-level predictor with 3,196 rows from a smaller set of respondents. X10 rests on 266 ratings. The X11 table is truncated.
  - Suggested fix: Add the interactions that the descriptions promise, or remove those phrases. Report the number of respondents in X6 and X10. Complete the X11 output.
  - Disposition: Fit the promised interactions on the same data, or drop the 'by information type' phrasing; complete the X11 output and report respondent counts.
- **low** R8 (presentational) [editorial] — H1 / E1: The robustness table E1 (dropping trial 1) and E2 (topic) are not discussed in the prose. Health fact-check shows about −0.03 versus political −0.15, which qualifies the pooled fact-check claim.
  - Suggested fix: Discuss E1 and E2 in the text and qualify the pooled fact-check effect.
  - Disposition: Discuss E1 and E2 in the prose and qualify the pooled fact-check effect.
- **medium** A1 (analytical, advanced:methodology) [address] — Design and data / Results H2–H7, H9–H14: Measured sharer traits interpreted as AMCEs without confounding control: Tie, origin, ideology, trust, knowledge and conspiracy belief are respondent ratings of real contacts, not randomized. The 'AMCE' regressions adjust only for the other six features. Unmeasured contact characteristics (e.g., relationship type, closeness history, demographics) are bundled with each trait. Trust and tie are likely correlated with one another and with the contact's identity. The paper flags that these are descriptive, but the labelling as AMCEs and the heading 'effects' still invite causal readings.
  - Suggested fix: Report these as conditional associations. Add contact-level fixed effects or respondent fixed effects to separate within-respondent from between-respondent variation. Avoid causal wording.
  - Disposition: Respondent or contact fixed-effects fits can be added, with associational labels.
- **medium** A2 (analytical, advanced:methodology) [address] — Results H5 / Design: Sparse reference categories and imbalance in measured traits: The Trust: low reference has only 817 eligible profiles, against 8,388 for Trust: high. The Trust: mid CI [−0.1, 7.3] is wide. S1–S5 cells for low trust (e.g., 230–336) are tiny. Foreign origin (about 2,500) is also small. Estimates against thin references are imprecise and sensitive to who lands in them.
  - Suggested fix: Report the trust effect with the continuous 1–5 measure as primary. Show overlap or balance of the measured traits across information types.
  - Disposition: A continuous trust slope (X1) already exists; add a reference-level sensitivity check.
- **medium** A3 (presentational, advanced:methodology) [declined] — Planned heterogeneity S1–S10: Large uncorrected subgroup battery with selective prose reporting: Each of S1–S10 tests 18 contrasts, about 180 tests with no multiplicity adjustment (a policy choice by the authors). Results such as p=0.03 and p=0.038 are discussed alongside strong ones. Tertile splits also reduce power. The key findings headline S3 (5.6 points) without stating that it is one of roughly 180 tests.
  - Suggested fix: Report the number of tests next to the highlights and give the expected number of false positives. Treat the p≈0.01–0.05 results as tentative.
  - Disposition: A correction would conflict with the registered no-correction plan; instead report the number of tests and the expected false positives.
- **medium** A4 (analytical, advanced:methodology) [address] — Results H1 / Design: Forced-choice paired design vs. per-profile OLS and sample accounting: Respondents compare two profiles per task and choose one. The two profiles' outcomes are mechanically complementary, so linear regression on profile rows with respondent clustering ignores the within-task dependence. The N differs across outcomes (11,882 vs 11,884) without an explanation of the missing values. The E1 table shows n_full of 7,967 for H1, which is inconsistent with the H1 N of 11,882. Also, 'n (level)' for misinformation is 3,822 against 3,854 eligible, so the missingness is unexplained.
  - Suggested fix: Clarify the unit of analysis and the pairing. Cluster at the task level or use task fixed effects. Explain the missing data and the E1 sample-size discrepancy.
  - Disposition: Task-clustered re-fit plus an explanation of missingness and of the E1 sample sizes.
- **medium** A5 (presentational, advanced:methodology) [editorial] — Results H4/H11 and Re-weighted AMCEs: Borderline results are described inconsistently across specifications: Moderate sharer on sharing: p=0.034 unweighted, p=0.056 reweighted (−1.7). The text says it 'weakened', while the table still shows the effect as 'supported'. The abstract states the lowering of sharing by 1.9 points without qualification. The Re-weighted section's description of weights (inverse assignment probabilities for measured traits) is also not reproducibly specified.
  - Suggested fix: Qualify the abstract claim as fragile. Specify how the weights were constructed for traits that are not randomized.
  - Disposition: Qualify the moderate-sharer abstract claim and document how the weights were built.
- **medium** A6 (analytical, advanced:methodology) [address] — Exploratory X1–X12: Exploratory models omit controls and are unclear about interactions and the 'treat' variable: X1's formula is `share ~ treat + close_num + ...` but omits information type, though the description promises 'how it differs by information type'. No interaction terms are shown. X5 and X7 are unadjusted cell differences, and X7 relies on 'preliminary automated coding' of slant with no validation. X10 rests on N=266. X6 uses n=3,196 with the respondent-level weight.
  - Suggested fix: Include the interaction terms the text promises. Validate the slant coding. Label the X10 and X6 results as highly tentative.
  - Disposition: Add the interaction terms and information-type controls on the same data; label X6 and X10 as tentative.
- **high** A7 (analytical, advanced:statistics) [address] — X1-X3, X8-X9: Exploratory 'by information type' claims are not supported by the models: The descriptions say slopes are examined 'by information type', but the models contain only a main-effect slope with no interaction term. X8 refers to 'differed by information type (see XS8)', but no such result is shown. The 'treat' term is reused for different variables across models. X1 also omits the information-type arm as a control.
  - Suggested fix: Either fit and report interaction terms, or change the descriptions and remove the unsupported claim in X8.
  - Disposition: Fit the interaction models or remove the unsupported 'by information type' claims and the XS8 reference.
- **medium** A8 (presentational, advanced:statistics) [editorial] — Results H4 / H11: Borderline moderate-sharer effects overinterpreted given multiplicity: The moderate-sharer effect on sharing (p=0.034) is highlighted in the abstract, but its reweighted p is 0.056, and with 14 registered hypotheses plus many sub-tests, it is easily a false positive. The abstract treats it as a finding alongside much stronger ones. The authors do state that tests are uncorrected.
  - Suggested fix: Remove it from the abstract's headline findings or flag it as fragile, stating the reweighted result.
  - Disposition: Flag the moderate-sharer result as fragile in the abstract.
- **medium** A9 (presentational, advanced:statistics) [declined] — Heterogeneity S1-S10: Large subgroup families with no multiplicity handling; selective prose: Each of S1-S10 has 18 contrasts, which gives about 180 tests. Several highlighted effects have p of 0.01-0.04 (S5 low trust p=0.022, S4 p=0.032), and the prose treats them as 'distinguishable from zero'. Cells such as low trust (n=196-343) are small, with SEs of 0.04-0.05. The Key findings bullet presents the S3 subgroup result as a main finding. The policy is 'none', so this is a limitation rather than an error.
  - Suggested fix: Flag that about 9 false positives are expected at 0.05 across ~180 tests, and emphasize only the p<0.001 results (S1 misinformation, S3, S8).
  - Disposition: Correcting the S-family would alter the registered analysis; report the test count and treat p between 0.01 and 0.05 as tentative.
- **medium** A10 (analytical, advanced:statistics) [address] — X4: Conditioning on post-outcome selection: X4 restricts to profiles chosen to share (N=5,938) and compares across randomized arms. Since the arms differ in sharing rates (60% vs 42%), selection into the sample differs by arm, so the comparison is no longer causal.
  - Suggested fix: Acknowledge selection bias, or model the joint outcome (share and plausibility) over all profiles.
  - Disposition: Re-model the joint outcome on all profiles, or label X4 as selected and non-causal.
- **medium** A11 (analytical, advanced:statistics) [address] — Design and data / H1: Causal claim for information type conflicts with within-respondent design and attrition: H1 says 'these are causal estimates', yet the model is adjusted for non-randomized, measured sharer traits (post-treatment-like and possibly correlated with headline assignment). Observations with missing values are dropped (N=11,882 of 12,000), and the E1 drop-trial1 check shows a drop from -0.182 to -0.170. Respondents also rate multiple profiles, and the forced-choice pairing is not described in the estimation, so the 'chosen' outcome mixes pair-level dependence.
  - Suggested fix: Report the unadjusted information-type estimate, state the handling of paired tasks, and temper the causal wording to match the conditions of the design.
  - Disposition: Report the unadjusted information-type AMCE and the task-aware SEs.
- **medium** A12 (analytical, advanced:statistics) [address] — Results H5 / Reweighting: Trust estimates are fragile: reference group small and weighted estimate differs: The low-trust reference cell has only 817 profiles, and the high-trust estimate (0.057, p=0.001) rests on it. Reweighting moves it to 0.067 (about 18% larger), and the 'very close' description is generous. The Trust: mid CI [-0.1, 7.3] is wide. Trust is a measured, not randomized, attribute, and is probably confounded with tie strength.
  - Suggested fix: Report the sensitivity to the choice of reference level, collapse trust into coarser categories or use a continuous trust slope, and describe the weighted shift accurately.
  - Disposition: Use a continuous or collapsed trust robustness fit and describe the weighted shift accurately.
- **medium** K1 (presentational, claims) [editorial] — Abstract: Overstated claim: "fact-checks 13.3 points less often". H1: -0.133 [-0.156,-0.111] is correct pooled, but E2 shows Health fact-check -0.028 (SE 0.028) vs Political -0.151.
  - Suggested fix: Say fact-checks were shared 13.3 points less overall, driven by political items; the health estimate is near zero.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K2 (presentational, claims) [editorial] — Abstract: Overstated claim: "Close ties (+3.0 points) and highly trusted sharers (+5.7 points) raised sharing". H2 +0.030 [0.010,0.050]; H5 Trust: high +0.057 [0.023,0.091]. Both are measured contrasts, and the trust reference cell has only 817 profiles.
  - Suggested fix: Use associational wording: 'were associated with higher sharing'. Note the thin reference cell.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K3 (presentational, claims) [editorial] — Abstract: Overstated claim: "a moderate sharer lowered it by 1.9 points". H4: -0.019, p=0.034, CI [-0.037,-0.001]. Reweighted: -0.017, p=0.056. Measured trait, uncorrected.
  - Suggested fix: Present it as a fragile, near-threshold association, or drop it from the abstract.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K4 (presentational, claims) [editorial] — Key findings: Overstated claim: "intervals of about ±2 to 4 points". Origin and conspiracy intervals are about ±1.6-1.8; knowledge about ±2; the 4-point half-width appears only for trust.
  - Suggested fix: State the actual intervals: roughly ±1.7 to ±2.2 points.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K5 (presentational, claims) [editorial] — Key findings: Overstated claim: "Registered subgroup tests show misinformation was shared more by respondents who believe more disputed claims, by 5.6 points (SE 0.017)". S3: Misinformation +0.056, SE 0.017, p=0.0008, but true/neutral -0.055, a mirrored shift in a forced-choice design. No interaction test. One of about 180 uncorrected contrasts.
  - Suggested fix: Describe it as a relative reordering of information types, report the count of tests, and use an interaction test.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K6 (presentational, claims) [editorial] — Abstract: Overstated claim: "Plausibility judgments followed a similar pattern". H8 matches (-0.186, -0.124), but trust is null for plausibility (H12 high +0.025 [-0.007,0.058]) while it was significant for sharing.
  - Suggested fix: Say the information-type pattern replicates; trust does not carry over to plausibility.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K7 (presentational, claims) [editorial] — H1: Overstated claim: "Information type is the randomized feature, so these are causal estimates". Regression adjusts for six measured traits; E1 drop-trial-1 gives -0.170; pairing of profiles within tasks is not modelled.
  - Suggested fix: Report the unadjusted estimate and task-aware SEs, then keep the causal wording for the randomized arm.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K8 (presentational, claims) [editorial] — Re-weighted AMCEs: Overstated claim: "Re-weighting gave estimates very close to the unweighted ones". Trust: high 0.057 → 0.067; moderate sharer p 0.034 → 0.056.
  - Suggested fix: Say most estimates are unchanged but trust-high rose by about 1 point and moderate-sharer lost significance.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K9 (presentational, claims) [editorial] — X2: Overstated claim: "Each step of trust raised plausibility by 1.3 points". X2 slope 0.013, SE 0.004, exploratory, measured trait; the registered H12 shows no trust effect on plausibility.
  - Suggested fix: Use 'was associated with' and note the conflict with H12.
  - Disposition: claim checked against the tables by the orchestrator

## Claim checks (review orchestrator)

- **supported** (Abstract): "Misinformation was chosen for sharing 18.2 points less often than true or neutral content (95% CI [−20.4, −16.0])" — H1 table: Misinformation -0.182, SE 0.011, CI [-0.204,-0.160], randomized arm.
- **overstated** (Abstract): "fact-checks 13.3 points less often" — H1: -0.133 [-0.156,-0.111] is correct pooled, but E2 shows Health fact-check -0.028 (SE 0.028) vs Political -0.151.
- **overstated** (Abstract): "Close ties (+3.0 points) and highly trusted sharers (+5.7 points) raised sharing" — H2 +0.030 [0.010,0.050]; H5 Trust: high +0.057 [0.023,0.091]. Both are measured contrasts, and the trust reference cell has only 817 profiles.
- **overstated** (Abstract): "a moderate sharer lowered it by 1.9 points" — H4: -0.019, p=0.034, CI [-0.037,-0.001]. Reweighted: -0.017, p=0.056. Measured trait, uncorrected.
- **supported** (Abstract): "Sharer origin, knowledge and belief in disputed claims were not distinguishable from zero" — H3 0.002 [-0.014,0.018]; H6 high 0.017 [-0.005,0.039]; H7 -0.002 [-0.019,0.016].
- **overstated** (Key findings): "intervals of about ±2 to 4 points" — Origin and conspiracy intervals are about ±1.6-1.8; knowledge about ±2; the 4-point half-width appears only for trust.
- **overstated** (Key findings): "Registered subgroup tests show misinformation was shared more by respondents who believe more disputed claims, by 5.6 points (SE 0.017)" — S3: Misinformation +0.056, SE 0.017, p=0.0008, but true/neutral -0.055, a mirrored shift in a forced-choice design. No interaction test. One of about 180 uncorrected contrasts.
- **overstated** (Abstract): "Plausibility judgments followed a similar pattern" — H8 matches (-0.186, -0.124), but trust is null for plausibility (H12 high +0.025 [-0.007,0.058]) while it was significant for sharing.
- **overstated** (H1): "Information type is the randomized feature, so these are causal estimates" — Regression adjusts for six measured traits; E1 drop-trial-1 gives -0.170; pairing of profiles within tasks is not modelled.
- **overstated** (Re-weighted AMCEs): "Re-weighting gave estimates very close to the unweighted ones" — Trust: high 0.057 → 0.067; moderate sharer p 0.034 → 0.056.
- **overstated** (X2): "Each step of trust raised plausibility by 1.3 points" — X2 slope 0.013, SE 0.004, exploratory, measured trait; the registered H12 shows no trust effect on plausibility.

## Editorial guidance

- Relabel all sharer-trait estimates as conditional associations in the abstract, headings and hypothesis text; reserve 'causal' for the randomized information type.
- Qualify the moderate-sharer finding as fragile (p=0.034, reweighted p=0.056) or remove it from the abstract.
- State the number of uncorrected tests (about 14 registered plus about 180 subgroup contrasts) next to every highlighted subgroup result, and describe S3 as a mirrored reordering.
- Explain the unit of analysis (paired forced choice), the 118 dropped rows and the E1 sample discrepancy; add a task-clustered robustness fit.
- Discuss E2: the fact-check effect is near zero for health items. Qualify the pooled 13.3-point claim.
- Fix the prose errors: the '−0.0' value, the XS8 reference, the 'about ±2 to 4' interval, and the 'by information type' descriptions that lack interactions.

## Author response (the writer's revision notes)

- K1: Abstract and takeaway now say fact-checks were shared 13.3 points less overall, driven by political items, with health near zero.
- K2: Reworded to 'associated with'; thin trust reference cell noted in takeaway and H5.
- K3: Moderate-sharer finding removed from abstract; flagged fragile (re-weighted p=0.056) in H4.
- K4: Takeaway now states intervals of roughly ±1.7 to ±2.2 points.
- K5: S3 described as a mirrored reordering, with the count of about 180 uncorrected contrasts; no separate interaction test is available in the tables.
- K6: Abstract now says the information-type pattern replicated but trust did not carry over.
- K7: H1 notes adjustment for measured traits and the E1 estimate; unadjusted and task-clustered fits are not in the tables, so none were added.
- K8: RW note now says most estimates are unchanged, trust-high rose about 1 point, and moderate-sharer lost significance.
- K9: X2 now says 'associated with' and notes conflict with H12.
- G1: Sharer-trait estimates relabelled as conditional associations; causal wording reserved for information type.
- G2: Moderate-sharer finding qualified as fragile and dropped from the abstract.
- G3: Test counts stated in takeaway, abstract and limitations; S3 called a mirrored reordering.
- G4: Design notes explain the paired forced choice and the 118 dropped rows; E1 sample discrepancy flagged as unexplained. A task-clustered fit cannot be added without new results.
- G5: E2 discussed, and the pooled fact-check claim qualified in the abstract, takeaway and H1.
- G6: Fixed the −0.0 value, the conspiracy figure, the XS8 reference, the interval statement, and added interaction wording to XS notes.
- R5: Rounding made consistent, dangling XS8 reference replaced, and interval statements matched to the tables.
- R6: Missingness stated as far as the tables allow (118 dropped; per-attribute breakdown unavailable); re-weighting described accurately.
- R8: E1 and E2 are now discussed in the H1 note, the exploratory notes and the abstract.
- A5: Abstract claim removed; the weight construction for measured traits is described as a sensitivity check, but the exact construction is not in the supplied material.
- A8: Moderate-sharer result removed from the abstract and flagged as fragile in H4.
- R3: Declined; no correction added.
- A3: Declined; test counts reported instead.
- A9: Declined; test count reported and the results treated as tentative.

## Sign-off on the revised text

Only minor wording remains: S1 says other levels differed by 'under 3 points' though the fact-check gap is 3.0; change to 'about 3 points or less'.

- **supported** (Abstract, re-check of C1): "Misinformation was chosen for sharing 18.2 points less often than true or neutral content (95% CI [−20.4, −16.0])" — H1 table: -0.182, CI [-0.204,-0.160]; randomized arm.
- **supported** (Abstract, re-check of C2): "fact-checks were shared 13.3 points less overall, driven by political items" — H1 -0.133; E2 Political fact-check -0.151 vs Health -0.028 (SE 0.028).
- **supported** (Abstract, re-check of C3): "Close ties (+3.0 points) and highly trusted sharers (+5.7 points) were associated with higher sharing" — H2 +0.030 [0.010,0.050]; H5 high +0.057 [0.023,0.091]; associational wording and thin cell noted.
- **supported** (Abstract, re-check of C4): "a moderate sharer lowered it by 1.9 points (abstract mention)" — Removed from the abstract in revision; H4 text now calls it fragile (reweighted p=0.056).
- **supported** (Key findings, re-check of C5): "Sharer origin, political knowledge and belief in disputed claims were not distinguishable from zero for sharing" — H3 [-0.014,0.018]; H6 high [-0.005,0.039]; H7 [-0.019,0.016].
- **supported** (Key findings, re-check of C6): "intervals of roughly ±1.7 to ±2.2 points" — Half-widths: origin 1.6, conspiracy 1.75, knowledge high 2.2.
- **supported** (Key findings, re-check of C7): "Respondents who believe more disputed claims shifted toward misinformation (+5.6 points) and away from true items (−5.5 points). This is a relative reordering" — S3: +0.056 (p=0.0008) and -0.055 (p=0.0004); framed as mirrored reordering, one of ~180 uncorrected contrasts.
- **supported** (Abstract, re-check of C8): "The information-type pattern replicated for plausibility, but trust did not" — H8 -0.186/-0.124; H12 high +0.025 [-0.007,0.058].
- **supported** (H1, re-check of C9): "Information type is randomized, but the model adjusts for six measured traits. An unadjusted fit and a task-clustered fit are not in the tables." — Causal wording qualified; E1 drop-trial-1 -0.170 reported; missing fits disclosed.
- **supported** (Re-weighted AMCEs, re-check of C10): "Re-weighting left most estimates essentially unchanged. High trust rose from 5.7 to 6.7; moderate-sharer lost significance" — RW table: Trust high 0.057→0.067; Moderate 0.056 vs 0.034; others within 0.002.
- **supported** (X2, re-check of C11): "Each step of trust was associated with 1.3 points higher plausibility; conflicts with H12" — X2 slope 0.013 (SE 0.004); associational wording and conflict with H12 noted.
- **overstated** (S1): "The age gap appeared mainly for misinformation: the oldest tertile shared it 6.1 points less (SE 0.016, p<0.001). Other levels differed by under 3 points" — S1 misinformation -0.061, p=0.000165. But Fact-check +0.030 is not under 3 points (it is 3.0), and 'mainly' is loose.

## Unresolved questions (candidates for extensions)

- U1: Does contact trust or closeness change sharing when randomized, for instance via randomly assigned sharer profiles, rather than measured on real contacts? (The traits are respondent ratings of real contacts and are confounded with unmeasured contact characteristics; only a randomized design can separate them.)
- U2: Does misinformation sharing rise with belief in disputed claims in an absolute sense, or only relative to true content, when respondents can decline to share? (The forced-choice design makes the misinformation increase and the true-content decrease mechanically linked.)
- U3: Do fact-checks reduce sharing equally for health and political claims? (The topic cells are small (about 1,100 health profiles) and topic was not randomized.)

Analytical issues can be answered with robustness addenda: `filedrawer address <study>` proposes one per issue for approval.
