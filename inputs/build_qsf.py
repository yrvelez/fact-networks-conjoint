"""Reconstruct a QSF-shaped schema for the fact_networks YouGov study.

The survey was fielded by YouGov, not Qualtrics, so no QSF exists. This file gives filedrawer the
same schema information a QSF would: one question per column of inputs/export.csv, with YouGov's
question wording and value labels (taken from the variable and value labels in the YouGov .sav),
and a randomizer that sets the information-type arm. Every question text says it is reconstructed.
It contains no responses. Run: python inputs/build_qsf.py  ->  inputs/survey.qsf
"""
import json
from pathlib import Path

NOTE = "[Reconstructed from YouGov .sav labels; not the fielded instrument] "
CONTACT = ("Asked about each of six contacts the respondent named: three close contacts (\"From time to time, "
           "most people discuss important matters with others. Looking back over the last six months, who are the "
           "people with whom you discussed matters important to you?\") and three distant contacts (\"people you "
           "interact with on a regular basis, but do not consider a close contact\"). Value for the contact this "
           "headline was attributed to. ")
CLAIMS = ("Joe Biden is a socialist; The 2020 election was stolen by the Democrats; Covid-19 vaccines modify your DNA; "
          "A new world order - elites who control the media, industry, and government - were implicated in most wars "
          "over the last 200 years; Trump is still president of the United States; Republicans want to end Social "
          "Security and Medicare")

questions = []


def mc(tag, text, choices):
    """choices: list of (export value, label)."""
    questions.append({"tag": tag, "type": "MC", "selector": "SAVR", "text": text, "choices": choices})


def num(tag, text):
    questions.append({"tag": tag, "type": "Slider", "selector": "HSLIDER", "text": text, "choices": []})


num("resp_id", "Respondent number (1-1,500). Replaces the YouGov case id; used to cluster standard errors.")
mc("trial", "Conjoint trial (4 per respondent).", [(str(i), f"Trial {i}") for i in range(1, 5)])
mc("profile", "Position of the headline within the pair: \"Message 1\" or \"Message 2\".", [("A", "Message 1"), ("B", "Message 2")])
num("headline_theme", "Topic of the headline shown (17 topics, e.g. Tucker Carlson, Biden Budget, Guanabana, Polio).")
mc("chosen_share", "\"Which post would you be more likely to share?\" (Message 1 / Message 2). 1 if this headline was chosen.",
   [("1", "Chosen"), ("0", "Not chosen")])
mc("chosen_belief", "\"Based on the available information, which post do you think is more likely to be accurate?\" "
   "(Message 1 / Message 2). 1 if this headline was chosen.", [("1", "Chosen"), ("0", "Not chosen")])
# ---- the seven profile features, coded as in the paper ------------------------------------------
mc("tie", CONTACT + "Whether the contact was named as a close contact or a distant contact.",
   [("Distant tie", "Distant tie"), ("Close tie", "Close tie")])
mc("sharer_origin", CONTACT + "\"Where do personal contacts live?\" Continental US vs. any other answer (Puerto Rico, Latin "
   "America, Other region, Don't know).", [("Foreign origin", "Foreign origin"), ("Continental US", "Continental US")])
mc("sharer_ideology", CONTACT + "\"Political orientation of personal contacts.\" \"Don't know\" coded moderate.",
   [("Liberal sharer", "Liberal sharer"), ("Moderate sharer", "Moderate sharer"), ("Conservative sharer", "Conservative sharer")])
mc("sharer_trust", CONTACT + "\"Trust personal contacts provide accurate information\" (5 points), binned: low = distrust or "
   "distrust somewhat, mid = neither, high = trust or trust somewhat.", [("Trust: low", "Trust: low"), ("Trust: mid", "Trust: mid"), ("Trust: high", "Trust: high")])
mc("sharer_knowledge", CONTACT + "\"Personal contacts knowledgeable about politics\" (5-point agreement), binned: low = "
   "disagree, mid = neither, high = agree.", [("Knowledge: low", "Knowledge: low"), ("Knowledge: mid", "Knowledge: mid"), ("Knowledge: high", "Knowledge: high")])
mc("sharer_conspiracy", CONTACT + "Share of six disputed claims the respondent thinks the contact believes, split at the median. "
   "Claims: " + CLAIMS, [("Conspiracy belief: low", "Conspiracy belief: low"), ("Conspiracy belief: high", "Conspiracy belief: high")])
