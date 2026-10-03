"""Build inputs/pap.json: the structured plan for the filedrawer pipeline, written by the depositor.

Registered (AsPredicted #132,508, transcribed in inputs/pap.md):
  H1-H7   AMCE of each of the seven features on sharing: the registered regression of the DV on all features,
          with one hypothesis per feature (treatment = that feature, covariates = the other six), so the arm
          coefficients are the additive-model AMCEs; SEs clustered by respondent.
  H8-H14  the same for plausibility.
  R1-R12  item 8(2): each source attribute's AMCE re-weighted by its stabilized per-field inverse assignment
          probability (both DVs).
  S1-S10  item 8(1): differences in marginal means, upper vs. lower tertile of age, respondent ideology,
          respondent belief in disputed claims and media trust, and English vs. Spanish (both DVs).
Exploratory, specified by the authors after seeing the data (implemented only, so tagged exploratory):
  X1-X13 with subgroups XS*, from the paper's sections 5-6 (IDEAS.md A1-A4, B1-B4).

Run from the study repository root: python inputs/build_pap.py
"""
import json
from pathlib import Path

FEATURES = [  # column, label, reference level, levels
    ("infotype", "Information type", "True/neutral", ["True/neutral", "Misinformation", "Fact-check"]),
    ("tie", "Tie strength", "Distant tie", ["Distant tie", "Close tie"]),
    ("sharer_origin", "Sharer origin", "Foreign origin", ["Foreign origin", "Continental US"]),
    ("sharer_ideology", "Sharer ideology", "Liberal sharer", ["Liberal sharer", "Moderate sharer", "Conservative sharer"]),
    ("sharer_trust", "Trust in sharer", "Trust: low", ["Trust: low", "Trust: mid", "Trust: high"]),
    ("sharer_knowledge", "Sharer political knowledge", "Knowledge: low", ["Knowledge: low", "Knowledge: mid", "Knowledge: high"]),
    ("sharer_conspiracy", "Sharer belief in disputed claims", "Conspiracy belief: low", ["Conspiracy belief: low", "Conspiracy belief: high"]),
]
COLS = [f[0] for f in FEATURES]
IPW = {"tie": "ipw_tie", "sharer_origin": "ipw_origin", "sharer_ideology": "ipw_ideology", "sharer_trust": "ipw_trust",
       "sharer_knowledge": "ipw_knowledge", "sharer_conspiracy": "ipw_conspiracy"}
DV = {"share": "sharing", "plausibility": "plausibility"}
CL = "resp_id"


def est(covs, cats=None, kind="ols", weights=None):
    cats = cats if cats is not None else [c for c in covs if c in COLS]
    # numeric covariates are pinned continuous so the codebook's value labels never turn them into factors
    return {"kind": kind, "robust": "HC1", "cluster": CL, "weights": weights, "covariates": covs,
            "categorical": cats, "continuous": [c for c in covs if c not in cats]}


def amce(hid, col, label, ref, levels, outcome, weights=None):
    others = [c for c in COLS if c != col]
    txt = (f"AMCE of {label.lower()} on {DV[outcome]}: each level against '{ref}', from the regression of {DV[outcome]} on all "
           f"seven profile features, SEs clustered by respondent")
    if weights:
        txt += f"; re-weighted by the inverse of the realized assignment probability of {label.lower()} (stabilized)"
    return {"id": hid, "text": txt + ".", "outcome": outcome,
            "label": f"{label} → {DV[outcome]}" + (" (re-weighted)" if weights else ""),
            **({"group": "RW"} if weights else {}),
            "treatment": {"column": col, "arms": [l for l in levels if l != ref], "control": ref},
            "direction": "two_sided", "pooled": False, "subgroup": None, "exclusions": [], "estimator": est(others, weights=weights)}


reg_h, n = [], 0
for outcome in ("share", "plausibility"):
    for col, label, ref, levels in FEATURES:
        n += 1
        reg_h.append(amce(f"H{n}", col, label, ref, levels, outcome))
n = 0
for outcome in ("share", "plausibility"):
    for col, label, ref, levels in FEATURES[1:]:
        n += 1
        reg_h.append(amce(f"R{n}", col, label, ref, levels, outcome, weights=IPW[col]))

MODS = [("age_t", "age"), ("ideo_self_t", "respondent ideology (1 very liberal ... 5 very conservative)"),
        ("disp_self_t", "respondent belief in disputed claims"), ("media_t", "trust in media")]
