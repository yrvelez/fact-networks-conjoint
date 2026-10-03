# Codebook: Social Network Conjoint (May 2023), YouGov - reconstructed schema

Source: qsf

**Arms** (`infotype`, source: flow_embedded): Fact-check, Misinformation, True/neutral

| column | qid | type | label | values |
|---|---|---|---|---|
| `resp_id` | QID1 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Respondent n |  |
| `trial` | QID2 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Conjoint tri | 1=Trial 1; 2=Trial 2; 3=Trial 3; 4=Trial 4 |
| `profile` | QID3 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Position of  | A=Message 1; B=Message 2 |
| `headline_theme` | QID4 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Topic of the |  |
| `chosen_share` | QID5 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] "Which post  | 1=Chosen; 0=Not chosen |
| `chosen_belief` | QID6 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] "Based on th | 1=Chosen; 0=Not chosen |
| `infotype` |  | embedded |  |  |
| `tie` | QID7 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Asked about  | Distant tie=Distant tie; Close tie=Close tie |
| `sharer_origin` | QID8 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Asked about  | Foreign origin=Foreign origin; Continental US=Continental US |
| `sharer_ideology` | QID9 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Asked about  | Liberal sharer=Liberal sharer; Moderate sharer=Moderate sharer; Conservative sharer=Conservative sharer |
| `sharer_trust` | QID10 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Asked about  | Trust: low=Trust: low; Trust: mid=Trust: mid; Trust: high=Trust: high |
| `sharer_knowledge` | QID11 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Asked about  | Knowledge: low=Knowledge: low; Knowledge: mid=Knowledge: mid; Knowledge: high=Knowledge: high |
| `sharer_conspiracy` | QID12 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Asked about  | Conspiracy belief: low=Conspiracy belief: low; Conspiracy belief: high=Conspiracy belief: high |
| `close_num` | QID13 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Asked about  |  |
| `origin_num` | QID14 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Asked about  |  |
| `trust_raw` | QID15 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Asked about  |  |
| `knowledge_raw` | QID16 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Asked about  |  |
| `conspiracy_raw` | QID17 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Asked about  |  |
| `ipw_tie` | QID18 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Stabilized i |  |
| `ipw_origin` | QID19 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Stabilized i |  |
| `ipw_ideology` | QID20 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Stabilized i |  |
| `ipw_trust` | QID21 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Stabilized i |  |
| `ipw_knowledge` | QID22 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Stabilized i |  |
| `ipw_conspiracy` | QID23 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Stabilized i |  |
| `survey_language` | QID24 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] "Do you pref | English=English; Spanish=Spanish |
| `age` | QID25 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Age in years |  |
| `ideo5_self` | QID26 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] "In general, |  |
| `disputed_self` | QID27 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] "Claims abou |  |
| `media_trust` | QID28 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] "Trusted pol |  |
| `resp_nativity` | QID29 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] "Which of th | US-born=US-born; Foreign-born=Foreign-born |
| `weight` | QID30 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] YouGov surve |  |
| `age_t` | QID31 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Tertile of a | Lowest=Lowest; Middle=Middle; Highest=Highest |
| `ideo_self_t` | QID32 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Tertile of r | Lowest=Lowest; Middle=Middle; Highest=Highest |
| `disp_self_t` | QID33 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Tertile of r | Lowest=Lowest; Middle=Middle; Highest=Highest |
| `media_t` | QID34 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Tertile of m | Lowest=Lowest; Middle=Middle; Highest=Highest |
| `share_not_believe` | QID35 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Among profil | 1=Shared, judged less plausible; 0=Shared and judged more plausible |
| `src_congruence` | QID36 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Respondent a | Incongruent=Incongruent; Neutral (a moderate)=Neutral (a moderate); Congruent=Congruent |
| `msg_slant` | QID37 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Ideological  | left=Left; neutral=Neutral; right=Right |
| `msg_congenial` | QID38 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] For partisan | Uncongenial=Uncongenial; Congenial=Congenial |
| `topic_type` | QID39 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Headline top | Health=Health; Political=Political |
| `src_covid` | QID40 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Asked about  | 1=Believes the claim; 0=Does not |
| `net_consp` | QID41 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Ego network: |  |
| `net_ideo_sd` | QID42 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Ego network: |  |
| `net_trust` | QID43 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Ego network: |  |
| `w_resp_misinfo` | QID44 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] For misinfor |  |
