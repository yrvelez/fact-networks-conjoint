# prepare_export.R -- build inputs/export.csv for the filedrawer pipeline from the analysis repository.
#
# Reads (not committed here): <analysis repo>/data/long.rds (one row per shown profile, contact names
# already pseudonymized as "Contact k"), data/yougov_analysis.sav (trimmed, pseudonymized YouGov fields)
# and headline_slant.csv (the paper's automated headline-slant coding).
# Writes inputs/export.csv: one row per shown profile, no names, no headline text, no YouGov ids.
#
# Every derived column reproduces the paper's own construction:
#   features and levels      R/prep.R          (trust/knowledge bins, conspiracy median split, DK ideology -> moderate)
#   ipw_*                     R/estimate.R      (stabilized per-field marginal IPW on complete cases)
#   *_t tertiles              R/estimate.R      (dplyr::ntile over profiles)
#   share_not_believe         R/explore.R  A2
#   src_congruence            R/explore.R  A3
#   net_*, w_resp_misinfo     R/explore.R  A4  (the six named contacts as a measured network)
#   msg_slant, msg_congenial  R/explore_B.R B1
#   src_covid, topic_type     R/explore_B.R B2, B3
#   resp_nativity             R/explore_B.R B4
#
# Usage (from the study repository root):
#   Rscript inputs/prepare_export.R "<path to the fact_networks analysis repository>"
suppressMessages({library(dplyr); library(haven); library(stringr)})

args <- commandArgs(trailingOnly = TRUE)
repo <- if (length(args)) args[1] else
  "/Users/yamil/Library/CloudStorage/Dropbox/Current Projects/fact_networks"
long  <- readRDS(file.path(repo, "data", "long.rds"))
raw   <- read_sav(file.path(repo, "data", "yougov_analysis.sav"))
slant <- read.csv(file.path(repo, "headline_slant.csv"), stringsAsFactors = FALSE)
# the slant file was written in a non-UTF-8 locale: Spanish characters are stored as literal "<U+00F3>" escapes
slant$headline <- stringi::stri_unescape_unicode(gsub("<U\\+([0-9A-Fa-f]{4})>", "\\\\u\\1", slant$headline))
na89  <- function(x) { x <- as.numeric(x); x[x %in% c(8, 9)] <- NA; x }

feats  <- c("infotype", "close_f", "native_f", "ideo_f", "trust_f", "know_f", "disp_f")
social <- setdiff(feats, "infotype")

# ---- registered secondary: per-field IPW (estimate.R) and tertiles ----------------------------
cc <- complete.cases(long[feats])
for (v in social) {
  p  <- prop.table(table(long[[v]][cc]))
  w  <- ifelse(cc, 1 / as.numeric(p[as.character(long[[v]])]), NA_real_)
  long[[paste0("ipw_", v)]] <- w / mean(w, na.rm = TRUE)
}
tert <- function(x) as.character(factor(dplyr::ntile(x, 3), levels = 1:3, labels = c("Lowest", "Middle", "Highest")))
long <- long |> mutate(age_t = tert(age), ideo_self_t = tert(ideo5_self),
                       disp_self_t = tert(disputed_self), media_t = tert(media_trust))

# ---- exploratory constructions (explore.R, explore_B.R) ---------------------------------------
long <- long |> mutate(
  share_not_believe = ifelse(chosen_share == 1 & !is.na(chosen_belief), as.numeric(chosen_belief == 0), NA_real_),
  resp_lean = case_when(ideo5_self <= 2 ~ "L", ideo5_self == 3 ~ "M", ideo5_self >= 4 ~ "C"),
  shar_lean = case_when(ideo3 == 1 ~ "L", ideo3 == 2 ~ "M", ideo3 == 3 ~ "C"),
  src_congruence = case_when(is.na(resp_lean) | is.na(shar_lean) ~ NA_character_,
                             resp_lean == "M" | shar_lean == "M" ~ "Neutral (a moderate)",
                             resp_lean == shar_lean ~ "Congruent", TRUE ~ "Incongruent"),
  topic_type = ifelse(theme %in% c("Guanabana", "Polio"), "Health", "Political"))