# ---- the same source attributes as numbers (for slopes) -----------------------------------------
num("close_num", CONTACT + "1 = close contact, 0 = distant contact.")
num("origin_num", CONTACT + "1 = lives in the continental US, 0 = elsewhere or don't know.")
num("trust_raw", CONTACT + "Trust that the contact provides accurate information, 1 = distrust ... 5 = trust.")
num("knowledge_raw", CONTACT + "The contact is knowledgeable about politics, 1 = strongly disagree ... 5 = strongly agree.")
num("conspiracy_raw", CONTACT + "Share of six disputed claims the respondent thinks the contact believes, 0-1.")
for f, lab in (("tie", "tie strength"), ("origin", "sharer origin"), ("ideology", "sharer ideology"), ("trust", "trust in the sharer"),
               ("knowledge", "sharer political knowledge"), ("conspiracy", "sharer belief in disputed claims")):
    num(f"ipw_{f}", f"Stabilized inverse of the realized assignment probability of {lab} (complete cases; mean 1). "
        "Used for the registered re-weighting.")
# ---- respondent ----------------------------------------------------------------------------------
mc("survey_language", "\"Do you prefer to take the survey in English or Spanish?\"", [("English", "English"), ("Spanish", "Spanish")])
num("age", "Age in years, computed as 2023 minus \"In what year were you born?\"")
num("ideo5_self", "\"In general, how would you describe your own political viewpoint?\" 1 = very liberal ... 5 = very "
    "conservative; \"Not sure\" is missing.")
num("disputed_self", "\"Claims about American politics\" (True / Not True). Share of the six claims the respondent rated True, 0-1. "
    "Claims: " + CLAIMS)
num("media_trust", "\"Trusted political news sources\": mean of six items (Family and friends; WhatsApp groups; Social media; "
    "Conservative media; Liberal media; Spanish-language media), 1 = distrust ... 5 = trust.")
mc("resp_nativity", "\"Which of these statements best describes you?\" Immigrant citizen or non-citizen = foreign-born; first, "
   "second or third generation = US-born.", [("US-born", "US-born"), ("Foreign-born", "Foreign-born")])
num("weight", "YouGov survey weight. Not mentioned in the pre-registration and not used.")
for t, lab in (("age_t", "age"), ("ideo_self_t", "respondent ideology (ideo5_self)"), ("disp_self_t", "respondent belief in disputed claims"),
               ("media_t", "media trust")):
    mc(t, f"Tertile of {lab}, formed over shown profiles (the registered subgroup splits).",
       [("Lowest", "Lowest"), ("Middle", "Middle"), ("Highest", "Highest")])
# ---- constructed for the authors' exploratory analyses ---------------------------------------------
mc("share_not_believe", "Among profiles chosen to share: 1 if the respondent chose the OTHER post as more plausible (shared "
   "without believing); missing for profiles not chosen to share.", [("1", "Shared, judged less plausible"), ("0", "Shared and judged more plausible")])
mc("src_congruence", "Respondent and sharer ideology: Congruent = both liberal or both conservative; Incongruent = opposite leans; "
   "Neutral = either is moderate. Respondent lean from ideo5_self (1-2 liberal, 3 moderate, 4-5 conservative).",
   [("Incongruent", "Incongruent"), ("Neutral (a moderate)", "Neutral (a moderate)"), ("Congruent", "Congruent")])
mc("msg_slant", "Ideological slant of the headline (the paper's preliminary automated coding): which side the content favours.",
   [("left", "Left"), ("neutral", "Neutral"), ("right", "Right")])
mc("msg_congenial", "For partisan respondents and partisan-slanted headlines: Congenial = the headline favours the respondent's side.",
   [("Uncongenial", "Uncongenial"), ("Congenial", "Congenial")])
mc("topic_type", "Headline topic type: Health (guanabana, polio) or Political (all other topics).", [("Health", "Health"), ("Political", "Political")])
mc("src_covid", CONTACT + "1 if the respondent thinks this contact believes \"Covid-19 vaccines modify your DNA\".",
   [("1", "Believes the claim"), ("0", "Does not")])
num("net_consp", "Ego network: mean perceived belief in disputed claims across the respondent's named contacts (0-1).")
num("net_ideo_sd", "Ego network: standard deviation of the named contacts' ideology (1-3).")
num("net_trust", "Ego network: mean trust in the named contacts (1-5).")
num("w_resp_misinfo", "For misinformation profiles: 1 / the respondent's number of misinformation profiles (respondent-level weighting).")

