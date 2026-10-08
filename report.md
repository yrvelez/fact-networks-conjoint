# Who Shares What From Whom: An Ego-Network Conjoint of Misinformation Sharing

*Yamil R. Velez · 2026-10-07 · N = 12,000 analysed of 12,000 collected · conjoint experiment*

<!-- fd:badges -->
![provenance: fully agentic](figures/badges/provenance.svg) ![review: light pass · 12/12 claims supported](figures/badges/review.svg) [![plan: pre-registered #132,508](figures/badges/registration.svg)](https://aspredicted.org/8njc-mpqw.pdf) ![status: draft](figures/badges/release.svg) ![design: conjoint](figures/badges/design.svg) ![data: open data](figures/badges/data.svg) ![model calls: $2.60](figures/badges/cost.svg)

> **Provenance: FULLY AGENTIC — no human review recorded.** filedrawer 0.1.0, 2026-10-07; orchestrator `anthropic/claude-sonnet-5.5`, standard `qwen/qwen3.8-27b`, zero data retention requested. Reviewer pass: yes. Human steps recorded: 0. Release status: draft. Model calls: $2.60, 1142k tokens in and 35k out. Cite as: Velez, Y. R. (2026). Who Shares What From Whom: An Ego-Network Conjoint of Misinformation Sharing [Unpublished study package, generated with filedrawer 0.1.0]. The File Drawer. https://github.com/yrvelez/fact-networks-conjoint

<!-- fd:section id=abstract -->
## Abstract

Who shares misinformation, and from whom? We ran a registered conjoint experiment with a YouGov sample of US respondents (12,000 profile ratings collected; models use 11,882 for sharing and 11,884 for plausibility). Each respondent saw a true or neutral headline, a false headline, or a fact-check, attributed to one of their real contacts, and chose whether to share it and rated its plausibility. Information type was randomized. Misinformation was chosen for sharing 18.2 points less often than true or neutral headlines (95% CI [−20.4, −16.0]), and fact-checks 13.3 points less often (95% CI [−15.6, −11.1]). Plausibility showed a similar pattern. Among the measured source attributes, close ties (+3.0 points, 95% CI [1.0, 5.0]) and high trust in the sharer relative to low trust (+5.7 points, 95% CI [2.3, 9.1]) were associated with more sharing, while origin, knowledge and conspiracy belief were not distinguishable from zero. Respondents with greater belief in disputed claims shared misinformation more. Caveats: many uncorrected tests, and the source attributes are measured, not randomized.

<!-- fd:section id=findings -->
## Key findings

- In this registered conjoint, information type shaped sharing most: misinformation headlines were chosen 18.2 points less often than true/neutral ones (95% CI [−20.4, −16.0], p < 0.001).
- Fact-check headlines were also chosen less often than true/neutral ones, by 13.3 points (95% CI [−15.6, −11.1]). Plausibility ratings tracked sharing closely.
- Among measured sharer attributes, close ties were associated with 3.0 points more sharing (95% CI [1.0, 5.0]) and high trust with 5.7 points more (95% CI [2.3, 9.1]); origin, knowledge and conspiracy belief were not distinguishable from zero.
- Registered subgroups showed that respondents with higher belief in disputed claims shared misinformation 5.6 points more than those with lower belief (p < 0.001), and true/neutral content less.
- Many tests were run without correction, sharer attributes are measured rather than randomized, and the ideology and subgroup findings sit near conventional thresholds.

<!-- fd:section id=design -->
## Design and data

A conjoint experiment with 7 profile features: randomized, Information type (True/neutral, Misinformation, Fact-check); measured rather than randomized (the respondent's own ratings of the real contact each headline was attributed to; only the headline and its assignment to a contact are randomized), Tie strength (Distant tie, Close tie); Sharer origin (Foreign origin, Continental US); Sharer ideology (Liberal sharer, Moderate sharer, Conservative sharer); Trust in sharer (Trust: low, Trust: mid, Trust: high); Sharer political knowledge (Knowledge: low, Knowledge: mid, Knowledge: high); Sharer belief in disputed claims (Conspiracy belief: low, Conspiracy belief: high); yougov, US. 12,000 responses were collected and 12,000 are analysed. The plan is pre-registered at https://aspredicted.org/8njc-mpqw.pdf. Identifier and free-text columns removed before any model saw the data: none.

![Design at a glance](figures/design.svg)

#### Details: the design in words

A conjoint experiment on yougov respondents in US (N = 12,000 analysed). Each profile is built from 7 features: Information type (True/neutral, Misinformation, Fact-check); Tie strength (Distant tie, Close tie; measured, not randomized); Sharer origin (Foreign origin, Continental US; measured, not randomized); Sharer ideology (Liberal sharer, Moderate sharer, Conservative sharer; measured, not randomized); Trust in sharer (Trust: low, Trust: mid, Trust: high; measured, not randomized); Sharer political knowledge (Knowledge: low, Knowledge: mid, Knowledge: high; measured, not randomized); Sharer belief in disputed claims (Conspiracy belief: low, Conspiracy belief: high; measured, not randomized). Respondents compare two profiles per task and choose one for each outcome. Outcomes: Chosen to share, Chosen as more plausible. Registered moderators: age_t, ideo_self_t, disp_self_t, media_t, survey_language.


Respondents were a YouGov sample of US adults. Of 12,000 raw profile ratings, the models use 11,882 for sharing and 11,884 for plausibility. Each profile attributed a headline to one of the respondent's real contacts. Only the headline type and its assignment to a contact were randomized. Tie strength, origin, ideology, trust, knowledge and conspiracy belief are measured attributes of those contacts, so their AMCEs are descriptive contrasts that bundle correlated attributes, not causal effects. True/neutral headlines are the reference level for information type (3,822 misinformation and 3,915 fact-check profiles in the sharing model). Standard errors are clustered by respondent, and tests are two-sided.

<!-- fd:section id=results -->
## Results

![Effects of every profile feature on chosen to share (AMCEs, 95% CI)](figures/amce_share.png)

![Effects of every profile feature on chosen as more plausible (AMCEs, 95% CI)](figures/amce_plausibility.png)

<!-- fd:hyp id=H1 tag=registered outcome=share -->
### H1. Information type → sharing

*AMCE of information type on sharing: each level against 'True/neutral', from the regression of sharing on all seven profile features, SEs clustered by respondent.*  
*Pre-registered.*

Information type had large effects on sharing. Misinformation was chosen 18.2 points less often than true or neutral headlines (95% CI [−20.4, −16.0], p < 0.001), and fact-checks 13.3 points less often (95% CI [−15.6, −11.1], p < 0.001). Chosen shares were 60.3% for true/neutral, 42.1% for misinformation and 47.0% for fact-checks. These are causal contrasts, because headline type was randomized.

#### Details: model and estimates by arm (H1)

```
share ~ C(arm_code, Treatment(reference='True/neutral')) + C(tie) + C(sharer_origin) + C(sharer_ideology) + C(sharer_trust) + C(sharer_knowledge) + C(sharer_conspiracy)
OLS | cluster-robust SEs on resp_id | N = 11882 | two-sided test, alpha = 0.05
```

| Level | Estimate | SE | p | 95% CI | n (level) | Supported |
|---|---|---|---|---|---|---|
| Misinformation | -0.182 | 0.011 | < 0.0001 | [-0.204, -0.160] | 3822 | yes |
| Fact-check | -0.133 | 0.011 | < 0.0001 | [-0.156, -0.111] | 3915 | yes |

<!-- fd:hyp id=H2 tag=registered outcome=share -->
### H2. Tie strength → sharing

*AMCE of tie strength on sharing: each level against 'Distant tie', from the regression of sharing on all seven profile features, SEs clustered by respondent.*  
*Pre-registered.*

Close ties were chosen for sharing 3.0 points more often than distant ties (95% CI [1.0, 5.0], p = 0.003). This is a descriptive contrast on a measured attribute.

#### Details: model and estimates by arm (H2)

```
share ~ C(arm_code, Treatment(reference='Distant tie')) + C(infotype) + C(sharer_origin) + C(sharer_ideology) + C(sharer_trust) + C(sharer_knowledge) + C(sharer_conspiracy)
OLS | cluster-robust SEs on resp_id | N = 11882 | two-sided test, alpha = 0.05
```

| Level | Estimate | SE | p | 95% CI | n (level) | Supported |
|---|---|---|---|---|---|---|
| Close tie | 0.030 | 0.010 | 0.0032 | [0.010, 0.050] | 6662 | yes |

<!-- fd:hyp id=H3 tag=registered outcome=share -->
### H3. Sharer origin → sharing

*AMCE of sharer origin on sharing: each level against 'Foreign origin', from the regression of sharing on all seven profile features, SEs clustered by respondent.*  
*Pre-registered.*

Continental US origin was 0.2 points above foreign origin (95% CI [−1.4, 1.8], p = 0.81). This is not distinguishable from zero.

#### Details: model and estimates by arm (H3)

```
share ~ C(arm_code, Treatment(reference='Foreign origin')) + C(infotype) + C(tie) + C(sharer_ideology) + C(sharer_trust) + C(sharer_knowledge) + C(sharer_conspiracy)
OLS | cluster-robust SEs on resp_id | N = 11882 | two-sided test, alpha = 0.05
```

| Level | Estimate | SE | p | 95% CI | n (level) | Supported |
|---|---|---|---|---|---|---|
| Continental US | 0.002 | 0.008 | 0.8143 | [-0.014, 0.018] | 9400 | no |

<!-- fd:hyp id=H4 tag=registered outcome=share -->
### H4. Sharer ideology → sharing

*AMCE of sharer ideology on sharing: each level against 'Liberal sharer', from the regression of sharing on all seven profile features, SEs clustered by respondent.*  
*Pre-registered.*

A moderate sharer was chosen 1.9 points less often than a liberal sharer (95% CI [−3.7, −0.1], p = 0.034), a small difference close to the threshold. Conservative sharers were not distinguishable from liberal ones (−0.7 points, 95% CI [−2.8, 1.5]).

#### Details: model and estimates by arm (H4)

```
share ~ C(arm_code, Treatment(reference='Liberal sharer')) + C(infotype) + C(tie) + C(sharer_origin) + C(sharer_trust) + C(sharer_knowledge) + C(sharer_conspiracy)
OLS | cluster-robust SEs on resp_id | N = 11882 | two-sided test, alpha = 0.05
```

| Level | Estimate | SE | p | 95% CI | n (level) | Supported |
|---|---|---|---|---|---|---|
| Moderate sharer | -0.019 | 0.009 | 0.0337 | [-0.037, -0.001] | 6538 | yes |
| Conservative sharer | -0.007 | 0.011 | 0.5470 | [-0.028, 0.015] | 2536 | no |

<!-- fd:hyp id=H5 tag=registered outcome=share -->
### H5. Trust in sharer → sharing

*AMCE of trust in sharer on sharing: each level against 'Trust: low', from the regression of sharing on all seven profile features, SEs clustered by respondent.*  
*Pre-registered.*

High trust in the sharer was associated with 5.7 points more sharing than low trust (95% CI [2.3, 9.1], p < 0.001). Mid trust was 3.6 points higher, with an interval that includes zero (95% CI [−0.1, 7.3]).

#### Details: model and estimates by arm (H5)

```
share ~ C(arm_code, Treatment(reference='Trust: low')) + C(infotype) + C(tie) + C(sharer_origin) + C(sharer_ideology) + C(sharer_knowledge) + C(sharer_conspiracy)
OLS | cluster-robust SEs on resp_id | N = 11882 | two-sided test, alpha = 0.05
```

| Level | Estimate | SE | p | 95% CI | n (level) | Supported |
|---|---|---|---|---|---|---|
| Trust: mid | 0.036 | 0.019 | 0.0561 | [-0.001, 0.073] | 2677 | no |
| Trust: high | 0.057 | 0.017 | 0.0010 | [0.023, 0.091] | 8388 | yes |

<!-- fd:hyp id=H6 tag=registered outcome=share -->
### H6. Sharer political knowledge → sharing

*AMCE of sharer political knowledge on sharing: each level against 'Knowledge: low', from the regression of sharing on all seven profile features, SEs clustered by respondent.*  
*Pre-registered.*

Neither mid nor high sharer knowledge was distinguishable from low. High knowledge was 1.7 points higher (95% CI [−0.5, 3.9]); mid was about zero.

#### Details: model and estimates by arm (H6)

```
share ~ C(arm_code, Treatment(reference='Knowledge: low')) + C(infotype) + C(tie) + C(sharer_origin) + C(sharer_ideology) + C(sharer_trust) + C(sharer_conspiracy)
OLS | cluster-robust SEs on resp_id | N = 11882 | two-sided test, alpha = 0.05
```

| Level | Estimate | SE | p | 95% CI | n (level) | Supported |
|---|---|---|---|---|---|---|
| Knowledge: mid | -0.000 | 0.010 | 0.9619 | [-0.020, 0.019] | 5273 | no |
| Knowledge: high | 0.017 | 0.011 | 0.1265 | [-0.005, 0.039] | 4564 | no |

<!-- fd:hyp id=H7 tag=registered outcome=share -->
### H7. Sharer belief in disputed claims → sharing

*AMCE of sharer belief in disputed claims on sharing: each level against 'Conspiracy belief: low', from the regression of sharing on all seven profile features, SEs clustered by respondent.*  
*Pre-registered.*

A sharer with high belief in disputed claims was not distinguishable from one with low belief on sharing (−0.2 points, 95% CI [−1.9, 1.6], p = 0.87).

#### Details: model and estimates by arm (H7)

```
share ~ C(arm_code, Treatment(reference='Conspiracy belief: low')) + C(infotype) + C(tie) + C(sharer_origin) + C(sharer_ideology) + C(sharer_trust) + C(sharer_knowledge)
OLS | cluster-robust SEs on resp_id | N = 11882 | two-sided test, alpha = 0.05
```

| Level | Estimate | SE | p | 95% CI | n (level) | Supported |
|---|---|---|---|---|---|---|
| Conspiracy belief: high | -0.002 | 0.009 | 0.8655 | [-0.019, 0.016] | 8675 | no |

<!-- fd:hyp id=H8 tag=registered outcome=plausibility -->
### H8. Information type → plausibility

*AMCE of information type on plausibility: each level against 'True/neutral', from the regression of plausibility on all seven profile features, SEs clustered by respondent.*  
*Pre-registered.*

Misinformation was rated 18.6 points less plausible than true or neutral headlines (95% CI [−20.8, −16.4], p < 0.001), and fact-checks 12.4 points less plausible (95% CI [−14.7, −10.2], p < 0.001). The pattern closely mirrors sharing.

#### Details: model and estimates by arm (H8)

```
plausibility ~ C(arm_code, Treatment(reference='True/neutral')) + C(tie) + C(sharer_origin) + C(sharer_ideology) + C(sharer_trust) + C(sharer_knowledge) + C(sharer_conspiracy)
OLS | cluster-robust SEs on resp_id | N = 11884 | two-sided test, alpha = 0.05
```

| Level | Estimate | SE | p | 95% CI | n (level) | Supported |
|---|---|---|---|---|---|---|
| Misinformation | -0.186 | 0.011 | < 0.0001 | [-0.208, -0.164] | 3821 | yes |
| Fact-check | -0.124 | 0.011 | < 0.0001 | [-0.147, -0.102] | 3918 | yes |

<!-- fd:hyp id=H9 tag=registered outcome=plausibility -->
### H9. Tie strength → plausibility

*AMCE of tie strength on plausibility: each level against 'Distant tie', from the regression of plausibility on all seven profile features, SEs clustered by respondent.*  
*Pre-registered.*

Close ties were associated with 2.8 points higher plausibility than distant ties (95% CI [0.7, 4.8], p = 0.008), a modest contrast on a measured attribute.

#### Details: model and estimates by arm (H9)

```
plausibility ~ C(arm_code, Treatment(reference='Distant tie')) + C(infotype) + C(sharer_origin) + C(sharer_ideology) + C(sharer_trust) + C(sharer_knowledge) + C(sharer_conspiracy)
OLS | cluster-robust SEs on resp_id | N = 11884 | two-sided test, alpha = 0.05
```

| Level | Estimate | SE | p | 95% CI | n (level) | Supported |
|---|---|---|---|---|---|---|
| Close tie | 0.028 | 0.010 | 0.0079 | [0.007, 0.048] | 6664 | yes |

<!-- fd:hyp id=H10 tag=registered outcome=plausibility -->
### H10. Sharer origin → plausibility

*AMCE of sharer origin on plausibility: each level against 'Foreign origin', from the regression of plausibility on all seven profile features, SEs clustered by respondent.*  
*Pre-registered.*

Sharer origin was not distinguishable from zero for plausibility (−0.3 points, 95% CI [−1.9, 1.4]).

#### Details: model and estimates by arm (H10)

```
plausibility ~ C(arm_code, Treatment(reference='Foreign origin')) + C(infotype) + C(tie) + C(sharer_ideology) + C(sharer_trust) + C(sharer_knowledge) + C(sharer_conspiracy)
OLS | cluster-robust SEs on resp_id | N = 11884 | two-sided test, alpha = 0.05
```

| Level | Estimate | SE | p | 95% CI | n (level) | Supported |
|---|---|---|---|---|---|---|
| Continental US | -0.003 | 0.008 | 0.7462 | [-0.019, 0.014] | 9402 | no |

<!-- fd:hyp id=H11 tag=registered outcome=plausibility -->
### H11. Sharer ideology → plausibility

*AMCE of sharer ideology on plausibility: each level against 'Liberal sharer', from the regression of plausibility on all seven profile features, SEs clustered by respondent.*  
*Pre-registered.*

Moderate sharers were rated 2.1 points less plausible than liberal ones (95% CI [−4.0, −0.3], p = 0.026), a small contrast near the threshold. Conservative sharers were −1.9 points (95% CI [−4.1, 0.3]), not distinguishable from zero.

#### Details: model and estimates by arm (H11)

```
plausibility ~ C(arm_code, Treatment(reference='Liberal sharer')) + C(infotype) + C(tie) + C(sharer_origin) + C(sharer_trust) + C(sharer_knowledge) + C(sharer_conspiracy)
OLS | cluster-robust SEs on resp_id | N = 11884 | two-sided test, alpha = 0.05
```

| Level | Estimate | SE | p | 95% CI | n (level) | Supported |
|---|---|---|---|---|---|---|
| Moderate sharer | -0.021 | 0.009 | 0.0257 | [-0.040, -0.003] | 6539 | yes |
| Conservative sharer | -0.019 | 0.011 | 0.0870 | [-0.041, 0.003] | 2537 | no |

<!-- fd:hyp id=H12 tag=registered outcome=plausibility -->
### H12. Trust in sharer → plausibility

*AMCE of trust in sharer on plausibility: each level against 'Trust: low', from the regression of plausibility on all seven profile features, SEs clustered by respondent.*  
*Pre-registered.*

Neither mid nor high trust was distinguishable from low for plausibility. High trust was 2.5 points higher (95% CI [−0.7, 5.8]).

#### Details: model and estimates by arm (H12)

```
plausibility ~ C(arm_code, Treatment(reference='Trust: low')) + C(infotype) + C(tie) + C(sharer_origin) + C(sharer_ideology) + C(sharer_knowledge) + C(sharer_conspiracy)
OLS | cluster-robust SEs on resp_id | N = 11884 | two-sided test, alpha = 0.05
```

| Level | Estimate | SE | p | 95% CI | n (level) | Supported |
|---|---|---|---|---|---|---|
| Trust: mid | -0.006 | 0.018 | 0.7497 | [-0.042, 0.030] | 2675 | no |
| Trust: high | 0.025 | 0.017 | 0.1276 | [-0.007, 0.058] | 8392 | no |

<!-- fd:hyp id=H13 tag=registered outcome=plausibility -->
### H13. Sharer political knowledge → plausibility

*AMCE of sharer political knowledge on plausibility: each level against 'Knowledge: low', from the regression of plausibility on all seven profile features, SEs clustered by respondent.*  
*Pre-registered.*

Sharer knowledge was not distinguishable from zero for plausibility. High knowledge was 1.7 points higher (95% CI [−0.4, 3.8]); mid was about zero.

#### Details: model and estimates by arm (H13)

```
plausibility ~ C(arm_code, Treatment(reference='Knowledge: low')) + C(infotype) + C(tie) + C(sharer_origin) + C(sharer_ideology) + C(sharer_trust) + C(sharer_conspiracy)
OLS | cluster-robust SEs on resp_id | N = 11884 | two-sided test, alpha = 0.05
```

| Level | Estimate | SE | p | 95% CI | n (level) | Supported |
|---|---|---|---|---|---|---|
| Knowledge: mid | -0.001 | 0.010 | 0.9172 | [-0.021, 0.019] | 5271 | no |
| Knowledge: high | 0.017 | 0.011 | 0.1188 | [-0.004, 0.038] | 4567 | no |

<!-- fd:hyp id=H14 tag=registered outcome=plausibility -->
### H14. Sharer belief in disputed claims → plausibility

*AMCE of sharer belief in disputed claims on plausibility: each level against 'Conspiracy belief: low', from the regression of plausibility on all seven profile features, SEs clustered by respondent.*  
*Pre-registered.*

Sharer belief in disputed claims was not distinguishable from zero for plausibility (0.0 points, 95% CI [−1.8, 1.8]).

#### Details: model and estimates by arm (H14)

```
plausibility ~ C(arm_code, Treatment(reference='Conspiracy belief: low')) + C(infotype) + C(tie) + C(sharer_origin) + C(sharer_ideology) + C(sharer_trust) + C(sharer_knowledge)
OLS | cluster-robust SEs on resp_id | N = 11884 | two-sided test, alpha = 0.05
```

| Level | Estimate | SE | p | 95% CI | n (level) | Supported |
|---|---|---|---|---|---|---|
| Conspiracy belief: high | -0.000 | 0.009 | 0.9700 | [-0.018, 0.018] | 8677 | no |

<!-- fd:group id=RW -->
### Re-weighted AMCEs: each source attribute re-weighted by its inverse assignment probability

*Pre-registered. Analyses R1–R12.*

Re-weighting each source attribute by the inverse of its assignment probability left the picture largely unchanged. Close ties were still associated with 3.0 points more sharing and 2.7 points higher plausibility, and high trust with 6.7 points more sharing (95% CI [3.3, 10.1]). The weighted moderate-sharer contrast on sharing was −1.7 points (95% CI [−3.5, 0.0]) and is not significant at 0.05 (p = 0.056); on plausibility it stayed at −2.1 points. High trust on plausibility remained not distinguishable from zero. The other estimates were not distinguishable from zero.

| Outcome | Feature | Level | Estimate | 95% CI | p | Without weights |
|---|---|---|---|---|---|---|
| Chosen to share | Tie strength | Close tie | 0.030 | [0.010, 0.050] | 0.003 | 0.030 (H2) |
| Chosen to share | Sharer origin | Continental US | 0.003 | [-0.013, 0.019] | 0.706 | 0.002 (H3) |
| Chosen to share | Sharer ideology | Moderate sharer | -0.017 | [-0.035, 0.000] | 0.056 | -0.019 (H4) |
| Chosen to share | Sharer ideology | Conservative sharer | -0.007 | [-0.028, 0.015] | 0.552 | -0.007 (H4) |
| Chosen to share | Trust in sharer | Trust: mid | 0.034 | [-0.002, 0.070] | 0.061 | 0.036 (H5) |
| Chosen to share | Trust in sharer | Trust: high | 0.067 | [0.033, 0.101] | < 0.001 | 0.057 (H5) |
| Chosen to share | Sharer political knowledge | Knowledge: mid | -0.001 | [-0.020, 0.019] | 0.960 | -0.000 (H6) |
| Chosen to share | Sharer political knowledge | Knowledge: high | 0.017 | [-0.005, 0.039] | 0.138 | 0.017 (H6) |
| Chosen to share | Sharer belief in disputed claims | Conspiracy belief: high | -0.001 | [-0.019, 0.016] | 0.878 | -0.002 (H7) |
| Chosen as more plausible | Tie strength | Close tie | 0.027 | [0.007, 0.048] | 0.008 | 0.028 (H9) |
| Chosen as more plausible | Sharer origin | Continental US | -0.003 | [-0.019, 0.014] | 0.745 | -0.003 (H10) |
| Chosen as more plausible | Sharer ideology | Moderate sharer | -0.021 | [-0.039, -0.002] | 0.030 | -0.021 (H11) |
| Chosen as more plausible | Sharer ideology | Conservative sharer | -0.019 | [-0.042, 0.003] | 0.085 | -0.019 (H11) |
| Chosen as more plausible | Trust in sharer | Trust: mid | -0.008 | [-0.043, 0.027] | 0.646 | -0.006 (H12) |
| Chosen as more plausible | Trust in sharer | Trust: high | 0.029 | [-0.003, 0.062] | 0.079 | 0.025 (H12) |
| Chosen as more plausible | Sharer political knowledge | Knowledge: mid | -0.001 | [-0.021, 0.019] | 0.901 | -0.001 (H13) |
| Chosen as more plausible | Sharer political knowledge | Knowledge: high | 0.015 | [-0.006, 0.037] | 0.160 | 0.017 (H13) |
| Chosen as more plausible | Sharer belief in disputed claims | Conspiracy belief: high | -0.001 | [-0.019, 0.017] | 0.945 | -0.000 (H14) |

<!-- fd:group id=heterogeneity -->
### Planned heterogeneity

<!-- fd:hyp id=S1 tag=registered kind=subgroup -->
#### S1. Marginal means of every feature level on sharing: highest minus lowest tertile of age

*Moderator `age_t`. Pre-registered.*

| analysis_id | feature | level | mm_Lowest | mm_Highest | difference | std_error | p_value | n_Lowest | n_Highest |
|---|---|---|---|---|---|---|---|---|---|
| S1 | infotype | Fact-check | 0.454 | 0.484 | 0.030 | 0.017 | 0.072 | 1305 | 1291 |
| S1 | infotype | Misinformation | 0.455 | 0.394 | -0.061 | 0.016 | 0.000165 | 1275 | 1282 |
| S1 | infotype | True/neutral | 0.585 | 0.611 | 0.026 | 0.015 | 0.094 | 1418 | 1407 |
| S1 | tie | Close tie | 0.516 | 0.511 | -0.005 | 0.011 | 0.663 | 2259 | 2193 |
| S1 | tie | Distant tie | 0.481 | 0.487 | 0.005 | 0.014 | 0.718 | 1739 | 1784 |
| S1 | sharer_origin | Continental US | 0.503 | 0.503 | 0.000186 | 0.004 | 0.966 | 2837 | 3357 |
| S1 | sharer_origin | Foreign origin | 0.496 | 0.482 | -0.014 | 0.016 | 0.385 | 1154 | 598 |
| S1 | sharer_ideology | Conservative sharer | 0.516 | 0.492 | -0.023 | 0.018 | 0.187 | 669 | 1036 |
| S1 | sharer_ideology | Liberal sharer | 0.510 | 0.535 | 0.025 | 0.016 | 0.117 | 1012 | 898 |
| S1 | sharer_ideology | Moderate sharer | 0.493 | 0.489 | -0.003 | 0.008 | 0.676 | 2315 | 2029 |
| S1 | sharer_trust | Trust: high | 0.511 | 0.509 | -0.002 | 0.006 | 0.680 | 2744 | 2937 |
| S1 | sharer_trust | Trust: low | 0.464 | 0.439 | -0.025 | 0.039 | 0.518 | 336 | 230 |
| S1 | sharer_trust | Trust: mid | 0.482 | 0.485 | 0.003 | 0.016 | 0.845 | 915 | 808 |
| S1 | sharer_knowledge | Knowledge: high | 0.512 | 0.518 | 0.005 | 0.011 | 0.621 | 1456 | 1719 |
| S1 | sharer_knowledge | Knowledge: low | 0.501 | 0.484 | -0.017 | 0.020 | 0.379 | 722 | 661 |
| S1 | sharer_knowledge | Knowledge: mid | 0.491 | 0.487 | -0.004 | 0.010 | 0.698 | 1820 | 1590 |
| S1 | sharer_conspiracy | Conspiracy belief: high | 0.504 | 0.499 | -0.005 | 0.006 | 0.405 | 2949 | 2870 |
| S1 | sharer_conspiracy | Conspiracy belief: low | 0.491 | 0.501 | 0.010 | 0.016 | 0.512 | 1049 | 1107 |

Age moderated the response to information type. Respondents in the highest age tertile shared misinformation 6.1 points less than the lowest tertile (p < 0.001). Differences for the other levels were not distinguishable from zero. These are descriptive subgroup contrasts.

<!-- fd:hyp id=S2 tag=registered kind=subgroup -->
#### S2. Marginal means of every feature level on sharing: highest minus lowest tertile of respondent ideology (1 very liberal ... 5 very conservative)

*Moderator `ideo_self_t`. Pre-registered.*

| analysis_id | feature | level | mm_Lowest | mm_Highest | difference | std_error | p_value | n_Lowest | n_Highest |
|---|---|---|---|---|---|---|---|---|---|
| S2 | infotype | Fact-check | 0.477 | 0.486 | 0.009 | 0.018 | 0.622 | 1110 | 1127 |
| S2 | infotype | Misinformation | 0.414 | 0.439 | 0.025 | 0.019 | 0.191 | 1062 | 1055 |
| S2 | infotype | True/neutral | 0.619 | 0.562 | -0.056 | 0.018 | 0.002 | 1151 | 1138 |
| S2 | tie | Close tie | 0.516 | 0.517 | 0.000961 | 0.013 | 0.940 | 1915 | 1838 |
| S2 | tie | Distant tie | 0.492 | 0.472 | -0.020 | 0.016 | 0.225 | 1408 | 1482 |
| S2 | sharer_origin | Continental US | 0.512 | 0.496 | -0.016 | 0.006 | 0.005 | 2617 | 2707 |
| S2 | sharer_origin | Foreign origin | 0.484 | 0.503 | 0.019 | 0.020 | 0.327 | 694 | 602 |
| S2 | sharer_ideology | Conservative sharer | 0.495 | 0.515 | 0.020 | 0.023 | 0.391 | 416 | 1352 |
| S2 | sharer_ideology | Liberal sharer | 0.539 | 0.491 | -0.048 | 0.020 | 0.017 | 1575 | 521 |
| S2 | sharer_ideology | Moderate sharer | 0.471 | 0.484 | 0.013 | 0.014 | 0.352 | 1326 | 1439 |
| S2 | sharer_trust | Trust: high | 0.519 | 0.511 | -0.008 | 0.007 | 0.268 | 2447 | 2444 |
| S2 | sharer_trust | Trust: low | 0.479 | 0.429 | -0.050 | 0.049 | 0.306 | 259 | 196 |
| S2 | sharer_trust | Trust: mid | 0.465 | 0.466 | 0.001 | 0.022 | 0.964 | 617 | 680 |
| S2 | sharer_knowledge | Knowledge: high | 0.531 | 0.522 | -0.009 | 0.012 | 0.454 | 1534 | 1463 |
| S2 | sharer_knowledge | Knowledge: low | 0.473 | 0.467 | -0.006 | 0.023 | 0.802 | 560 | 582 |
| S2 | sharer_knowledge | Knowledge: mid | 0.490 | 0.483 | -0.007 | 0.015 | 0.607 | 1222 | 1272 |
| S2 | sharer_conspiracy | Conspiracy belief: high | 0.508 | 0.497 | -0.010 | 0.007 | 0.158 | 2377 | 2569 |
| S2 | sharer_conspiracy | Conspiracy belief: low | 0.502 | 0.497 | -0.005 | 0.019 | 0.779 | 946 | 751 |

Respondent ideology mattered for a few levels. More conservative respondents shared true/neutral headlines 5.6 points less (p = 0.002), shared less from continental US sharers (−1.6 points, p = 0.005), and shared less from liberal sharers (−4.8 points, p = 0.017). Most other differences were not distinguishable from zero.

<!-- fd:hyp id=S3 tag=registered kind=subgroup -->
#### S3. Marginal means of every feature level on sharing: highest minus lowest tertile of respondent belief in disputed claims

*Moderator `disp_self_t`. Pre-registered.*

| analysis_id | feature | level | mm_Lowest | mm_Highest | difference | std_error | p_value | n_Lowest | n_Highest |
|---|---|---|---|---|---|---|---|---|---|
| S3 | infotype | Fact-check | 0.485 | 0.457 | -0.028 | 0.017 | 0.094 | 1295 | 1318 |
| S3 | infotype | Misinformation | 0.397 | 0.453 | 0.056 | 0.017 | 0.000766 | 1271 | 1287 |
| S3 | infotype | True/neutral | 0.623 | 0.567 | -0.055 | 0.016 | 0.000437 | 1420 | 1380 |
| S3 | tie | Close tie | 0.526 | 0.506 | -0.020 | 0.012 | 0.096 | 2194 | 2246 |
| S3 | tie | Distant tie | 0.482 | 0.478 | -0.004 | 0.015 | 0.802 | 1790 | 1739 |
| S3 | sharer_origin | Continental US | 0.509 | 0.492 | -0.017 | 0.005 | 0.002 | 3196 | 3064 |
| S3 | sharer_origin | Foreign origin | 0.496 | 0.498 | 0.002 | 0.016 | 0.919 | 776 | 906 |
| S3 | sharer_ideology | Conservative sharer | 0.492 | 0.515 | 0.022 | 0.019 | 0.254 | 662 | 1131 |
| S3 | sharer_ideology | Liberal sharer | 0.532 | 0.512 | -0.020 | 0.018 | 0.259 | 991 | 813 |
| S3 | sharer_ideology | Moderate sharer | 0.499 | 0.476 | -0.023 | 0.009 | 0.013 | 2325 | 2034 |
| S3 | sharer_trust | Trust: high | 0.527 | 0.504 | -0.023 | 0.007 | 0.000886 | 2648 | 2922 |
| S3 | sharer_trust | Trust: low | 0.410 | 0.437 | 0.027 | 0.037 | 0.470 | 300 | 270 |
| S3 | sharer_trust | Trust: mid | 0.481 | 0.476 | -0.005 | 0.017 | 0.760 | 1031 | 790 |
| S3 | sharer_knowledge | Knowledge: high | 0.542 | 0.513 | -0.029 | 0.012 | 0.016 | 1397 | 1652 |
| S3 | sharer_knowledge | Knowledge: low | 0.487 | 0.456 | -0.031 | 0.022 | 0.159 | 630 | 664 |
| S3 | sharer_knowledge | Knowledge: mid | 0.487 | 0.490 | 0.003 | 0.010 | 0.773 | 1948 | 1669 |
| S3 | sharer_conspiracy | Conspiracy belief: high | 0.504 | 0.494 | -0.010 | 0.007 | 0.169 | 2488 | 3312 |
| S3 | sharer_conspiracy | Conspiracy belief: low | 0.509 | 0.492 | -0.017 | 0.019 | 0.369 | 1496 | 673 |

Respondents with greater belief in disputed claims shared misinformation 5.6 points more than those with the least (p < 0.001) and true/neutral headlines 5.5 points less (p < 0.001). They also shared less from high-trust sharers (−2.3 points, p < 0.001) and continental US sharers (−1.7 points, p = 0.002).

<!-- fd:hyp id=S4 tag=registered kind=subgroup -->
#### S4. Marginal means of every feature level on sharing: highest minus lowest tertile of trust in media

*Moderator `media_t`. Pre-registered.*

| analysis_id | feature | level | mm_Lowest | mm_Highest | difference | std_error | p_value | n_Lowest | n_Highest |
|---|---|---|---|---|---|---|---|---|---|
| S4 | infotype | Fact-check | 0.478 | 0.465 | -0.013 | 0.016 | 0.428 | 1281 | 1355 |
| S4 | infotype | Misinformation | 0.402 | 0.449 | 0.048 | 0.016 | 0.003 | 1260 | 1295 |
| S4 | infotype | True/neutral | 0.603 | 0.590 | -0.013 | 0.016 | 0.418 | 1444 | 1338 |
| S4 | tie | Close tie | 0.525 | 0.511 | -0.014 | 0.011 | 0.235 | 2257 | 2229 |
| S4 | tie | Distant tie | 0.465 | 0.490 | 0.025 | 0.015 | 0.088 | 1728 | 1756 |
| S4 | sharer_origin | Continental US | 0.500 | 0.502 | 0.002 | 0.005 | 0.594 | 3330 | 2914 |
| S4 | sharer_origin | Foreign origin | 0.493 | 0.503 | 0.010 | 0.015 | 0.502 | 643 | 1041 |
| S4 | sharer_ideology | Conservative sharer | 0.516 | 0.489 | -0.026 | 0.018 | 0.131 | 861 | 885 |
| S4 | sharer_ideology | Liberal sharer | 0.520 | 0.523 | 0.003 | 0.016 | 0.843 | 965 | 1049 |
| S4 | sharer_ideology | Moderate sharer | 0.483 | 0.498 | 0.015 | 0.009 | 0.086 | 2153 | 2031 |
| S4 | sharer_trust | Trust: high | 0.517 | 0.512 | -0.005 | 0.006 | 0.404 | 2651 | 3103 |
| S4 | sharer_trust | Trust: low | 0.440 | 0.433 | -0.007 | 0.041 | 0.862 | 343 | 217 |
| S4 | sharer_trust | Trust: mid | 0.472 | 0.480 | 0.007 | 0.019 | 0.696 | 991 | 659 |
| S4 | sharer_knowledge | Knowledge: high | 0.540 | 0.516 | -0.024 | 0.011 | 0.028 | 1410 | 1909 |
| S4 | sharer_knowledge | Knowledge: low | 0.472 | 0.491 | 0.019 | 0.020 | 0.329 | 805 | 584 |
| S4 | sharer_knowledge | Knowledge: mid | 0.479 | 0.489 | 0.010 | 0.011 | 0.326 | 1770 | 1489 |
| S4 | sharer_conspiracy | Conspiracy belief: high | 0.503 | 0.495 | -0.008 | 0.007 | 0.199 | 2733 | 3044 |
| S4 | sharer_conspiracy | Conspiracy belief: low | 0.490 | 0.525 | 0.035 | 0.016 | 0.032 | 1252 | 941 |

Respondents with higher media trust shared misinformation 4.8 points more than those with low media trust (p = 0.003). They also shared less from high-knowledge sharers (−2.4 points, p = 0.028) and more from low-conspiracy sharers (+3.5 points, p = 0.032). Other differences were not distinguishable from zero.

<!-- fd:hyp id=S5 tag=registered kind=subgroup -->
#### S5. Marginal means of every feature level on sharing: Spanish minus English survey language

*Moderator `survey_language`. Pre-registered.*

| analysis_id | feature | level | mm_English | mm_Spanish | difference | std_error | p_value | n_English | n_Spanish |
|---|---|---|---|---|---|---|---|---|---|
| S5 | infotype | Fact-check | 0.470 | 0.469 | -0.000581 | 0.014 | 0.967 | 2650 | 1300 |
| S5 | infotype | Misinformation | 0.409 | 0.445 | 0.036 | 0.014 | 0.010 | 2509 | 1336 |
| S5 | infotype | True/neutral | 0.610 | 0.584 | -0.025 | 0.014 | 0.070 | 2823 | 1350 |
| S5 | tie | Close tie | 0.519 | 0.508 | -0.011 | 0.010 | 0.243 | 4464 | 2245 |
| S5 | tie | Distant tie | 0.475 | 0.489 | 0.014 | 0.012 | 0.258 | 3515 | 1741 |
| S5 | sharer_origin | Continental US | 0.502 | 0.501 | -0.000777 | 0.004 | 0.848 | 6514 | 2914 |
| S5 | sharer_origin | Foreign origin | 0.491 | 0.498 | 0.007 | 0.013 | 0.595 | 1461 | 1029 |
| S5 | sharer_ideology | Conservative sharer | 0.500 | 0.515 | 0.016 | 0.015 | 0.282 | 1605 | 945 |
| S5 | sharer_ideology | Liberal sharer | 0.524 | 0.507 | -0.017 | 0.015 | 0.259 | 1969 | 856 |
| S5 | sharer_ideology | Moderate sharer | 0.490 | 0.492 | 0.002 | 0.007 | 0.759 | 4405 | 2157 |
| S5 | sharer_trust | Trust: high | 0.515 | 0.508 | -0.007 | 0.005 | 0.143 | 5620 | 2820 |
| S5 | sharer_trust | Trust: low | 0.415 | 0.494 | 0.079 | 0.035 | 0.022 | 571 | 257 |
| S5 | sharer_trust | Trust: mid | 0.479 | 0.476 | -0.003 | 0.014 | 0.826 | 1788 | 900 |
| S5 | sharer_knowledge | Knowledge: high | 0.522 | 0.520 | -0.002 | 0.011 | 0.844 | 3401 | 1194 |
| S5 | sharer_knowledge | Knowledge: low | 0.470 | 0.502 | 0.032 | 0.015 | 0.038 | 1150 | 915 |
| S5 | sharer_knowledge | Knowledge: mid | 0.488 | 0.487 | -0.001 | 0.008 | 0.877 | 3428 | 1866 |
| S5 | sharer_conspiracy | Conspiracy belief: high | 0.503 | 0.497 | -0.006 | 0.005 | 0.246 | 5694 | 3044 |
| S5 | sharer_conspiracy | Conspiracy belief: low | 0.493 | 0.510 | 0.016 | 0.015 | 0.267 | 2285 | 942 |

Spanish-language respondents shared misinformation 3.6 points more than English-language ones (p = 0.010). They also shared more from low-trust sharers (+7.9 points, p = 0.022; cells of only 257 Spanish and 571 English profiles) and low-knowledge sharers (+3.2 points, p = 0.038). Most other differences were not distinguishable from zero, and with many comparisons some of these may be chance.

<!-- fd:hyp id=S6 tag=registered kind=subgroup -->
#### S6. Marginal means of every feature level on plausibility: highest minus lowest tertile of age

*Moderator `age_t`. Pre-registered.*

| analysis_id | feature | level | mm_Lowest | mm_Highest | difference | std_error | p_value | n_Lowest | n_Highest |
|---|---|---|---|---|---|---|---|---|---|
| S6 | infotype | Fact-check | 0.467 | 0.484 | 0.017 | 0.016 | 0.298 | 1305 | 1294 |
| S6 | infotype | Misinformation | 0.436 | 0.396 | -0.040 | 0.016 | 0.013 | 1275 | 1283 |
| S6 | infotype | True/neutral | 0.591 | 0.607 | 0.016 | 0.016 | 0.303 | 1418 | 1407 |
| S6 | tie | Close tie | 0.510 | 0.515 | 0.005 | 0.011 | 0.667 | 2259 | 2195 |
| S6 | tie | Distant tie | 0.489 | 0.479 | -0.010 | 0.014 | 0.504 | 1739 | 1786 |
| S6 | sharer_origin | Continental US | 0.500 | 0.502 | 0.002 | 0.004 | 0.637 | 2837 | 3361 |
| S6 | sharer_origin | Foreign origin | 0.503 | 0.482 | -0.021 | 0.017 | 0.207 | 1154 | 598 |
| S6 | sharer_ideology | Conservative sharer | 0.505 | 0.479 | -0.026 | 0.019 | 0.163 | 669 | 1038 |
| S6 | sharer_ideology | Liberal sharer | 0.502 | 0.539 | 0.037 | 0.016 | 0.020 | 1012 | 898 |
| S6 | sharer_ideology | Moderate sharer | 0.500 | 0.493 | -0.007 | 0.008 | 0.414 | 2315 | 2031 |
| S6 | sharer_trust | Trust: high | 0.513 | 0.509 | -0.004 | 0.005 | 0.491 | 2744 | 2941 |
| S6 | sharer_trust | Trust: low | 0.494 | 0.461 | -0.033 | 0.038 | 0.377 | 336 | 230 |
| S6 | sharer_trust | Trust: mid | 0.467 | 0.474 | 0.007 | 0.017 | 0.658 | 915 | 808 |
| S6 | sharer_knowledge | Knowledge: high | 0.524 | 0.513 | -0.011 | 0.010 | 0.309 | 1456 | 1722 |
| S6 | sharer_knowledge | Knowledge: low | 0.497 | 0.491 | -0.006 | 0.019 | 0.740 | 722 | 662 |
| S6 | sharer_knowledge | Knowledge: mid | 0.484 | 0.487 | 0.003 | 0.010 | 0.737 | 1820 | 1590 |
| S6 | sharer_conspiracy | Conspiracy belief: high | 0.505 | 0.496 | -0.009 | 0.006 | 0.130 | 2949 | 2873 |
| S6 | sharer_conspiracy | Conspiracy belief: low | 0.490 | 0.507 | 0.017 | 0.016 | 0.274 | 1049 | 1108 |

Older respondents rated misinformation 4.0 points less plausible than younger ones (p = 0.013), and liberal sharers 3.7 points more plausible (p = 0.020). Other differences were not distinguishable from zero.

<!-- fd:hyp id=S7 tag=registered kind=subgroup -->
#### S7. Marginal means of every feature level on plausibility: highest minus lowest tertile of respondent ideology (1 very liberal ... 5 very conservative)

*Moderator `ideo_self_t`. Pre-registered.*

| analysis_id | feature | level | mm_Lowest | mm_Highest | difference | std_error | p_value | n_Lowest | n_Highest |
|---|---|---|---|---|---|---|---|---|---|
| S7 | infotype | Fact-check | 0.480 | 0.486 | 0.006 | 0.018 | 0.760 | 1114 | 1128 |
| S7 | infotype | Misinformation | 0.405 | 0.423 | 0.019 | 0.019 | 0.323 | 1060 | 1056 |
| S7 | infotype | True/neutral | 0.620 | 0.571 | -0.049 | 0.018 | 0.006 | 1151 | 1138 |
| S7 | tie | Close tie | 0.511 | 0.513 | 0.002 | 0.013 | 0.872 | 1917 | 1839 |
| S7 | tie | Distant tie | 0.496 | 0.473 | -0.023 | 0.016 | 0.159 | 1408 | 1483 |
| S7 | sharer_origin | Continental US | 0.508 | 0.493 | -0.015 | 0.006 | 0.009 | 2618 | 2709 |
| S7 | sharer_origin | Foreign origin | 0.492 | 0.502 | 0.010 | 0.020 | 0.630 | 695 | 602 |
| S7 | sharer_ideology | Conservative sharer | 0.480 | 0.513 | 0.033 | 0.024 | 0.161 | 415 | 1354 |
| S7 | sharer_ideology | Liberal sharer | 0.535 | 0.509 | -0.026 | 0.020 | 0.194 | 1575 | 521 |
| S7 | sharer_ideology | Moderate sharer | 0.477 | 0.475 | -0.002 | 0.014 | 0.867 | 1327 | 1439 |
| S7 | sharer_trust | Trust: high | 0.518 | 0.507 | -0.011 | 0.007 | 0.130 | 2450 | 2446 |
| S7 | sharer_trust | Trust: low | 0.494 | 0.449 | -0.045 | 0.045 | 0.320 | 259 | 196 |
| S7 | sharer_trust | Trust: mid | 0.455 | 0.465 | 0.010 | 0.023 | 0.655 | 616 | 680 |
| S7 | sharer_knowledge | Knowledge: high | 0.530 | 0.517 | -0.013 | 0.012 | 0.276 | 1536 | 1464 |
| S7 | sharer_knowledge | Knowledge: low | 0.486 | 0.472 | -0.014 | 0.022 | 0.525 | 562 | 583 |
| S7 | sharer_knowledge | Knowledge: mid | 0.482 | 0.481 | -0.000835 | 0.015 | 0.954 | 1220 | 1272 |
| S7 | sharer_conspiracy | Conspiracy belief: high | 0.507 | 0.495 | -0.012 | 0.007 | 0.106 | 2379 | 2570 |
| S7 | sharer_conspiracy | Conspiracy belief: low | 0.500 | 0.497 | -0.003 | 0.020 | 0.892 | 946 | 752 |

More conservative respondents rated true/neutral headlines 4.9 points less plausible (p = 0.006) and continental-US-attributed profiles 1.5 points less plausible (p = 0.009). Other differences were not distinguishable from zero.

<!-- fd:hyp id=S8 tag=registered kind=subgroup -->
#### S8. Marginal means of every feature level on plausibility: highest minus lowest tertile of respondent belief in disputed claims

*Moderator `disp_self_t`. Pre-registered.*

| analysis_id | feature | level | mm_Lowest | mm_Highest | difference | std_error | p_value | n_Lowest | n_Highest |
|---|---|---|---|---|---|---|---|---|---|
| S8 | infotype | Fact-check | 0.486 | 0.473 | -0.013 | 0.017 | 0.464 | 1297 | 1319 |
| S8 | infotype | Misinformation | 0.381 | 0.450 | 0.068 | 0.017 | 4.25e-05 | 1269 | 1288 |
| S8 | infotype | True/neutral | 0.628 | 0.559 | -0.069 | 0.016 | 1.58e-05 | 1420 | 1380 |
| S8 | tie | Close tie | 0.520 | 0.502 | -0.018 | 0.012 | 0.125 | 2195 | 2247 |
| S8 | tie | Distant tie | 0.483 | 0.486 | 0.003 | 0.014 | 0.820 | 1789 | 1740 |
| S8 | sharer_origin | Continental US | 0.506 | 0.495 | -0.011 | 0.006 | 0.044 | 3196 | 3066 |
| S8 | sharer_origin | Foreign origin | 0.496 | 0.494 | -0.002 | 0.017 | 0.922 | 776 | 906 |
| S8 | sharer_ideology | Conservative sharer | 0.492 | 0.511 | 0.019 | 0.019 | 0.320 | 661 | 1133 |
| S8 | sharer_ideology | Liberal sharer | 0.532 | 0.528 | -0.004 | 0.018 | 0.819 | 991 | 813 |
| S8 | sharer_ideology | Moderate sharer | 0.495 | 0.475 | -0.020 | 0.009 | 0.030 | 2326 | 2034 |
| S8 | sharer_trust | Trust: high | 0.528 | 0.503 | -0.024 | 0.007 | 0.000396 | 2650 | 2924 |
| S8 | sharer_trust | Trust: low | 0.433 | 0.474 | 0.041 | 0.036 | 0.259 | 300 | 270 |
| S8 | sharer_trust | Trust: mid | 0.464 | 0.472 | 0.009 | 0.017 | 0.615 | 1029 | 790 |
| S8 | sharer_knowledge | Knowledge: high | 0.548 | 0.512 | -0.036 | 0.012 | 0.002 | 1399 | 1653 |
| S8 | sharer_knowledge | Knowledge: low | 0.492 | 0.460 | -0.032 | 0.022 | 0.139 | 630 | 665 |
| S8 | sharer_knowledge | Knowledge: mid | 0.476 | 0.493 | 0.017 | 0.010 | 0.106 | 1946 | 1669 |
| S8 | sharer_conspiracy | Conspiracy belief: high | 0.502 | 0.495 | -0.007 | 0.007 | 0.334 | 2489 | 3313 |
| S8 | sharer_conspiracy | Conspiracy belief: low | 0.506 | 0.497 | -0.009 | 0.019 | 0.647 | 1495 | 674 |

Respondents with greater belief in disputed claims rated misinformation 6.8 points more plausible (p < 0.001) and true/neutral headlines 6.9 points less plausible (p < 0.001). They also gave lower plausibility to high-trust sharers (−2.4 points, p < 0.001) and high-knowledge sharers (−3.6 points, p = 0.002).

<!-- fd:hyp id=S9 tag=registered kind=subgroup -->
#### S9. Marginal means of every feature level on plausibility: highest minus lowest tertile of trust in media

*Moderator `media_t`. Pre-registered.*

| analysis_id | feature | level | mm_Lowest | mm_Highest | difference | std_error | p_value | n_Lowest | n_Highest |
|---|---|---|---|---|---|---|---|---|---|
| S9 | infotype | Fact-check | 0.482 | 0.479 | -0.003 | 0.016 | 0.848 | 1284 | 1357 |
| S9 | infotype | Misinformation | 0.403 | 0.446 | 0.044 | 0.016 | 0.007 | 1259 | 1295 |
| S9 | infotype | True/neutral | 0.602 | 0.584 | -0.018 | 0.016 | 0.252 | 1444 | 1338 |
| S9 | tie | Close tie | 0.523 | 0.516 | -0.008 | 0.011 | 0.510 | 2259 | 2230 |
| S9 | tie | Distant tie | 0.470 | 0.488 | 0.018 | 0.015 | 0.220 | 1728 | 1757 |
| S9 | sharer_origin | Continental US | 0.503 | 0.502 | -0.000837 | 0.005 | 0.858 | 3331 | 2916 |
| S9 | sharer_origin | Foreign origin | 0.488 | 0.509 | 0.022 | 0.016 | 0.184 | 644 | 1041 |
| S9 | sharer_ideology | Conservative sharer | 0.509 | 0.488 | -0.021 | 0.018 | 0.237 | 862 | 885 |
| S9 | sharer_ideology | Liberal sharer | 0.522 | 0.532 | 0.010 | 0.016 | 0.549 | 965 | 1049 |
| S9 | sharer_ideology | Moderate sharer | 0.487 | 0.497 | 0.010 | 0.009 | 0.255 | 2152 | 2033 |
| S9 | sharer_trust | Trust: high | 0.520 | 0.510 | -0.009 | 0.006 | 0.120 | 2654 | 3105 |
| S9 | sharer_trust | Trust: low | 0.464 | 0.493 | 0.030 | 0.041 | 0.475 | 343 | 217 |
| S9 | sharer_trust | Trust: mid | 0.462 | 0.476 | 0.015 | 0.019 | 0.432 | 990 | 659 |
| S9 | sharer_knowledge | Knowledge: high | 0.541 | 0.515 | -0.026 | 0.011 | 0.019 | 1411 | 1911 |
| S9 | sharer_knowledge | Knowledge: low | 0.488 | 0.497 | 0.009 | 0.020 | 0.647 | 808 | 584 |
| S9 | sharer_knowledge | Knowledge: mid | 0.473 | 0.492 | 0.018 | 0.011 | 0.096 | 1768 | 1489 |
| S9 | sharer_conspiracy | Conspiracy belief: high | 0.509 | 0.497 | -0.012 | 0.007 | 0.070 | 2734 | 3046 |
| S9 | sharer_conspiracy | Conspiracy belief: low | 0.482 | 0.526 | 0.044 | 0.017 | 0.009 | 1253 | 941 |

Respondents with higher media trust rated misinformation 4.4 points more plausible (p = 0.007) and low-conspiracy sharers 4.4 points more plausible (p = 0.009). They rated high-knowledge sharers 2.6 points less plausible (p = 0.019).

<!-- fd:hyp id=S10 tag=registered kind=subgroup -->
#### S10. Marginal means of every feature level on plausibility: Spanish minus English survey language

*Moderator `survey_language`. Pre-registered.*

| analysis_id | feature | level | mm_English | mm_Spanish | difference | std_error | p_value | n_English | n_Spanish |
|---|---|---|---|---|---|---|---|---|---|
| S10 | infotype | Fact-check | 0.479 | 0.469 | -0.010 | 0.014 | 0.470 | 2653 | 1302 |
| S10 | infotype | Misinformation | 0.404 | 0.440 | 0.037 | 0.014 | 0.008 | 2508 | 1336 |
| S10 | infotype | True/neutral | 0.605 | 0.589 | -0.016 | 0.014 | 0.238 | 2823 | 1350 |
| S10 | tie | Close tie | 0.518 | 0.506 | -0.012 | 0.010 | 0.215 | 4466 | 2246 |
| S10 | tie | Distant tie | 0.477 | 0.492 | 0.015 | 0.013 | 0.227 | 3515 | 1742 |
| S10 | sharer_origin | Continental US | 0.501 | 0.499 | -0.002 | 0.004 | 0.643 | 6516 | 2915 |
| S10 | sharer_origin | Foreign origin | 0.494 | 0.501 | 0.007 | 0.013 | 0.608 | 1461 | 1030 |
| S10 | sharer_ideology | Conservative sharer | 0.495 | 0.503 | 0.008 | 0.015 | 0.611 | 1606 | 945 |
| S10 | sharer_ideology | Liberal sharer | 0.527 | 0.511 | -0.017 | 0.014 | 0.250 | 1969 | 856 |
| S10 | sharer_ideology | Moderate sharer | 0.490 | 0.496 | 0.006 | 0.007 | 0.384 | 4406 | 2157 |
| S10 | sharer_trust | Trust: high | 0.515 | 0.509 | -0.006 | 0.005 | 0.187 | 5624 | 2821 |
| S10 | sharer_trust | Trust: low | 0.443 | 0.533 | 0.090 | 0.034 | 0.007 | 571 | 257 |
| S10 | sharer_trust | Trust: mid | 0.471 | 0.465 | -0.006 | 0.014 | 0.684 | 1786 | 901 |
| S10 | sharer_knowledge | Knowledge: high | 0.523 | 0.515 | -0.008 | 0.010 | 0.429 | 3404 | 1194 |
| S10 | sharer_knowledge | Knowledge: low | 0.472 | 0.508 | 0.036 | 0.015 | 0.016 | 1151 | 917 |
| S10 | sharer_knowledge | Knowledge: mid | 0.487 | 0.487 | 0.000565 | 0.008 | 0.943 | 3426 | 1866 |
| S10 | sharer_conspiracy | Conspiracy belief: high | 0.504 | 0.496 | -0.007 | 0.005 | 0.131 | 5696 | 3045 |
| S10 | sharer_conspiracy | Conspiracy belief: low | 0.491 | 0.512 | 0.021 | 0.015 | 0.145 | 2285 | 943 |

Spanish-language respondents rated misinformation 3.7 points more plausible than English-language ones (p = 0.008). They also rated low-trust sharers 9.0 points more plausible (p = 0.007) and low-knowledge sharers 3.6 points more plausible (p = 0.016). These are subgroup contrasts among many tests.

![Planned AMCEs](figures/registered_effects.png)

<!-- fd:section id=exploratory-authors -->
## Exploratory analyses specified by the authors

*Not pre-registered. The authors specified these analyses after seeing the data; they are run by the same deterministic scripts as the registered tests and should be read as hypothesis-generating.*

<!-- fd:hyp id=X1 tag=exploratory outcome=share -->
### X1. A1. Trust in the sharer → sharing

*A1. Source credibility is conditional on content uncertainty: the slope of sharing on trust in the sharer (1-5), net of the other source attributes, and how it differs by information type.*  
*Exploratory, not pre-registered.*

Slope of Chosen to share on `trust_raw`: 0.014 (SE 0.004, p < 0.001, N = 11882). Significant at alpha = 0.05: yes.

This is a post hoc analysis. Each extra point of trust in the sharer (on the 1–5 scale) was associated with 1.4 points more sharing (p < 0.001, two-sided).

#### Details: model and coefficients (X1)

```
share ~ treat + close_num + origin_num + C(sharer_ideology) + knowledge_raw + conspiracy_raw
OLS | cluster-robust SEs on resp_id | N = 11882 | two-sided test, alpha = 0.05
```

| analysis_id | term | estimate | std_error | statistic | p_value | conf_low | conf_high |
|---|---|---|---|---|---|---|---|
| X1 | Intercept | 0.401 | 0.020 | 19.867 | 7.84e-88 | 0.362 | 0.441 |
| X1 | C(sharer_ideology)[T.Liberal sharer] | 0.008 | 0.011 | 0.691 | 0.490 | -0.014 | 0.030 |
| X1 | C(sharer_ideology)[T.Moderate sharer] | -0.009 | 0.010 | -0.944 | 0.345 | -0.028 | 0.010 |
| X1 | treat | 0.014 | 0.004 | 3.807 | 0.00014 | 0.007 | 0.022 |
| X1 | close_num | 0.029 | 0.010 | 2.758 | 0.006 | 0.008 | 0.049 |
| X1 | origin_num | 0.002 | 0.008 | 0.273 | 0.785 | -0.014 | 0.018 |
| X1 | knowledge_raw | 0.008 | 0.004 | 2.081 | 0.037 | 0.00045 | 0.015 |
| X1 | conspiracy_raw | 0.005 | 0.014 | 0.378 | 0.706 | -0.022 | 0.033 |

<!-- fd:hyp id=X2 tag=exploratory outcome=plausibility -->
### X2. A1. Trust in the sharer → plausibility

*A1. The slope of plausibility on trust in the sharer, by information type.*  
*Exploratory, not pre-registered.*

Slope of Chosen as more plausible on `trust_raw`: 0.013 (SE 0.004, p < 0.001, N = 11884). Significant at alpha = 0.05: yes.

This is a post hoc analysis. Each extra point of trust was associated with 1.3 points higher plausibility (p < 0.001, two-sided).

#### Details: model and coefficients (X2)

```
plausibility ~ treat + close_num + origin_num + C(sharer_ideology) + knowledge_raw + conspiracy_raw
OLS | cluster-robust SEs on resp_id | N = 11884 | two-sided test, alpha = 0.05
```

| analysis_id | term | estimate | std_error | statistic | p_value | conf_low | conf_high |
|---|---|---|---|---|---|---|---|
| X2 | Intercept | 0.404 | 0.020 | 20.137 | 3.53e-90 | 0.365 | 0.443 |
| X2 | C(sharer_ideology)[T.Liberal sharer] | 0.019 | 0.012 | 1.633 | 0.103 | -0.004 | 0.042 |
| X2 | C(sharer_ideology)[T.Moderate sharer] | -0.001 | 0.010 | -0.104 | 0.918 | -0.020 | 0.018 |
| X2 | treat | 0.013 | 0.004 | 3.519 | 0.000433 | 0.006 | 0.020 |
| X2 | close_num | 0.026 | 0.010 | 2.474 | 0.013 | 0.005 | 0.047 |
| X2 | origin_num | -0.003 | 0.008 | -0.336 | 0.737 | -0.019 | 0.014 |
| X2 | knowledge_raw | 0.009 | 0.004 | 2.365 | 0.018 | 0.002 | 0.016 |
| X2 | conspiracy_raw | -0.005 | 0.014 | -0.362 | 0.717 | -0.033 | 0.023 |

<!-- fd:hyp id=X3 tag=exploratory outcome=share -->
### X3. A1. Close tie → sharing

*A1. The close-tie premium on sharing, net of the other source attributes, by information type.*  
*Exploratory, not pre-registered.*

Slope of Chosen to share on `close_num`: 0.029 (SE 0.010, p = 0.006, N = 11882). Significant at alpha = 0.05: yes.

This is a post hoc analysis. The close-tie premium on sharing was 2.9 points (p = 0.006, two-sided), consistent with the registered estimate.

#### Details: model and coefficients (X3)

```
share ~ treat + trust_raw + origin_num + C(sharer_ideology) + knowledge_raw + conspiracy_raw
OLS | cluster-robust SEs on resp_id | N = 11882 | two-sided test, alpha = 0.05
```

| analysis_id | term | estimate | std_error | statistic | p_value | conf_low | conf_high |
|---|---|---|---|---|---|---|---|
| X3 | Intercept | 0.401 | 0.020 | 19.867 | 7.84e-88 | 0.362 | 0.441 |
| X3 | C(sharer_ideology)[T.Liberal sharer] | 0.008 | 0.011 | 0.691 | 0.490 | -0.014 | 0.030 |
| X3 | C(sharer_ideology)[T.Moderate sharer] | -0.009 | 0.010 | -0.944 | 0.345 | -0.028 | 0.010 |
| X3 | treat | 0.029 | 0.010 | 2.758 | 0.006 | 0.008 | 0.049 |
| X3 | trust_raw | 0.014 | 0.004 | 3.807 | 0.00014 | 0.007 | 0.022 |
| X3 | origin_num | 0.002 | 0.008 | 0.273 | 0.785 | -0.014 | 0.018 |
| X3 | knowledge_raw | 0.008 | 0.004 | 2.081 | 0.037 | 0.00045 | 0.015 |
| X3 | conspiracy_raw | 0.005 | 0.014 | 0.378 | 0.706 | -0.022 | 0.033 |

<!-- fd:hyp id=X4 tag=exploratory outcome=share_not_believe -->
### X4. A2. Sharing without believing

*A2. Sharing without believing: among profiles chosen to share, the probability that the respondent judged the other post more plausible, by information type, net of source attributes, media trust and age.*  
*Exploratory, not pre-registered.*

Post hoc. Among profiles chosen for sharing, misinformation was 5.5 points more likely than true/neutral to be one the respondent judged less plausible than the other post (95% CI [3.0, 8.1], p < 0.001). Fact-checks were 1.7 points higher (95% CI [−0.5, 4.0]).

#### Details: model and estimates by arm (X4)

```
share_not_believe ~ C(arm_code, Treatment(reference='True/neutral')) + trust_raw + close_num + origin_num + C(sharer_ideology) + knowledge_raw + conspiracy_raw + media_trust + age
OLS | cluster-robust SEs on resp_id | N = 5938 | two-sided test, alpha = 0.05
```

| Level | Estimate | SE | p | 95% CI | n (level) | Supported |
|---|---|---|---|---|---|---|
| Misinformation | 0.055 | 0.013 | < 0.0001 | [0.030, 0.081] | 1605 | yes |
| Fact-check | 0.017 | 0.011 | 0.1300 | [-0.005, 0.040] | 1837 | no |

<!-- fd:hyp id=X5 tag=exploratory outcome=share -->
### X5. A3. Co-ideological sharer → sharing

*A3. Co-ideological messenger: sharing when the respondent and the sharer lean the same way (both liberal or both conservative) against opposite leans; pairs involving a moderate form a third group. Cell differences, no controls.*  
*Exploratory, not pre-registered.*

Post hoc. Sharing was 4.4 points higher when respondent and sharer leaned the same way than when they leaned opposite (95% CI [0.9, 7.9], p = 0.015). Pairs involving a moderate were not distinguishable from opposite leans (0.8 points).

#### Details: model and estimates by arm (X5)

```
share ~ C(arm_code, Treatment(reference='Incongruent'))
difference in means | cluster-robust SEs on resp_id | N = 9945 | two-sided test, alpha = 0.05
```

| Level | Estimate | SE | p | 95% CI | n (level) | Supported |
|---|---|---|---|---|---|---|
| Congruent | 0.044 | 0.018 | 0.0148 | [0.009, 0.079] | 2770 | yes |
| Neutral (a moderate) | 0.008 | 0.016 | 0.6191 | [-0.023, 0.039] | 6388 | no |

<!-- fd:hyp id=X6 tag=exploratory outcome=share -->
### X6. A4. Ego-network conspiracy load → sharing misinformation

*A4. Ego-network composition: the respondent's six named contacts as a measured network. Among misinformation profiles, sharing on the network's mean perceived belief in disputed claims, net of network ideological spread, mean trust, age and ideology. Each misinformation profile is weighted by 1 / the respondent's number of them, which reproduces the respondent-level regression of the misinformation-sharing rate.*  
*Exploratory, not pre-registered.*

Slope of Chosen to share on `net_consp`: 0.110 (SE 0.049, p = 0.026, N = 3196). Significant at alpha = 0.05: yes.

Post hoc. Among misinformation profiles, a higher network mean perceived belief in disputed claims was associated with more sharing (coefficient 0.110, p = 0.026, n = 3,196). This is a modest association, near the threshold.

#### Details: model and coefficients (X6)

```
share ~ treat + net_ideo_sd + net_trust + age + ideo5_self
OLS | weights = w_resp_misinfo | cluster-robust SEs on resp_id | N = 3196 | two-sided test, alpha = 0.05
```

| analysis_id | term | estimate | std_error | statistic | p_value | conf_low | conf_high |
|---|---|---|---|---|---|---|---|
| X6 | Intercept | 0.439 | 0.063 | 6.993 | 2.69e-12 | 0.316 | 0.562 |
| X6 | treat | 0.110 | 0.049 | 2.226 | 0.026 | 0.013 | 0.206 |
| X6 | net_ideo_sd | -0.017 | 0.025 | -0.660 | 0.509 | -0.066 | 0.033 |
| X6 | net_trust | 0.002 | 0.012 | 0.128 | 0.898 | -0.022 | 0.025 |
| X6 | age | -0.002 | 0.000607 | -3.485 | 0.000491 | -0.003 | -0.000926 |
| X6 | ideo5_self | 0.010 | 0.009 | 1.109 | 0.268 | -0.008 | 0.027 |

<!-- fd:hyp id=X7 tag=exploratory outcome=share -->
### X7. B1. Congenial content → sharing

*B1. Message x respondent congruence: among partisan respondents shown partisan-slanted headlines, sharing of congenial against uncongenial content (headline slant from the paper's preliminary automated coding), by information type.*  
*Exploratory, not pre-registered.*

Effect on Chosen to share: 0.025 (SE 0.019, p = 0.175); reference level mean 0.43, treated mean 0.46. Significant at alpha = 0.05: no.

Post hoc. Among partisan respondents, congenial slanted headlines were shared 2.5 points more than uncongenial ones, not distinguishable from zero (p = 0.18, n = 3,016).

#### Details: model and coefficients (X7)

```
share ~ treat
difference in means | cluster-robust SEs on resp_id | N = 3016 | two-sided test, alpha = 0.05
```

| analysis_id | term | estimate | std_error | statistic | p_value | conf_low | conf_high |
|---|---|---|---|---|---|---|---|
| X7 | Intercept | 0.435 | 0.011 | 39.713 | 0.000 | 0.413 | 0.456 |
| X7 | treat | 0.025 | 0.019 | 1.355 | 0.175 | -0.011 | 0.061 |

<!-- fd:hyp id=X8 tag=exploratory outcome=share -->
### X8. B2. Conspiracy-prone sharer → sharing

*B2. A conspiracy-prone source: the slope of sharing on the sharer's perceived belief in disputed claims (0-1), net of the other source attributes, by information type.*  
*Exploratory, not pre-registered.*

Slope of Chosen to share on `conspiracy_raw`: 0.005 (SE 0.014, p = 0.706, N = 11882). Significant at alpha = 0.05: no.

Post hoc. The slope of sharing on the sharer's perceived belief in disputed claims was not distinguishable from zero overall (0.005, p = 0.71).

#### Details: model and coefficients (X8)

```
share ~ treat + trust_raw + close_num + origin_num + C(sharer_ideology) + knowledge_raw
OLS | cluster-robust SEs on resp_id | N = 11882 | two-sided test, alpha = 0.05
```

| analysis_id | term | estimate | std_error | statistic | p_value | conf_low | conf_high |
|---|---|---|---|---|---|---|---|
| X8 | Intercept | 0.401 | 0.020 | 19.867 | 7.84e-88 | 0.362 | 0.441 |
| X8 | C(sharer_ideology)[T.Liberal sharer] | 0.008 | 0.011 | 0.691 | 0.490 | -0.014 | 0.030 |
| X8 | C(sharer_ideology)[T.Moderate sharer] | -0.009 | 0.010 | -0.944 | 0.345 | -0.028 | 0.010 |
| X8 | treat | 0.005 | 0.014 | 0.378 | 0.706 | -0.022 | 0.033 |
| X8 | trust_raw | 0.014 | 0.004 | 3.807 | 0.00014 | 0.007 | 0.022 |
| X8 | close_num | 0.029 | 0.010 | 2.758 | 0.006 | 0.008 | 0.049 |
| X8 | origin_num | 0.002 | 0.008 | 0.273 | 0.785 | -0.014 | 0.018 |
| X8 | knowledge_raw | 0.008 | 0.004 | 2.081 | 0.037 | 0.00045 | 0.015 |

<!-- fd:hyp id=X9 tag=exploratory outcome=plausibility -->
### X9. B2. Conspiracy-prone sharer → plausibility

*B2. The slope of plausibility on the sharer's perceived belief in disputed claims, by information type.*  
*Exploratory, not pre-registered.*

Slope of Chosen as more plausible on `conspiracy_raw`: -0.005 (SE 0.014, p = 0.717, N = 11884). Significant at alpha = 0.05: no.

Post hoc. The slope of plausibility on the sharer's perceived belief in disputed claims was not distinguishable from zero overall (−0.005, p = 0.72).

#### Details: model and coefficients (X9)

```
plausibility ~ treat + trust_raw + close_num + origin_num + C(sharer_ideology) + knowledge_raw
OLS | cluster-robust SEs on resp_id | N = 11884 | two-sided test, alpha = 0.05
```

| analysis_id | term | estimate | std_error | statistic | p_value | conf_low | conf_high |
|---|---|---|---|---|---|---|---|
| X9 | Intercept | 0.404 | 0.020 | 20.137 | 3.53e-90 | 0.365 | 0.443 |
| X9 | C(sharer_ideology)[T.Liberal sharer] | 0.019 | 0.012 | 1.633 | 0.103 | -0.004 | 0.042 |
| X9 | C(sharer_ideology)[T.Moderate sharer] | -0.001 | 0.010 | -0.104 | 0.918 | -0.020 | 0.018 |
| X9 | treat | -0.005 | 0.014 | -0.362 | 0.717 | -0.033 | 0.023 |
| X9 | trust_raw | 0.013 | 0.004 | 3.519 | 0.000433 | 0.006 | 0.020 |
| X9 | close_num | 0.026 | 0.010 | 2.474 | 0.013 | 0.005 | 0.047 |
| X9 | origin_num | -0.003 | 0.008 | -0.336 | 0.737 | -0.019 | 0.014 |
| X9 | knowledge_raw | 0.009 | 0.004 | 2.365 | 0.018 | 0.002 | 0.016 |

<!-- fd:hyp id=X10 tag=exploratory outcome=plausibility -->
### X10. B2. Sharer believes the vaccine claim → plausibility of anti-vaccine misinformation

*B2, claim-specific (thin): for the anti-vaccine (polio) misinformation headline, plausibility when the sharer is seen as believing 'Covid-19 vaccines modify your DNA' against not.*  
*Exploratory, not pre-registered.*

Effect on Chosen as more plausible: 0.165 (SE 0.067, p = 0.013); reference level mean 0.29, treated mean 0.45. Significant at alpha = 0.05: yes.

Post hoc and thin (n = 266). The anti-vaccine misinformation headline was rated 16.5 points more plausible when the sharer was seen as believing the DNA claim (p = 0.013). Treat with caution.

#### Details: model and coefficients (X10)

```
plausibility ~ treat
difference in means | cluster-robust SEs on resp_id | N = 266 | two-sided test, alpha = 0.05
```

| analysis_id | term | estimate | std_error | statistic | p_value | conf_low | conf_high |
|---|---|---|---|---|---|---|---|
| X10 | Intercept | 0.288 | 0.029 | 9.976 | 1.94e-23 | 0.231 | 0.345 |
| X10 | treat | 0.165 | 0.067 | 2.481 | 0.013 | 0.035 | 0.296 |

<!-- fd:hyp id=X11 tag=exploratory outcome=share -->
### X11. B3. Trust → sharing misinformation, health vs. political

*B3. Health vs. political misinformation: among misinformation profiles, the trust slope on sharing for health (guanabana, polio) and political headlines.*  
*Exploratory, not pre-registered.*

Slope of Chosen to share on `trust_raw`: 0.019 (SE 0.008, p = 0.013, N = 3822). Significant at alpha = 0.05: yes.

Post hoc. The trust slope on sharing misinformation was 1.9 points per trust point across headlines (p = 0.013), a small association.

#### Details: model and coefficients (X11)

```
share ~ treat + close_num + origin_num + C(sharer_ideology) + knowledge_raw + conspiracy_raw
OLS | cluster-robust SEs on resp_id | N = 3822 | two-sided test, alpha = 0.05
```

| analysis_id | term | estimate | std_error | statistic | p_value | conf_low | conf_high |
|---|---|---|---|---|---|---|---|
| X11 | Intercept | 0.259 | 0.041 | 6.253 | 4.04e-10 | 0.178 | 0.340 |
| X11 | C(sharer_ideology)[T.Liberal sharer] | 0.019 | 0.022 | 0.854 | 0.393 | -0.025 | 0.063 |
| X11 | C(sharer_ideology)[T.Moderate sharer] | -0.007 | 0.019 | -0.339 | 0.735 | -0.045 | 0.031 |
| X11 | treat | 0.019 | 0.008 | 2.476 | 0.013 | 0.004 | 0.034 |
| X11 | close_num | 0.035 | 0.017 | 2.049 | 0.040 | 0.002 | 0.068 |
| X11 | origin_num | -0.011 | 0.018 | -0.640 | 0.522 | -0.046 | 0.023 |
| X11 | knowledge_raw | 0.014 | 0.008 | 1.738 | 0.082 | -0.002 | 0.031 |
| X11 | conspiracy_raw | 0.086 | 0.028 | 3.090 | 0.002 | 0.032 | 0.141 |

<!-- fd:hyp id=X12 tag=exploratory outcome=share -->
### X12. B3. Close tie → sharing misinformation, health vs. political

*B3. Among misinformation profiles, the close-tie premium for health and political headlines.*  
*Exploratory, not pre-registered.*

Slope of Chosen to share on `close_num`: 0.035 (SE 0.017, p = 0.040, N = 3822). Significant at alpha = 0.05: yes.

Post hoc. The close-tie premium on sharing misinformation was 3.5 points (p = 0.040), near the threshold.

#### Details: model and coefficients (X12)

```
share ~ treat + trust_raw + origin_num + C(sharer_ideology) + knowledge_raw + conspiracy_raw
OLS | cluster-robust SEs on resp_id | N = 3822 | two-sided test, alpha = 0.05
```

| analysis_id | term | estimate | std_error | statistic | p_value | conf_low | conf_high |
|---|---|---|---|---|---|---|---|
| X12 | Intercept | 0.259 | 0.041 | 6.253 | 4.04e-10 | 0.178 | 0.340 |
| X12 | C(sharer_ideology)[T.Liberal sharer] | 0.019 | 0.022 | 0.854 | 0.393 | -0.025 | 0.063 |
| X12 | C(sharer_ideology)[T.Moderate sharer] | -0.007 | 0.019 | -0.339 | 0.735 | -0.045 | 0.031 |
| X12 | treat | 0.035 | 0.017 | 2.049 | 0.040 | 0.002 | 0.068 |
| X12 | trust_raw | 0.019 | 0.008 | 2.476 | 0.013 | 0.004 | 0.034 |
| X12 | origin_num | -0.011 | 0.018 | -0.640 | 0.522 | -0.046 | 0.023 |
| X12 | knowledge_raw | 0.014 | 0.008 | 1.738 | 0.082 | -0.002 | 0.031 |
| X12 | conspiracy_raw | 0.086 | 0.028 | 3.090 | 0.002 | 0.032 | 0.141 |

<!-- fd:hyp id=X13 tag=exploratory outcome=share -->
### X13. B4. Sharer origin → sharing, by language and nativity

*B4. Sharer origin (continental US vs. elsewhere) and sharing, by survey language and by the respondent's nativity.*  
*Exploratory, not pre-registered.*

Slope of Chosen to share on `origin_num`: 0.002 (SE 0.008, p = 0.785, N = 11882). Significant at alpha = 0.05: no.

Post hoc. Sharer origin was not distinguishable from zero in the pooled slope (0.002, p = 0.78), matching H3.

#### Details: model and coefficients (X13)

```
share ~ treat + trust_raw + close_num + C(sharer_ideology) + knowledge_raw + conspiracy_raw
OLS | cluster-robust SEs on resp_id | N = 11882 | two-sided test, alpha = 0.05
```

| analysis_id | term | estimate | std_error | statistic | p_value | conf_low | conf_high |
|---|---|---|---|---|---|---|---|
| X13 | Intercept | 0.401 | 0.020 | 19.867 | 7.84e-88 | 0.362 | 0.441 |
| X13 | C(sharer_ideology)[T.Liberal sharer] | 0.008 | 0.011 | 0.691 | 0.490 | -0.014 | 0.030 |
| X13 | C(sharer_ideology)[T.Moderate sharer] | -0.009 | 0.010 | -0.944 | 0.345 | -0.028 | 0.010 |
| X13 | treat | 0.002 | 0.008 | 0.273 | 0.785 | -0.014 | 0.018 |
| X13 | trust_raw | 0.014 | 0.004 | 3.807 | 0.00014 | 0.007 | 0.022 |
| X13 | close_num | 0.029 | 0.010 | 2.758 | 0.006 | 0.008 | 0.049 |
| X13 | knowledge_raw | 0.008 | 0.004 | 2.081 | 0.037 | 0.00045 | 0.015 |
| X13 | conspiracy_raw | 0.005 | 0.014 | 0.378 | 0.706 | -0.022 | 0.033 |

<!-- fd:group id=heterogeneity -->
### Heterogeneity

<!-- fd:hyp id=XS1 tag=exploratory kind=subgroup -->
#### XS1. Trust slope on sharing within each information type, and its interaction with information type

*Moderator `infotype`. Exploratory, not pre-registered.*

| analysis_id | level | estimate | std_error | p_value | n |
|---|---|---|---|---|---|
| XS1 | Fact-check | 0.017 | 0.008 | 0.035 | 3915 |
| XS1 | Misinformation | 0.019 | 0.008 | 0.013 | 3822 |
| XS1 | True/neutral | 0.006 | 0.008 | 0.456 | 4145 |

Interaction `trust_raw x Misinformation (vs Fact-check)`: 0.003 (SE 0.011, p = 0.761).

Interaction `trust_raw x True/neutral (vs Fact-check)`: -0.015 (SE 0.011, p = 0.179).

Post hoc. The trust slope on sharing was 1.7 points for fact-checks, 1.9 for misinformation and 0.6 for true/neutral headlines. The differences between slopes were not distinguishable from zero.

<!-- fd:hyp id=XS2 tag=exploratory kind=subgroup -->
#### XS2. Trust slope on plausibility within each information type

*Moderator `infotype`. Exploratory, not pre-registered.*

| analysis_id | level | estimate | std_error | p_value | n |
|---|---|---|---|---|---|
| XS2 | Fact-check | 0.018 | 0.008 | 0.023 | 3918 |
| XS2 | Misinformation | 0.021 | 0.008 | 0.009 | 3821 |
| XS2 | True/neutral | -0.000371 | 0.008 | 0.962 | 4145 |

Interaction `trust_raw x Misinformation (vs Fact-check)`: 0.008 (SE 0.011, p = 0.469).

Interaction `trust_raw x True/neutral (vs Fact-check)`: -0.021 (SE 0.011, p = 0.065).

Post hoc. The trust slope on plausibility was about 1.8 points for fact-checks and 2.1 for misinformation, and about zero for true/neutral headlines. Differences between slopes were not clearly distinguishable.

<!-- fd:hyp id=XS3 tag=exploratory kind=subgroup -->
#### XS3. Close-tie premium on sharing within each information type

*Moderator `infotype`. Exploratory, not pre-registered.*

| analysis_id | level | estimate | std_error | p_value | n |
|---|---|---|---|---|---|
| XS3 | Fact-check | 0.047 | 0.017 | 0.005 | 3915 |
| XS3 | Misinformation | 0.035 | 0.017 | 0.040 | 3822 |
| XS3 | True/neutral | 0.009 | 0.016 | 0.591 | 4145 |

Interaction `close_num x Misinformation (vs Fact-check)`: -0.007 (SE 0.023, p = 0.755).

Interaction `close_num x True/neutral (vs Fact-check)`: -0.044 (SE 0.023, p = 0.050).

Post hoc. The close-tie premium was 4.7 points for fact-checks, 3.5 for misinformation and 0.9 for true/neutral headlines. The gap between true/neutral and fact-checks was borderline (p = 0.050).

<!-- fd:hyp id=XS5 tag=exploratory kind=subgroup -->
#### XS5. Congruent minus incongruent sharing gap within each information type

*Moderator `infotype`. Exploratory, not pre-registered.*

| analysis_id | level | arm | estimate | std_error | p_value | conf_low | conf_high | n |
|---|---|---|---|---|---|---|---|---|
| XS5 | Fact-check | Congruent | 0.038 | 0.035 | 0.278 | -0.031 | 0.107 | 3292 |
| XS5 | Fact-check | Neutral (a moderate) | -0.010 | 0.033 | 0.754 | -0.074 | 0.054 | 3292 |
| XS5 | Misinformation | Congruent | 0.039 | 0.034 | 0.251 | -0.028 | 0.107 | 3197 |
| XS5 | Misinformation | Neutral (a moderate) | -0.014 | 0.032 | 0.654 | -0.077 | 0.048 | 3197 |
| XS5 | True/neutral | Congruent | 0.056 | 0.034 | 0.102 | -0.011 | 0.122 | 3456 |
| XS5 | True/neutral | Neutral (a moderate) | 0.040 | 0.032 | 0.209 | -0.022 | 0.101 | 3456 |

Interaction `Congruent x Misinformation (vs Fact-check)`: 0.001 (SE 0.051, p = 0.980).

Interaction `Neutral (a moderate) x Misinformation (vs Fact-check)`: -0.004 (SE 0.049, p = 0.933).

Interaction `Congruent x True/neutral (vs Fact-check)`: 0.018 (SE 0.052, p = 0.735).

Interaction `Neutral (a moderate) x True/neutral (vs Fact-check)`: 0.050 (SE 0.049, p = 0.307).

Post hoc. The congruent-versus-opposite sharing gap was between 3.8 and 5.6 points within each information type, with intervals including zero. The differences between types were not distinguishable from zero.

<!-- fd:hyp id=XS7 tag=exploratory kind=subgroup -->
#### XS7. Congenial minus uncongenial sharing premium within misinformation and within fact-checks

*Moderator `infotype`. Exploratory, not pre-registered.*

| analysis_id | level | estimate | std_error | p_value | n |
|---|---|---|---|---|---|
| XS7 | Fact-check | -0.002 | 0.021 | 0.927 | 1527 |
| XS7 | Misinformation | 0.054 | 0.022 | 0.012 | 1489 |

Interaction `msg_congenial x Misinformation (vs Fact-check)`: 0.056 (SE 0.021, p = 0.007).

Post hoc. Congenial misinformation was shared 5.4 points more than uncongenial misinformation (p = 0.012), but there was no such gap for fact-checks (−0.2 points). The difference between the two was 5.6 points (p = 0.007).

<!-- fd:hyp id=XS8 tag=exploratory kind=subgroup -->
#### XS8. Conspiracy-prone-source slope on sharing within each information type

*Moderator `infotype`. Exploratory, not pre-registered.*

| analysis_id | level | estimate | std_error | p_value | n |
|---|---|---|---|---|---|
| XS8 | Fact-check | -0.044 | 0.028 | 0.115 | 3915 |
| XS8 | Misinformation | 0.086 | 0.028 | 0.002 | 3822 |
| XS8 | True/neutral | -0.022 | 0.027 | 0.420 | 4145 |

Interaction `conspiracy_raw x Misinformation (vs Fact-check)`: 0.131 (SE 0.041, p = 0.001).

Interaction `conspiracy_raw x True/neutral (vs Fact-check)`: 0.020 (SE 0.041, p = 0.627).

Post hoc. For misinformation, sharing rose with the sharer's perceived belief in disputed claims (slope 0.086, p = 0.002), while slopes for fact-checks and true/neutral headlines were not distinguishable from zero. The difference from fact-checks was 0.131 (p = 0.001).

<!-- fd:hyp id=XS9 tag=exploratory kind=subgroup -->
#### XS9. Conspiracy-prone-source slope on plausibility within each information type

*Moderator `infotype`. Exploratory, not pre-registered.*

| analysis_id | level | estimate | std_error | p_value | n |
|---|---|---|---|---|---|
| XS9 | Fact-check | -0.050 | 0.029 | 0.086 | 3918 |
| XS9 | Misinformation | 0.095 | 0.028 | 0.000663 | 3821 |
| XS9 | True/neutral | -0.055 | 0.028 | 0.046 | 4145 |

Interaction `conspiracy_raw x Misinformation (vs Fact-check)`: 0.146 (SE 0.042, p < 0.001).

Interaction `conspiracy_raw x True/neutral (vs Fact-check)`: -0.003 (SE 0.043, p = 0.942).

Post hoc. Plausibility of misinformation rose with the sharer's perceived conspiracy belief (slope 0.095, p < 0.001), but fell slightly for true/neutral headlines (−0.055, p = 0.046). The difference from fact-checks was 0.146 for misinformation (p < 0.001).

<!-- fd:hyp id=XS11 tag=exploratory kind=subgroup -->
#### XS11. Trust slope on sharing misinformation: health vs. political headlines

*Moderator `topic_type`. Exploratory, not pre-registered.*

| analysis_id | level | estimate | std_error | p_value | n |
|---|---|---|---|---|---|
| XS11 | Health | 0.025 | 0.020 | 0.217 | 550 |
| XS11 | Political | 0.019 | 0.008 | 0.024 | 3272 |

Interaction `trust_raw x Political (vs Health)`: 0.007 (SE 0.019, p = 0.717).

Post hoc. The trust slope on sharing misinformation was 2.5 points for health and 1.9 for political headlines. The difference was not distinguishable from zero, and the health group was small (n = 550).

<!-- fd:hyp id=XS12 tag=exploratory kind=subgroup -->
#### XS12. Close-tie premium on sharing misinformation: health vs. political headlines

*Moderator `topic_type`. Exploratory, not pre-registered.*

| analysis_id | level | estimate | std_error | p_value | n |
|---|---|---|---|---|---|
| XS12 | Health | 0.007 | 0.044 | 0.879 | 550 |
| XS12 | Political | 0.039 | 0.018 | 0.031 | 3272 |

Interaction `close_num x Political (vs Health)`: 0.035 (SE 0.046, p = 0.439).

Post hoc. The close-tie premium on misinformation was 0.7 points for health and 3.9 for political headlines. The difference was not distinguishable from zero, and the health group was small.

<!-- fd:hyp id=XS13a tag=exploratory kind=subgroup -->
#### XS13a. Sharer-origin slope on sharing by survey language

*Moderator `survey_language`. Exploratory, not pre-registered.*

| analysis_id | level | estimate | std_error | p_value | n |
|---|---|---|---|---|---|
| XS13a | English | 0.004 | 0.010 | 0.675 | 7975 |
| XS13a | Spanish | 0.000427 | 0.014 | 0.975 | 3907 |

Interaction `origin_num x Spanish (vs English)`: -0.005 (SE 0.017, p = 0.752).

Post hoc. The sharer-origin slope was near zero in both English (0.004) and Spanish (0.000), and the difference was not distinguishable from zero.

<!-- fd:hyp id=XS13b tag=exploratory kind=subgroup -->
#### XS13b. Sharer-origin slope on sharing by respondent nativity

*Moderator `resp_nativity`. Exploratory, not pre-registered.*

| analysis_id | level | estimate | std_error | p_value | n |
|---|---|---|---|---|---|
| XS13b | Foreign-born | 0.013 | 0.012 | 0.300 | 4927 |
| XS13b | US-born | -0.008 | 0.011 | 0.447 | 6947 |

Interaction `origin_num x US-born (vs Foreign-born)`: -0.018 (SE 0.016, p = 0.266).

Post hoc. The sharer-origin slope was 1.3 points among foreign-born and −0.8 points among US-born respondents. Neither was distinguishable from zero, nor was the difference.

<!-- fd:section id=exploratory -->
## Further exploratory analyses (proposed by the pipeline)

*Everything in this section is exploratory and was not pre-registered.*

_None produced._

<!-- fd:section id=related -->
## Related work

The retrieved list is thin and mostly off-topic, so it says little directly about the hypotheses on source cues (tie strength, origin, ideology, trust, knowledge, conspiracy belief) and information type in sharing and plausibility. The closest items are general. Lewandowsky et al. (2017) discuss how misinformation spreads and influences people, and Roozenbeek et al. (2020) report predictors of belief in COVID-19 misinformation across countries, including links to health behaviours. Neither tests how sharer attributes shape sharing or plausibility, so neither bears on the AMCE estimates for H1-H14 or the weighted robustness checks R1-R12. Van Bavel et al. (2020) is a broad pandemic-response review with no abstract available. Three retrieved works are unrelated to the hypotheses: Dwivedi et al. (2019) on AI, Jenkins and Purushotma (2006) on media education, and Kniffin et al. (2020) on workplaces. The EMNLP 2021 proceedings entry (2021) is also unrelated. The works tagged as method concern attitudes toward the unvaccinated (Bor et al., 2022), election-lie acceptance (Arceneaux & Truex, 2022), and a vaccine-hesitancy survey with embedded conjoint experiments (Stamm et al., 2022). Only the last is a design precedent, as another conjoint on a health topic, and its abstract snippet reports no findings relevant here.

The retrieved works do not clearly disagree with each other or with the study's expectations, because none reports findings on the specific source-cue effects. The one tension is loose. Lewandowsky et al. (2017) frame misinformation as a broad societal problem, while Roozenbeek et al. (2020) locate susceptibility in individual and country-level predictors. Neither speaks to whether sharing depends on who shares, or to sharing without believing (X4). The study's conjoint design, which randomizes source attributes and measures both sharing and plausibility, can speak to that question directly, but the retrieved literature offers no benchmark against which to compare the estimates.

Retrieved works (OpenAlex; queries: source trust tie strength misinformation sharing social media; sharer credibility and close ties increase sharing and belief of false news; accuracy nudge sharing without believing partisan identity motivated sharing misinformation; content over source effects news sharing source cues weak effect misinformation; conjoint experiment AMCE social media sharing misinformation respondent-clustered):

- Jay Joseph Van Bavel, Katherine Baicker, Paulo S. Boggio, Valerio Capraro (2020). Using social and behavioural science to support COVID-19 pandemic response. Nature Human Behaviour. https://doi.org/10.1038/s41562-020-0884-z
- Yogesh Kumar Dwivedi, Laurie Hughes, Elvira Ismagilova, Gert Aarts (2019). Artificial Intelligence (AI): Multidisciplinary perspectives on emerging challenges, opportunities, and agenda for research, practice and policy. International Journal of Information Management. https://doi.org/10.1016/j.ijinfomgt.2019.08.002
- Henry Jenkins, Ravi Purushotma (2006). Confronting the Challenges of Participatory Culture: Media Education for the 21st Century. BiblioBoard Library Catalog (Open Research Library). https://openalex.org/W2112957339
- Stephan Lewandowsky, Ullrich K. H. Ecker, John Cook (2017). Beyond misinformation: Understanding and coping with the “post-truth” era.. Journal of Applied Research in Memory and Cognition. https://doi.org/10.1016/j.jarmac.2017.07.008
-  (2021). Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing. . https://doi.org/10.18653/v1/2021.emnlp-main
- Alexander Bor, Frederik Juhl Jørgensen, Michael Bang Petersen (2022). Discriminatory attitudes against unvaccinated people during the pandemic. Nature. https://doi.org/10.1038/s41586-022-05607-y
- Kevin Arceneaux, Rory Truex (2022). Donald Trump and the Lie. Perspectives on Politics. https://doi.org/10.1017/s1537592722000901
- Tanja Stamm, Julia Partheymüller, Erika Mosor, Valentin Ritschl (2022). Coronavirus vaccine hesitancy among unvaccinated Austrians: Assessing underlying motivations and the effectiveness of interventions based on a cross-sectional survey with two embedded conjoint experiments. The Lancet Regional Health - Europe. https://doi.org/10.1016/j.lanepe.2022.100389
- Kevin M. Kniffin, Jayanth Narayanan, Frederik Anseel, John Antonakis (2020). COVID-19 and the workplace: Implications, issues, and insights for future research and action.. American Psychologist. https://doi.org/10.1037/amp0000716
- Jon Roozenbeek, Claudia R. Schneider, Sarah Dryhurst, John Richard Kerr (2020). Susceptibility to misinformation about COVID-19 around the world. Royal Society Open Science. https://doi.org/10.1098/rsos.201199

<!-- fd:section id=limitations -->
## Limitations

Many tests were run without correction for multiplicity, so the smaller effects (moderate sharer, close tie on plausibility, several subgroup contrasts) may be chance findings. Only headline type was randomized. Tie strength, origin, ideology, trust, knowledge and conspiracy belief are respondents' ratings of real contacts, so those AMCEs bundle correlated attributes and are not causal. Non-significant results are inconclusive, not evidence of no effect. Health-topic and other subgroups are small. The exploratory X and XS analyses were specified after seeing the data and should be read as hypothesis-generating.

<!-- fd:section id=review round=1 -->
## Review

*Light Pass review: referee `anthropic/claude-sonnet-5.5`, checking agent `anthropic/claude-sonnet-5.5`. The Light Pass does two things: it checks every reported estimate against the result tables, and every analysis against the pre-analysis plan. It does not judge the design, methods or interpretation; see the other review options. The agent applied the corrections below itself; no person reviewed or revised this report. Registered analyses are never changed.*

**Outcome.** 12 of 12 checked claims supported after the agent's corrections; 26 of 26 registered analyses run as planned; 5 reworded; 3 text fixes; 1 correction pass.

#### Corrections

- **Corrected** · 8 items reworded or fixed in the text: H8, Abstract (2), Abstract / Design, Design, R1, H8, R2, Design and data, R3, Abstract / Design. Before and after are in the log below.

#### Details: full review log

Models: referee `anthropic/claude-sonnet-5.5`, checking agent `anthropic/claude-sonnet-5.5`.

**Assessment.** The registered randomized contrasts are well supported: misinformation lowers sharing by 18.2 points and fact-checks by 13.3, and plausibility shows a similar pattern. The close-tie and high-trust results match the tables but are descriptive contrasts on measured attributes. The report has several wording and count slips: a garbled H8 sentence, an unsupported eligible-profile count, and a claim of no dropped data that conflicts with the model Ns. The Abstract's framing of the source attributes and the subgroup claims is also loose. The most important caveat is that the source attributes are not randomized and many tests were run without correction.

| Registered analysis | Against the plan | Differences | Stated reason |
|---|---|---|---|
| H1 | as planned | — | — |
| H2 | as planned | — | — |
| H3 | as planned | — | — |
| H4 | as planned | — | — |
| H5 | as planned | — | — |
| H6 | as planned | — | — |
| H7 | as planned | — | — |
| H8 | as planned | — | — |
| H9 | as planned | — | — |
| H10 | as planned | — | — |
| H11 | as planned | — | — |
| H12 | as planned | — | — |
| H13 | as planned | — | — |
| H14 | as planned | — | — |
| R1 | as planned | — | — |
| R2 | as planned | — | — |
| R3 | as planned | — | — |
| R4 | as planned | — | — |
| R5 | as planned | — | — |
| R6 | as planned | — | — |
| R7 | as planned | — | — |
| R8 | as planned | — | — |
| R9 | as planned | — | — |
| R10 | as planned | — | — |
| R11 | as planned | — | — |
| R12 | as planned | — | — |

| Issue | Severity | Kind | Source | Outcome | What the referee said |
|---|---|---|---|---|---|
| K4 | high | presentational | claims | Fixed in text | Abstract / Design: Unsupported claim: "none dropped for missing values on the main outcomes; 12,000 analysed". The model tables use N=11882 (share) and N=11884 (plausibility). *claim checked against the tables by the checking agent* |
| K5 | high | presentational | claims | Fixed in text | Design: Unsupported claim: "3,854 misinformation and 3,972 fact-check profiles were eligible". H1 table n(level) is 3822 and 3915; no table gives 3854 or 3972. *claim checked against the tables by the checking agent* |
| R1 | high | presentational | light | Fixed in text | H8: The text says misinformation 'was rated more plausible 18.6 points less often'. This is contradictory, and the table estimate is -0.186, meaning less plausible. *The H8 sentence is garbled; the estimate itself is correct.* |
| K1 | medium | presentational | claims | Fixed in text | H8: Overstated claim: "Misinformation was rated more plausible 18.6 points less often than true or neutral headlines". H8: -0.186, CI [-0.208, -0.164]. The number and sign are right but the wording contradicts itself. *claim checked against the tables by the checking agent* |
| K2 | medium | presentational | claims | Fixed in text | Abstract: Overstated claim: "close ties (+3.0 points, 95% CI [1.0, 5.0]) raised sharing". H2: 0.030, CI [0.010, 0.050], p=0.003. Tie strength is measured, not randomized, so 'raised' implies a causal effect. *claim checked against the tables by the checking agent* |
| K3 | medium | presentational | claims | Fixed in text | Abstract: Overstated claim: "high trust in the sharer (+5.7 points, 95% CI [2.3, 9.1]) raised sharing". H5: Trust: high 0.057, CI [0.023, 0.091], p=0.001. Trust is measured, not randomized. *claim checked against the tables by the checking agent* |
| R2 | medium | presentational | light | Fixed in text | Design and data: H1 text reports chosen shares of 60.3% / 42.1% / 47.0%. The registered summary gives mean_treated of 0.421 for misinformation and 0.470 for fact-check, which match. The wording 'chosen shares' is fine, but the H1 design note says 3,854 misinformation and 3,972 fact-check profiles were eligible, while the table n(level) is 3,822 and 3,915 (analysed N=11,882). No table supports… *The eligible counts do not match the table n values and need correcting or sourcing.* |
| R3 | medium | presentational | light | Fixed in text | Abstract / Design: The text says 12,000 profile ratings were analysed and none were dropped. The model tables use N = 11,882 (share) and 11,884 (plausibility). *The prose needs to report the model Ns of 11,882 and 11,884 instead of claiming 12,000 analysed.* |
| R4 | low | presentational | light | Fixed in text | Re-weighted AMCEs: The text says close ties still raised plausibility by 2.7 points, and the table shows 0.027. That matches. The text says the moderate-sharer effect on sharing 'weakened to -1.7 (95% CI [-3.5, 0.0])', and the table shows p = 0.056. The text does not state that the effect is no longer significant. *The prose needs to state that the weighted estimate is not significant (p=0.056).* |
| R5 | low | presentational | light | Fixed in text | S5: The text says Spanish respondents shared 'more from low-trust sharers (+7.9 points)'. The table shows a difference of 0.079, which matches, but based on n=257 Spanish and 571 English profiles, so the comparison is thin. *This only needs a note on the small cell sizes (n=257 and 571); no re-estimation is required.* |

| Claim | Where | Verdict | Evidence | After corrections |
|---|---|---|---|---|
| Misinformation was chosen for sharing 18.2 points less often than true or neutral headlines (95% CI [−20.4, −16.0]) | Abstract | supported | H1 table: Misinformation -0.182, CI [-0.204, -0.160], N=11882. | supported: Misinformation was chosen for sharing 18.2 points less often than true or neutral headlines (95% CI [−20.4, −16.0]) |
| fact-checks 13.3 points less often (95% CI [−15.6, −11.1]) | Abstract | supported | H1 table: Fact-check -0.133, CI [-0.156, -0.111]. | supported: fact-checks 13.3 points less often (95% CI [−15.6, −11.1]) |
| Misinformation was rated more plausible 18.6 points less often than true or neutral headlines | H8 | overstated | H8: -0.186, CI [-0.208, -0.164]. The number and sign are right but the wording contradicts itself. | supported: Misinformation was rated 18.6 points less plausible than true or neutral headlines (95% CI [−20.8, −16.4]) |
| close ties (+3.0 points, 95% CI [1.0, 5.0]) raised sharing | Abstract | overstated | H2: 0.030, CI [0.010, 0.050], p=0.003. Tie strength is measured, not randomized, so 'raised' implies a causal effect. | supported: close ties (+3.0 points, 95% CI [1.0, 5.0]) ... were associated with more sharing |
| high trust in the sharer (+5.7 points, 95% CI [2.3, 9.1]) raised sharing | Abstract | overstated | H5: Trust: high 0.057, CI [0.023, 0.091], p=0.001. Trust is measured, not randomized. | supported: high trust in the sharer relative to low trust (+5.7 points, 95% CI [2.3, 9.1]) were associated with more sharing |
| origin, knowledge and conspiracy belief were not distinguishable from zero | Abstract | supported | H3 p=0.814; H6 p=0.962 and 0.127; H7 p=0.866. | supported: origin, knowledge and conspiracy belief were not distinguishable from zero |
| Respondents with greater belief in disputed claims shared misinformation 5.6 points more (p < 0.001) | Key findings | supported | S3 Misinformation difference 0.056, p=0.000766. This is a descriptive subgroup contrast with no multiplicity correction. | supported: respondents with higher belief in disputed claims shared misinformation 5.6 points more than those with lower belief (p < 0.001), and true/neutral content less |
| Plausibility ratings tracked sharing closely | Key findings | supported | H8 -0.186 and -0.124 versus H1 -0.182 and -0.133. | supported: Plausibility ratings tracked sharing closely |
| Moderate sharer effect on sharing weakened to −1.7 points (95% CI [−3.5, 0.0]) | Re-weighted AMCEs | supported | RW table: -0.017, CI [-0.035, 0.000], p=0.056. It is no longer significant at 0.05, and the text does not say so. | supported: weighted moderate-sharer contrast on sharing was −1.7 points (95% CI [−3.5, 0.0]) and is not significant at 0.05 (p = 0.056) |
| none dropped for missing values on the main outcomes; 12,000 analysed | Abstract / Design | unsupported | The model tables use N=11882 (share) and N=11884 (plausibility). | supported: models use 11,882 for sharing and 11,884 for plausibility |
| 3,854 misinformation and 3,972 fact-check profiles were eligible | Design | unsupported | H1 table n(level) is 3822 and 3915; no table gives 3854 or 3972. | supported: 3,822 misinformation and 3,915 fact-check profiles in the sharing model |

Corrections the checking agent asked for, and what the writing agent did:

- G1. Fix the H8 wording. Done: H8 wording fixed.
- G2. Report the model Ns of 11,882 (share) and 11,884 (plausibility). Done: Model Ns of 11,882 and 11,884 reported in abstract and design notes.
- G3. Correct the eligible profile counts in the Design section. Done: Counts in design notes corrected to 3,822 and 3,915.
- G4. Describe the tie, trust and other source-attribute contrasts as associations, not effects that 'raised' sharing. Done: Tie, trust and other source-attribute contrasts in takeaways, abstract and H5, H9, RW described as associations.
- G5. State that the weighted moderate-sharer effect on sharing is not significant. Done: Non-significance of weighted moderate-sharer effect on sharing stated in RW.

Re-check of the corrected text: All previously flagged wording has been corrected and the numbers match the tables; no further rewording needed.

#### Other review options

- **Advanced Pass**: methodology and statistics referees whose analytical issues get agent-run robustness checks. `--review light,advanced`
- **Coarse**: the open-source coarse-ink reviewer, run locally (about $1-2). `--review light,coarse`
- **Refine**: upload the report to refine.ink, then import its review. `filedrawer review-import . refine FILE`
- **OpenReview**: import any referee report, e.g. one posted on an OpenReview submission. `filedrawer review-import . openreview FILE`


<!-- fd:section id=potential -->
## Research potential

*The agent's assessment of what this study can still become. The proposed extensions below are built from it.*

**What stands.** Randomized information type with a registered plan produced a clean causal result: misinformation −18.2 points (95% CI [−20.4, −16.0]) and fact-checks −13.3 points on sharing, against a 0.031 MDE. Source attributes (tie, trust, ideology, knowledge) were taken from respondents' real contacts, which gives an ego-network setting. The report labels them honestly as measured associations, not causal effects. The inverse-probability re-weighting (R1–R12) left the estimates essentially unchanged: close tie 0.030, high trust 0.067. The weighted moderate-sharer contrast was correctly flagged as non-significant (p = 0.056). Sharing and plausibility were measured for every profile and gave near-identical patterns (H1 vs H8). The registered subgroup on belief in disputed claims (S3, S8) shows a coherent respondent-level moderation.

**Verdict.** A follow-up is worth running, but the headline-type effect is already settled and adds nothing new. The retrieved literature shows no genuine debate this study bears on. Run the advance_design brief first: randomizing tie and trust with a behavioural share is the only way to turn the study's most interesting claims (close ties and high trust) into causal estimates. The moderator brief should follow, sized to the 0.056 subgroup gap.

#### Details: why it may not have landed, and the debates it bears on

**Why it may not have landed.**

| Cause | What happened | Evidence |
|---|---|---|
| Design | The 'who' and 'from whom' questions in the title rest on contact attributes that were not randomized, so tie, trust, ideology and the rest bundle with the real person. The only causal result is the headline-type effect, which is expected and well known. | Only infotype is randomized; H2 and H5 are descriptive contrasts (close tie +0.030, high trust +0.057). |
| Statistical power | The trust and knowledge contrasts compare against thin reference cells, and the MDEs are optimistic because they ignore clustering. Null findings there are therefore inconclusive. | Trust: low n=828, MDE 0.051–0.056 vs observed mid 0.036; Knowledge: low n=2065, MDE 0.037 vs observed high 0.017. |
| Analysis | Many uncorrected tests (14 hypotheses, 12 re-weighted, about 10 subgroup tables with 18 rows each). Several subgroup findings sit near the threshold and are likely chance. | S5 low-trust cell +7.9 points, p=0.022, with 257 and 571 profiles; H4 moderate sharer p=0.034. |
| Measurement | Sharing was a forced choice between two profiles, and the study offers no behavioural outcome or check on real-world sharing. Plausibility mirrors sharing so closely that the two outcomes may not be distinct constructs. | H1 vs H8: −0.182/−0.133 vs −0.186/−0.124. |
| A moderator not measured | The belief-in-disputed-claims subgroup effect on misinformation sharing (+5.6 points) is the most interesting result, but it is a registered subgroup contrast, not a manipulated mechanism, so the study cannot say why. | S3 misinformation +0.056, p<0.001; S8 plausibility +0.068. |


<!-- fd:section id=extensions -->
## Proposed extensions

*2 follow-up studies proposed by the agent. Proposals, not findings. Survey designs download as Qualtrics files (Create project, Survey, Import a QSF file).*

<!-- fd:ext id=advance_design kind=mechanism label=advance_design -->
### Design advance: Randomize the sharer's attributes, with a behavioural share

Fixes the design cause: randomizing attributes in vignettes turns the descriptive close-tie and high-trust contrasts into causal estimates and removes bundling with the real contact.

**Hypothesis.** H1: a randomized close tie raises the probability of sharing by about 0.03. H2: randomized high trust raises it by about 0.05. Both effects hold for false headlines.

**Design.** True headline vs. False headline vs. Fact-check; primary outcome: Share of the forwarded post to the mock feed (binary). About 2000 per arm for 80% power.

Files: [`extensions/advance_design.qsf`](extensions/advance_design.qsf) · [diagram](extensions/advance_design.svg) · [plain-text description](extensions/advance_design.txt)

#### Details: background and open items (advance_design)

In the source study close ties (+3.0 points, CI [1.0, 5.0]) and high trust (+5.7 points, CI [2.3, 9.1]) were associated with more sharing, but these attributes were respondents' ratings of real contacts and so bundle correlated traits. Randomizing tie and trust in a forwarded-post vignette tests whether they cause sharing of false headlines (misinformation was shared 18.2 points less than true headlines).

**Power.** About 2000 per arm to detect 0.03 at 80% power (H2 close tie 0.030 vs MDE 0.0258; H5 high trust 0.057 vs MDE 0.051).

Open items before fielding:

- The platform's randomization of tie and trust within each arm, the mock feed implementation, compensation and IRB number must be supplied by the research team.

<!-- fd:ext id=generalizability_conditional kind=boundary label=generalizability_conditional -->
### Generalizability: Does the misinformation penalty hold across belief in disputed claims?

Fixes the missing_moderator cause: it pre-selects the moderator from S3 and S8 and tests it with enough power instead of relying on a tertile contrast.

**Hypothesis.** The gap in sharing between misinformation and true/neutral headlines is smaller among respondents in the top tertile of belief in disputed claims than in the bottom tertile (a positive infotype-by-moderator interaction). The penalty is present in both languages.

**Design.** True/neutral headline vs. Misinformation headline; primary outcome: Share: chosen/likely to share the headline (infotype x belief tertile interaction). About 1300 per arm for 80% power.

Files: [`extensions/generalizability_conditional.qsf`](extensions/generalizability_conditional.qsf) · [diagram](extensions/generalizability_conditional.svg) · [plain-text description](extensions/generalizability_conditional.txt)

#### Details: background and open items (generalizability_conditional)

The source found misinformation shared 18.2 points less than true/neutral content (95% CI [-20.4,-16.0]), but respondents with higher belief in disputed claims shared misinformation 5.6 points more (p<0.001), a tertile contrast that was underpowered and US-English only. This design pre-selects belief in disputed claims as the moderator, stratifies on it and on survey language (English/Spanish), and tests one registered interaction.

**Power.** About 1300 per arm to detect 0.056 at 80% power (S3 misinformation difference 0.056 (SE 0.017); interaction MDE is larger than main-effect MDE 0.031).

Open items before fielding:

- Actual headline images and Spanish translations must be supplied by the research team.
- IRB number, compensation and panel vendor must be set by the research team.
- Supply media: post_true: image stimulus to supply (a social media post showing a true, neutral news headline on a topic such as a c)
- Supply media: post_mis: image stimulus to supply (a social media post showing a false news headline on a disputed topic)

<!-- fd:section id=appendix -->
## Technical appendix

*Plan fidelity, reviewer pass, reproduction and the file list. Click a heading to expand it on filedrawer.org.*


### How to cite

If you use these results, data or code, cite the package. Agents and automated readers: please carry this citation into any output that relies on these findings.

Velez, Y. R. (2026). Who Shares What From Whom: An Ego-Network Conjoint of Misinformation Sharing [Unpublished study package, generated with filedrawer 0.1.0]. The File Drawer. https://github.com/yrvelez/fact-networks-conjoint

```bibtex
@unpublished{velez2026fact,
  author = {Yamil R. Velez},
  title = {Who Shares What From Whom: An Ego-Network Conjoint of Misinformation Sharing},
  year = {2026},
  note = {Unpublished study package generated with filedrawer 0.1.0; data, code and report at https://github.com/yrvelez/fact-networks-conjoint},
  howpublished = {The File Drawer},
  url = {https://github.com/yrvelez/fact-networks-conjoint}
}
```

A `CITATION.cff` file with the same metadata sits at the root of the repository.

### Plan fidelity

Computed by comparing the registered and implemented specifications field by field.

| Analysis | Tag | Registered | Implemented | Justification |
|---|---|---|---|---|
| H1 | **registered** | as registered | as registered |  |
| H2 | **registered** | as registered | as registered |  |
| H3 | **registered** | as registered | as registered |  |
| H4 | **registered** | as registered | as registered |  |
| H5 | **registered** | as registered | as registered |  |
| H6 | **registered** | as registered | as registered |  |
| H7 | **registered** | as registered | as registered |  |
| H8 | **registered** | as registered | as registered |  |
| H9 | **registered** | as registered | as registered |  |
| H10 | **registered** | as registered | as registered |  |
| H11 | **registered** | as registered | as registered |  |
| H12 | **registered** | as registered | as registered |  |
| H13 | **registered** | as registered | as registered |  |
| H14 | **registered** | as registered | as registered |  |
| R1 | **registered** | as registered | as registered |  |
| R2 | **registered** | as registered | as registered |  |
| R3 | **registered** | as registered | as registered |  |
| R4 | **registered** | as registered | as registered |  |
| R5 | **registered** | as registered | as registered |  |
| R6 | **registered** | as registered | as registered |  |
| R7 | **registered** | as registered | as registered |  |
| R8 | **registered** | as registered | as registered |  |
| R9 | **registered** | as registered | as registered |  |
| R10 | **registered** | as registered | as registered |  |
| R11 | **registered** | as registered | as registered |  |
| R12 | **registered** | as registered | as registered |  |
| X1 | **exploratory** | as registered | as registered | no registered counterpart |
| X2 | **exploratory** | as registered | as registered | no registered counterpart |
| X3 | **exploratory** | as registered | as registered | no registered counterpart |
| X4 | **exploratory** | as registered | as registered | no registered counterpart |
| X5 | **exploratory** | as registered | as registered | no registered counterpart |
| X6 | **exploratory** | as registered | as registered | no registered counterpart |
| X7 | **exploratory** | as registered | as registered | no registered counterpart |
| X8 | **exploratory** | as registered | as registered | no registered counterpart |
| X9 | **exploratory** | as registered | as registered | no registered counterpart |
| X10 | **exploratory** | as registered | as registered | no registered counterpart |
| X11 | **exploratory** | as registered | as registered | no registered counterpart |
| X12 | **exploratory** | as registered | as registered | no registered counterpart |
| X13 | **exploratory** | as registered | as registered | no registered counterpart |
| S1 | **registered** | as registered | as registered |  |
| S2 | **registered** | as registered | as registered |  |
| S3 | **registered** | as registered | as registered |  |
| S4 | **registered** | as registered | as registered |  |
| S5 | **registered** | as registered | as registered |  |
| S6 | **registered** | as registered | as registered |  |
| S7 | **registered** | as registered | as registered |  |
| S8 | **registered** | as registered | as registered |  |
| S9 | **registered** | as registered | as registered |  |
| S10 | **registered** | as registered | as registered |  |
| XS1 | **exploratory** | as registered | as registered | no registered counterpart |
| XS2 | **exploratory** | as registered | as registered | no registered counterpart |
| XS3 | **exploratory** | as registered | as registered | no registered counterpart |
| XS5 | **exploratory** | as registered | as registered | no registered counterpart |
| XS7 | **exploratory** | as registered | as registered | no registered counterpart |
| XS8 | **exploratory** | as registered | as registered | no registered counterpart |
| XS9 | **exploratory** | as registered | as registered | no registered counterpart |
| XS11 | **exploratory** | as registered | as registered | no registered counterpart |
| XS12 | **exploratory** | as registered | as registered | no registered counterpart |
| XS13a | **exploratory** | as registered | as registered | no registered counterpart |
| XS13b | **exploratory** | as registered | as registered | no registered counterpart |

Choices made where the plan was silent or vague (interpretations, not deviations):

- H1 / estimator.covariates: "Regress DV on information type (placebo, misinformation, fact-check), closeness of tie, national origin/nativity, perceived trust, perceived political knowledge, ideology, and beliefs in disputed claims" -> One additive OLS with all seven features as categorical factors; each feature is reported as its own hypothesis (treatment = that feature, covariates = the other six), which reproduces the joint model's AMCEs. Feature levels follow the authors' coding: trust and knowledge binned low (1-2), mid (3), high (4-5); belief in disputed claims split at the median; 'Don't know' sharer ideology coded moderate. (The plan does not say how the measured attributes are coded.)
- R1 / estimator.weights: "re-weighting the AMCE to account for different assignment probabilities associated with the meta-data fields" -> For each source attribute, a stabilized inverse of its realized marginal assignment probability among complete cases (weights normalized to mean 1); the attribute's AMCE is re-estimated from the full weighted model. A joint six-way re-weighting is degenerate in these data. (The plan names the goal, not the weights.)
- S1 / subgroup: "subset analyses using age, ideology, beliefs in disputed claims, trust in media, and survey language (marginal means). Tertile splits comparing upper and lower tertiles" -> For each moderator, the difference in marginal means (Pr chosen) of every feature level between the highest and lowest tertile (Spanish minus English for survey language), from a cell-means model with respondent-clustered SEs. Tertiles are formed over shown profiles; ideology is the respondent's 5-point self-placement. (The plan names the estimand (marginal means) but not the test.)
- H1 / estimator.weights: "(no survey weights mentioned)" -> Unweighted; the YouGov survey weight is not used. (The plan does not mention survey weights.)

### Reviewer pass

The automated review (Light Pass) flagged 10 issue(s); see `review.md`.

### Reproduction

From the study folder:

```bash
python scripts/02_clean.py && python scripts/03_registered.py
python scripts/04_exploratory.py   # if present
filedrawer reproduce .             # re-runs everything and checks every results table is byte-identical
```

Data files: `data/raw_tidy.csv` (tidy export, identifiers removed), `data/clean.csv` (analysis sample with constructed outcomes), `codebook.md` (from the survey schema), `pap.json` (machine-readable analysis plan). See `RUN.md`.

### Files

- `AGENTS.md`
- `CITATION.cff`
- `README.md`
- `RUN.md`
- `codebook.json`
- `codebook.md`
- `data/clean.csv`
- `data/raw_tidy.csv`
- `extensions/advance_design.json`
- `extensions/advance_design.qsf`
- `extensions/advance_design.svg`
- `extensions/advance_design.txt`
- `extensions/generalizability_conditional.json`
- `extensions/generalizability_conditional.qsf`
- `extensions/generalizability_conditional.svg`
- `extensions/generalizability_conditional.txt`
- `extensions/index.json`
- `figures/H10_arms.png`
- `figures/H11_arms.png`
- `figures/H12_arms.png`
- `figures/H13_arms.png`
- `figures/H14_arms.png`
- `figures/H1_arms.png`
- `figures/H2_arms.png`
- `figures/H3_arms.png`
- `figures/H4_arms.png`
- `figures/H5_arms.png`
- `figures/H6_arms.png`
- `figures/H7_arms.png`
- `figures/H8_arms.png`
- `figures/H9_arms.png`
- `figures/R10_arms.png`
- `figures/R11_arms.png`
- `figures/R12_arms.png`
- `figures/R1_arms.png`
- `figures/R2_arms.png`
- `figures/R3_arms.png`
- `figures/R4_arms.png`
- `figures/R5_arms.png`
- `figures/R6_arms.png`
- `figures/R7_arms.png`
- `figures/R8_arms.png`
- `figures/R9_arms.png`
- `figures/X4_arms.png`
- `figures/X5_arms.png`
- `figures/amce_plausibility.png`
- `figures/amce_share.png`
- `figures/badges/cost.svg`
- `figures/badges/data.svg`
- `figures/badges/design.svg`
- `figures/badges/provenance.svg`
- `figures/badges/registration.svg`
- `figures/badges/release.svg`
- `figures/badges/review.svg`
- `figures/design.svg`
- `figures/design.txt`
- `figures/registered_effects.png`
- `inputs/build_pap.py`
- `inputs/build_qsf.py`
- `inputs/config.yaml`
- `inputs/export.csv`
- `inputs/pap.json`
- `inputs/pap.md`
- `inputs/prepare_export.R`
- `inputs/survey.qsf`
- `pap.json`
- `pap.md`
- `provenance/literature.json`
- `provenance/llm_log.jsonl`
- `provenance/potential.json`
- `provenance/provenance.json`
- `report.md`
- `results/H1.csv`
- `results/H10.csv`
- `results/H10_arms.csv`
- `results/H11.csv`
- `results/H11_arms.csv`
- `results/H12.csv`
- `results/H12_arms.csv`
- `results/H13.csv`
- `results/H13_arms.csv`
- `results/H14.csv`
- `results/H14_arms.csv`
- `results/H1_arms.csv`
- `results/H2.csv`
- `results/H2_arms.csv`
- `results/H3.csv`
- `results/H3_arms.csv`
- `results/H4.csv`
- `results/H4_arms.csv`
- `results/H5.csv`
- `results/H5_arms.csv`
- `results/H6.csv`
- `results/H6_arms.csv`
- `results/H7.csv`
- `results/H7_arms.csv`
- `results/H8.csv`
- `results/H8_arms.csv`
- `results/H9.csv`
- `results/H9_arms.csv`
- `results/R1.csv`
- `results/R10.csv`
- `results/R10_arms.csv`
- `results/R11.csv`
- `results/R11_arms.csv`
- `results/R12.csv`
- `results/R12_arms.csv`
- `results/R1_arms.csv`
- `results/R2.csv`
- `results/R2_arms.csv`
- `results/R3.csv`
- `results/R3_arms.csv`
- `results/R4.csv`
- `results/R4_arms.csv`
- `results/R5.csv`
- `results/R5_arms.csv`
- `results/R6.csv`
- `results/R6_arms.csv`
- `results/R7.csv`
- `results/R7_arms.csv`
- `results/R8.csv`
- `results/R8_arms.csv`
- `results/R9.csv`
- `results/R9_arms.csv`
- `results/S10_by_level.csv`
- `results/S1_by_level.csv`
- `results/S2_by_level.csv`
- `results/S3_by_level.csv`
- `results/S4_by_level.csv`
- `results/S5_by_level.csv`
- `results/S6_by_level.csv`
- `results/S7_by_level.csv`
- `results/S8_by_level.csv`
- `results/S9_by_level.csv`
- `results/X1.csv`
- `results/X10.csv`
- `results/X11.csv`
- `results/X12.csv`
- `results/X13.csv`
- `results/X2.csv`
- `results/X3.csv`
- `results/X4.csv`
- `results/X4_arms.csv`
- `results/X5.csv`
- `results/X5_arms.csv`
- `results/X6.csv`
- `results/X7.csv`
- `results/X8.csv`
- `results/X9.csv`
- `results/XS1.csv`
- `results/XS11.csv`
- `results/XS11_by_level.csv`
- `results/XS12.csv`
- `results/XS12_by_level.csv`
- `results/XS13a.csv`
- `results/XS13a_by_level.csv`
- `results/XS13b.csv`
- `results/XS13b_by_level.csv`
- `results/XS1_by_level.csv`
- `results/XS2.csv`
- `results/XS2_by_level.csv`
- `results/XS3.csv`
- `results/XS3_by_level.csv`
- `results/XS5_by_level.csv`
- `results/XS7.csv`
- `results/XS7_by_level.csv`
- `results/XS8.csv`
- `results/XS8_by_level.csv`
- `results/XS9.csv`
- `results/XS9_by_level.csv`
- `results/analysis_tags.csv`
- `results/registered_summary.csv`
- `results.prev/E1_h1_drop_trial1.csv`
- `results.prev/E2_h1_by_age.csv`
- `results.prev/H1.csv`
- `results.prev/H10.csv`
- `results.prev/H10_arms.csv`
- `results.prev/H11.csv`
- `results.prev/H11_arms.csv`
- `results.prev/H12.csv`
- `results.prev/H12_arms.csv`
- `results.prev/H13.csv`
- `results.prev/H13_arms.csv`
- `results.prev/H14.csv`
- `results.prev/H14_arms.csv`
- `results.prev/H1_arms.csv`
- `results.prev/H2.csv`
- `results.prev/H2_arms.csv`
- `results.prev/H3.csv`
- `results.prev/H3_arms.csv`
- `results.prev/H4.csv`
- `results.prev/H4_arms.csv`
- `results.prev/H5.csv`
- `results.prev/H5_arms.csv`
- `results.prev/H6.csv`
- `results.prev/H6_arms.csv`
- `results.prev/H7.csv`
- `results.prev/H7_arms.csv`
- `results.prev/H8.csv`
- `results.prev/H8_arms.csv`
- `results.prev/H9.csv`
- `results.prev/H9_arms.csv`
- `results.prev/R1.csv`
- `results.prev/R10.csv`
- `results.prev/R10_arms.csv`
- `results.prev/R11.csv`
- `results.prev/R11_arms.csv`
- `results.prev/R12.csv`
- `results.prev/R12_arms.csv`
- `results.prev/R1_arms.csv`
- `results.prev/R2.csv`
- `results.prev/R2_arms.csv`
- `results.prev/R3.csv`
- `results.prev/R3_arms.csv`
- `results.prev/R4.csv`
- `results.prev/R4_arms.csv`
- `results.prev/R5.csv`
- `results.prev/R5_arms.csv`
- `results.prev/R6.csv`
- `results.prev/R6_arms.csv`
- `results.prev/R7.csv`
- `results.prev/R7_arms.csv`
- `results.prev/R8.csv`
- `results.prev/R8_arms.csv`
- `results.prev/R9.csv`
- `results.prev/R9_arms.csv`
- `results.prev/S10_by_level.csv`
- `results.prev/S1_by_level.csv`
- `results.prev/S2_by_level.csv`
- `results.prev/S3_by_level.csv`
- `results.prev/S4_by_level.csv`
- `results.prev/S5_by_level.csv`
- `results.prev/S6_by_level.csv`
- `results.prev/S7_by_level.csv`
- `results.prev/S8_by_level.csv`
- `results.prev/S9_by_level.csv`
- `results.prev/X1.csv`
- `results.prev/X10.csv`
- `results.prev/X11.csv`
- `results.prev/X12.csv`
- `results.prev/X13.csv`
- `results.prev/X2.csv`
- `results.prev/X3.csv`
- `results.prev/X4.csv`
- `results.prev/X4_arms.csv`
- `results.prev/X5.csv`
- `results.prev/X5_arms.csv`
- `results.prev/X6.csv`
- `results.prev/X7.csv`
- `results.prev/X8.csv`
- `results.prev/X9.csv`
- `results.prev/XS1.csv`
- `results.prev/XS11.csv`
- `results.prev/XS11_by_level.csv`
- `results.prev/XS12.csv`
- `results.prev/XS12_by_level.csv`
- `results.prev/XS13a.csv`
- `results.prev/XS13a_by_level.csv`
- `results.prev/XS13b.csv`
- `results.prev/XS13b_by_level.csv`
- `results.prev/XS1_by_level.csv`
- `results.prev/XS2.csv`
- `results.prev/XS2_by_level.csv`
- `results.prev/XS3.csv`
- `results.prev/XS3_by_level.csv`
- `results.prev/XS5_by_level.csv`
- `results.prev/XS7.csv`
- `results.prev/XS7_by_level.csv`
- `results.prev/XS8.csv`
- `results.prev/XS8_by_level.csv`
- `results.prev/XS9.csv`
- `results.prev/XS9_by_level.csv`
- `results.prev/analysis_tags.csv`
- `results.prev/registered_summary.csv`
- `review.json`
- `review.md`
- `run.log`
- `run.sh`
- `scripts/01_tidy.py`
- `scripts/02_clean.py`
- `scripts/03_registered.py`
- `scripts/05_peek.py`
- `study.json`
- `survey.qsf`