reg_s, n = [], 0
for outcome, base in (("share", "H1"), ("plausibility", "H8")):
    for mod, mlabel in MODS:
        n += 1
        reg_s.append({"id": f"S{n}", "hypothesis": base, "moderator": mod, "levels": {"Lowest": "Lowest", "Highest": "Highest"},
                      "estimand": "mm_diff", "features": COLS,
                      "expected": f"Marginal means of every feature level on {DV[outcome]}: highest minus lowest tertile of {mlabel}"})
    n += 1
    reg_s.append({"id": f"S{n}", "hypothesis": base, "moderator": "survey_language", "levels": {"English": "English", "Spanish": "Spanish"},
                  "estimand": "mm_diff", "features": COLS,
                  "expected": f"Marginal means of every feature level on {DV[outcome]}: Spanish minus English survey language"})

outcomes = [
    {"name": "share", "label": "Chosen to share", "kind": "single_item", "columns": ["chosen_share"], "reverse": [], "scale": [0, 1],
     "construction": "1 if the profile was chosen in 'Which post would you be more likely to share?'"},
    {"name": "plausibility", "label": "Chosen as more plausible", "kind": "single_item", "columns": ["chosen_belief"], "reverse": [],
     "scale": [0, 1], "construction": "1 if chosen in 'which post do you think is more likely to be accurate?'"},
]
for sg in reg_s:
    sg["label"] = sg["expected"]
registered = {"outcomes": outcomes, "hypotheses": reg_h, "subgroups": reg_s, "sample_exclusions": [],
              "multiple_testing": "none", "alpha": 0.05,
              "groups": {"RW": "Re-weighted AMCEs: each source attribute re-weighted by its inverse assignment probability"}}

# ---- exploratory, specified by the authors (paper sections 5-6) ---------------------------------
CTRL = ["trust_raw", "close_num", "origin_num", "sharer_ideology", "knowledge_raw", "conspiracy_raw"]  # paper's controls


def slope(hid, col, outcome, text, excl=None, covs=None, weights=None):
    covs = covs if covs is not None else [c for c in CTRL if c != col]
    return {"id": hid, "text": text, "outcome": outcome, "treatment": {"column": col, "continuous": True}, "direction": "two_sided",
            "subgroup": None, "exclusions": excl or [],
            "estimator": est(covs, cats=[c for c in covs if c == "sharer_ideology"], weights=weights)}


def by(sid, hid, mod, text, covariates=True):
    return {"id": sid, "hypothesis": hid, "moderator": mod, "expected": text, "estimand": "effect_by", "covariates": covariates}