ARMS = {
    "True/neutral": ["How to improve your sleep quality", "Exercise reduces cortisol levels",
                     "The benefits of meditation and mindfulness"],
    "Misinformation": ["George Soros has endorsed (Ron) DeSantis for 2024.",
                       "Biden proposes record budget of 6.8 trillion dollars to win against Russia"],
    "Fact-check": ["No, Tucker Carlson didn't say Ukraine is staging dead bodies",
                   "GOP wants a '30% tax on everything'? That ignores taxes that would end, bill's limited chances"],
}
N_HEADLINES = {"True/neutral": 21, "Misinformation": 29, "Fact-check": 30}

elements, blocks, flow = [], {}, []
qid_n = 0


def add_sq(tag, qtype, selector, text, choices):
    global qid_n
    qid_n += 1
    qid = f"QID{qid_n}"
    payload = {"QuestionID": qid, "DataExportTag": tag, "QuestionType": qtype, "Selector": selector,
               "QuestionText": text, "QuestionDescription": tag[:100]}
    if choices:
        payload["Choices"] = {str(i + 1): {"Display": lab} for i, (_, lab) in enumerate(choices)}
        payload["ChoiceOrder"] = [str(i + 1) for i in range(len(choices))]
        payload["RecodeValues"] = {str(i + 1): val for i, (val, _) in enumerate(choices)}
    elements.append({"SurveyID": "SV_reconstructed", "Element": "SQ", "PrimaryAttribute": qid,
                     "SecondaryAttribute": tag, "Payload": payload})
    return qid


main_qids = [add_sq(q["tag"], q["type"], q["selector"], NOTE + q["text"], q["choices"]) for q in questions]
blocks["BL_main"] = {"Type": "Standard", "Description": "Measures (reconstructed)", "ID": "BL_main",
                     "BlockElements": [{"Type": "Question", "QuestionID": q} for q in main_qids]}

arm_groups = []
for i, (arm, examples) in enumerate(ARMS.items(), start=1):
    text = (NOTE + f"Information type: {arm}. Each conjoint profile shows one headline, attributed to one of the "
            f"respondent's six named contacts; the headline (and so its information type) is randomly drawn from "
            f"80 headlines ({N_HEADLINES[arm]} of this type), in English or Spanish. Example headlines: "
            + " | ".join(examples))
    qid = add_sq(f"stim_{i}", "DB", "TB", text, [])
    bid = f"BL_arm{i}"
    blocks[bid] = {"Type": "Standard", "Description": f"Headline: {arm}", "ID": bid,
                   "BlockElements": [{"Type": "Question", "QuestionID": qid}]}
    arm_groups.append({"Type": "Group", "FlowID": f"FL_g{i}", "Description": arm, "Flow": [
        {"Type": "EmbeddedData", "FlowID": f"FL_e{i}", "EmbeddedData": [
            {"Description": "infotype", "Type": "Custom", "Field": "infotype", "VariableType": "String", "Value": arm}]},
        {"Type": "Standard", "ID": bid, "FlowID": f"FL_b{i}"}]})

flow = [{"Type": "BlockRandomizer", "FlowID": "FL_rand", "SubSet": 1, "EvenPresentation": False, "Flow": arm_groups},
        {"Type": "Standard", "ID": "BL_main", "FlowID": "FL_main"}]

qsf = {
    "SurveyEntry": {"SurveyID": "SV_reconstructed",
                    "SurveyName": "Social Network Conjoint (May 2023), YouGov - reconstructed schema",
                    "SurveyDescription": "Reconstructed from the YouGov .sav variable and value labels. Not a "
                                         "Qualtrics export; no responses."},
    "SurveyElements": [
        {"SurveyID": "SV_reconstructed", "Element": "BL", "PrimaryAttribute": "Survey Blocks", "Payload": blocks},
        {"SurveyID": "SV_reconstructed", "Element": "FL", "PrimaryAttribute": "Survey Flow",
         "Payload": {"Type": "Root", "FlowID": "FL_1", "Flow": flow}},
        *elements,
    ],
}
out = Path(__file__).with_name("survey.qsf")
out.write_text(json.dumps(qsf, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"wrote {out} with {len(elements)} questions")