long <- long |> left_join(slant[, c("headline", "slant")], by = "headline") |>
  mutate(msg_congenial = case_when(
    resp_lean == "L" & slant == "left"  ~ "Congenial",
    resp_lean == "C" & slant == "right" ~ "Congenial",
    resp_lean %in% c("L", "C") & slant %in% c("left", "right") ~ "Uncongenial",
    TRUE ~ NA_character_))

alters <- long |> distinct(caseid, person, ideo3, trust, disputed)
net <- alters |> group_by(caseid) |>
  summarise(net_consp = mean(disputed, na.rm = TRUE), net_ideo_sd = sd(ideo3, na.rm = TRUE),
            net_trust = mean(trust, na.rm = TRUE), .groups = "drop")
long <- long |> left_join(net, by = "caseid")
# A4 is a respondent-level regression of the misinformation-sharing rate; weighting misinformation profiles by
# 1 / (the respondent's number of them) reproduces it exactly at the profile level
long <- long |> group_by(caseid) |>
  mutate(w_resp_misinfo = ifelse(infotype == "Misinformation" & !is.na(chosen_share),
                                 1 / sum(infotype == "Misinformation" & !is.na(chosen_share)), NA_real_)) |> ungroup()

slot <- tibble::tribble(~namecol, ~col,
  "q9_1_1", "q19c_1", "q9_2_1", "q19c_2", "q9_3_1", "q19c_3", "q10_1_1", "q20c_1", "q10_2_1", "q20c_2", "q10_3_1", "q20c_3")
covid <- bind_rows(lapply(seq_len(nrow(slot)), function(i)
  tibble(caseid = raw$caseid, person = str_squish(as.character(raw[[slot$namecol[i]]])),
         src_covid = as.numeric(na89(raw[[slot$col[i]]]) == 1)))) |>
  filter(person != "") |> group_by(caseid, person) |> slice(1) |> ungroup()
long <- long |> left_join(covid, by = c("caseid", "person"))

imm <- raw |> transmute(caseid, resp_nativity = case_when(na89(immigrant) %in% c(1, 2) ~ "Foreign-born",
                                                          !is.na(na89(immigrant)) ~ "US-born"))
long <- long |> left_join(imm, by = "caseid")

# ---- export -----------------------------------------------------------------------------------
out <- long |> transmute(
  resp_id = caseid, trial, profile = arm, headline_theme = theme,
  chosen_share, chosen_belief,
  infotype = as.character(infotype), tie = as.character(close_f), sharer_origin = as.character(native_f),
  sharer_ideology = as.character(ideo_f), sharer_trust = as.character(trust_f),
  sharer_knowledge = as.character(know_f), sharer_conspiracy = as.character(disp_f),
  close_num = close, origin_num = native_us, trust_raw = trust, knowledge_raw = knowledge, conspiracy_raw = round(disputed, 4),
  ipw_tie = ipw_close_f, ipw_origin = ipw_native_f, ipw_ideology = ipw_ideo_f, ipw_trust = ipw_trust_f,
  ipw_knowledge = ipw_know_f, ipw_conspiracy = ipw_disp_f,
  survey_language = c("English", "Spanish")[langpref], age, ideo5_self, disputed_self = round(disputed_self, 4),
  media_trust = round(media_trust, 4), resp_nativity, weight,
  age_t, ideo_self_t, disp_self_t, media_t,
  share_not_believe, src_congruence, msg_slant = slant, msg_congenial, topic_type, src_covid,
  net_consp = round(net_consp, 4), net_ideo_sd = round(net_ideo_sd, 4), net_trust = round(net_trust, 4), w_resp_misinfo)
stopifnot(nrow(out) == 12000, !any(grepl("^Contact", unlist(out[sapply(out, is.character)]))),
          all(long$headline %in% slant$headline))          # every headline, English and Spanish, has a slant code
dest <- file.path("inputs", "export.csv")
write.csv(out, dest, row.names = FALSE, na = "")
cat("wrote", dest, ":", nrow(out), "rows x", ncol(out), "columns\n")
