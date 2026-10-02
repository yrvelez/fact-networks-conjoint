# Codebook: Social Network Conjoint (May 2023), YouGov - reconstructed schema

Source: qsf

**Arms** (`infotype`, source: flow_embedded): Fact-check, Misinformation, True/neutral

| column | qid | type | label | values |
|---|---|---|---|---|
| `resp_id` | QID1 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Respondent n |  |
| `trial` | QID2 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Conjoint tri | 1=Trial 1; 2=Trial 2; 3=Trial 3; 4=Trial 4 |
| `profile` | QID3 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Position of  | A=Message 1; B=Message 2 |
| `headline_theme` | QID4 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Topic of the |  |
| `infotype` |  | embedded |  |  |
| `close_tie` | QID5 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Asked about  | 1=Close contact; 0=Distant contact |
| `sharer_native_us` | QID6 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Asked about  | 1=Continental US; 0=Elsewhere or don't know |
| `sharer_ideology` | QID9 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Asked about  | Liberal=Liberal; Moderate=Moderate (incl. Don't know); Conservative=Conservative |
| `sharer_trust` | QID7 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Asked about  | 5=Trust; 4=Trust somewhat; 3=Neither trust nor distrust; 2=Distrust somewhat; 1=Distrust |
| `sharer_knowledge` | QID8 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Asked about  | 1=Strongly disagree; 2=Disagree; 3=Neither agree nor disagree; 4=Agree; 5=Strongly agree |
| `sharer_disputed` | QID10 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Asked about  |  |
| `chosen_share` | QID11 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] "Which post  | 1=Chosen; 0=Not chosen |
| `chosen_belief` | QID12 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] "Based on th | 1=Chosen; 0=Not chosen |
| `weight` | QID13 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] YouGov surve |  |
| `survey_language` | QID14 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] "Do you pref | English=English; Spanish=Spanish |
| `age` | QID15 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] Age in years |  |
| `ideo5_self` | QID16 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] "In general, | 1=Very liberal; 2=Liberal; 3=Moderate; 4=Conservative; 5=Very conservative |
| `disputed_self` | QID17 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] "Claims abou |  |
| `media_trust` | QID18 | question | [Reconstructed from YouGov .sav labels; not the fielded instrument] "Trusted pol |  |