exp_h = [
    slope("X1", "trust_raw", "share", "A1. Source credibility is conditional on content uncertainty: the slope of sharing on trust in the sharer (1-5), "
          "net of the other source attributes, and how it differs by information type."),
    slope("X2", "trust_raw", "plausibility", "A1. The slope of plausibility on trust in the sharer, by information type."),
    slope("X3", "close_num", "share", "A1. The close-tie premium on sharing, net of the other source attributes, by information type."),
    {"id": "X4", "text": "A2. Sharing without believing: among profiles chosen to share, the probability that the respondent judged the "
     "other post more plausible, by information type, net of source attributes, media trust and age.",
     "outcome": "share_not_believe", "treatment": {"column": "infotype", "arms": ["Misinformation", "Fact-check"], "control": "True/neutral"},
     "direction": "two_sided", "pooled": False, "subgroup": None, "exclusions": [],
     "estimator": est(CTRL + ["media_trust", "age"], cats=["sharer_ideology"])},
    {"id": "X5", "text": "A3. Co-ideological messenger: sharing when the respondent and the sharer lean the same way (both liberal or both "
     "conservative) against opposite leans; pairs involving a moderate form a third group. Cell differences, no controls.",
     "outcome": "share", "treatment": {"column": "src_congruence", "arms": ["Congruent", "Neutral (a moderate)"], "control": "Incongruent"},
     "direction": "two_sided", "pooled": False, "subgroup": None, "exclusions": [], "estimator": est([], cats=[], kind="diff_means")},
    slope("X6", "net_consp", "share", "A4. Ego-network composition: the respondent's six named contacts as a measured network. Among "
          "misinformation profiles, sharing on the network's mean perceived belief in disputed claims, net of network ideological "
          "spread, mean trust, age and ideology. Each misinformation profile is weighted by 1 / the respondent's number of them, which "
          "reproduces the respondent-level regression of the misinformation-sharing rate.",
          excl=["infotype == 'Misinformation'"], covs=["net_ideo_sd", "net_trust", "age", "ideo5_self"], weights="w_resp_misinfo"),
    {"id": "X7", "text": "B1. Message x respondent congruence: among partisan respondents shown partisan-slanted headlines, sharing of "
     "congenial against uncongenial content (headline slant from the paper's preliminary automated coding), by information type.",
     "outcome": "share", "treatment": {"column": "msg_congenial", "contrast": ["Congenial", "Uncongenial"]}, "direction": "two_sided",
     "subgroup": None, "exclusions": [], "estimator": est([], cats=[], kind="diff_means")},
    slope("X8", "conspiracy_raw", "share", "B2. A conspiracy-prone source: the slope of sharing on the sharer's perceived belief in "
          "disputed claims (0-1), net of the other source attributes, by information type."),
    slope("X9", "conspiracy_raw", "plausibility", "B2. The slope of plausibility on the sharer's perceived belief in disputed claims, by information type."),
    {"id": "X10", "text": "B2, claim-specific (thin): for the anti-vaccine (polio) misinformation headline, plausibility when the sharer is "
     "seen as believing 'Covid-19 vaccines modify your DNA' against not.",
     "outcome": "plausibility", "treatment": {"column": "src_covid", "contrast": ["1", "0"]}, "direction": "two_sided",
     "subgroup": None, "exclusions": ["headline_theme == 'Polio'", "infotype == 'Misinformation'"],
     "estimator": est([], cats=[], kind="diff_means")},
    slope("X11", "trust_raw", "share", "B3. Health vs. political misinformation: among misinformation profiles, the trust slope on sharing "
          "for health (guanabana, polio) and political headlines.", excl=["infotype == 'Misinformation'"]),
    slope("X12", "close_num", "share", "B3. Among misinformation profiles, the close-tie premium for health and political headlines.",
          excl=["infotype == 'Misinformation'"]),
    slope("X13", "origin_num", "share", "B4. Sharer origin (continental US vs. elsewhere) and sharing, by survey language and by the "
          "respondent's nativity."),
]
exp_s = [
    by("XS1", "X1", "infotype", "Trust slope on sharing within each information type, and its interaction with information type"),
    by("XS2", "X2", "infotype", "Trust slope on plausibility within each information type"),
    by("XS3", "X3", "infotype", "Close-tie premium on sharing within each information type"),
    by("XS5", "X5", "infotype", "Congruent minus incongruent sharing gap within each information type", covariates=False),
    by("XS7", "X7", "infotype", "Congenial minus uncongenial sharing premium within misinformation and within fact-checks", covariates=False),
    by("XS8", "X8", "infotype", "Conspiracy-prone-source slope on sharing within each information type"),
    by("XS9", "X9", "infotype", "Conspiracy-prone-source slope on plausibility within each information type"),
    by("XS11", "X11", "topic_type", "Trust slope on sharing misinformation: health vs. political headlines"),
    by("XS12", "X12", "topic_type", "Close-tie premium on sharing misinformation: health vs. political headlines"),
    by("XS13a", "X13", "survey_language", "Sharer-origin slope on sharing by survey language"),
    by("XS13b", "X13", "resp_nativity", "Sharer-origin slope on sharing by respondent nativity"),
]
LABELS = {'X1': 'A1. Trust in the sharer → sharing', 'X2': 'A1. Trust in the sharer → plausibility', 'X3': 'A1. Close tie → sharing', 'X4': 'A2. Sharing without believing', 'X5': 'A3. Co-ideological sharer → sharing', 'X6': 'A4. Ego-network conspiracy load → sharing misinformation', 'X7': 'B1. Congenial content → sharing', 'X8': 'B2. Conspiracy-prone sharer → sharing', 'X9': 'B2. Conspiracy-prone sharer → plausibility', 'X10': 'B2. Sharer believes the vaccine claim → plausibility of anti-vaccine misinformation', 'X11': 'B3. Trust → sharing misinformation, health vs. political', 'X12': 'B3. Close tie → sharing misinformation, health vs. political', 'X13': 'B4. Sharer origin → sharing, by language and nativity'}
for h in exp_h:
    h["label"] = LABELS[h["id"]]
implemented = json.loads(json.dumps(registered))
implemented["outcomes"].append({"name": "share_not_believe", "label": "Shared but not judged more plausible", "kind": "single_item",
                                "columns": ["share_not_believe"], "reverse": [], "scale": [0, 1],
                                "construction": "among profiles chosen to share: 1 if the respondent chose the other post as more plausible"})
implemented["hypotheses"] += exp_h
implemented["subgroups"] += exp_s

AMB = [
    {"hypothesis": "H1", "field": "estimator.covariates", "kind": "interpretation",
     "pap_text": "Regress DV on information type (placebo, misinformation, fact-check), closeness of tie, national origin/nativity, perceived trust, perceived political knowledge, ideology, and beliefs in disputed claims",
     "interpretation": "One additive OLS with all seven features as categorical factors; each feature is reported as its own hypothesis "
                       "(treatment = that feature, covariates = the other six), which reproduces the joint model's AMCEs. Feature levels "
                       "follow the authors' coding: trust and knowledge binned low (1-2), mid (3), high (4-5); belief in disputed claims "
                       "split at the median; 'Don't know' sharer ideology coded moderate.",
     "alternatives": ["trust, knowledge and disputed beliefs as linear terms"], "reason": "The plan does not say how the measured attributes are coded."},
    {"hypothesis": "R1", "field": "estimator.weights", "kind": "interpretation",
     "pap_text": "re-weighting the AMCE to account for different assignment probabilities associated with the meta-data fields",
     "interpretation": "For each source attribute, a stabilized inverse of its realized marginal assignment probability among complete "
                       "cases (weights normalized to mean 1); the attribute's AMCE is re-estimated from the full weighted model. A joint "
                       "six-way re-weighting is degenerate in these data.",
     "alternatives": ["joint inverse-probability weights", "the YouGov survey weight"], "reason": "The plan names the goal, not the weights."},
    {"hypothesis": "S1", "field": "subgroup", "kind": "interpretation",
     "pap_text": "subset analyses using age, ideology, beliefs in disputed claims, trust in media, and survey language (marginal means). Tertile splits comparing upper and lower tertiles",
     "interpretation": "For each moderator, the difference in marginal means (Pr chosen) of every feature level between the highest and "
                       "lowest tertile (Spanish minus English for survey language), from a cell-means model with respondent-clustered SEs. "
                       "Tertiles are formed over shown profiles; ideology is the respondent's 5-point self-placement.",
     "alternatives": ["differences in AMCEs"], "reason": "The plan names the estimand (marginal means) but not the test."},
    {"hypothesis": "H1", "field": "estimator.weights", "kind": "interpretation",
     "pap_text": "(no survey weights mentioned)", "interpretation": "Unweighted; the YouGov survey weight is not used.",
     "alternatives": ["YouGov weight"], "reason": "The plan does not mention survey weights."},
]

pap = {
    "source": "pap.md", "title": "Who Shares What From Whom: An Ego-Network Conjoint of Misinformation Sharing",
    "constructs": ["misinformation", "fact_checking", "conjoint_preferences", "social_norms", "media_trust", "partisanship"],
    "keywords": ["misinformation", "sharing", "conjoint", "ego network", "social networks", "fact-check", "source credibility", "Latino"],
    "registration": {"status": "registered", "url": "https://aspredicted.org/8njc-mpqw.pdf", "note": "AsPredicted #132,508"},
    "design": {"type": "conjoint",
               "arms": {"column": "infotype", "treatment": ["Misinformation", "Fact-check"], "control": "True/neutral",
                        "labels": {}, "descriptions": {"True/neutral": "A true or neutral headline (the plan's placebo).",
                                                       "Misinformation": "A false headline.",
                                                       "Fact-check": "A headline correcting a false claim."}},
               "features": [{"column": c, "label": l, "levels": lv, "randomized": c == "infotype"} for c, l, _, lv in FEATURES],
               "measured_note": "the respondent's own ratings of the real contact each headline was attributed to; only the "
                                "headline and its assignment to a contact are randomized",
               "population": {"country": "US", "sample": "yougov"}},
    "registered": registered, "implemented": implemented, "ambiguities": AMB,
}
out = Path(__file__).with_name("pap.json")
out.write_text(json.dumps(pap, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"wrote {out}: {len(reg_h)} registered hypotheses, {len(reg_s)} registered subgroups, "
      f"{len(exp_h)} exploratory hypotheses, {len(exp_s)} exploratory subgroups")
