# load packages
library(mosaic)
library(psych)
library(readxl)

bluert_scores_file <- read.csv2("C:\\Users\\Eric\\Documents\\FOM Studium\\Bachelor-Thesis\\Advertisement_Images\\Web Crawling Images\\images\\Testrun_00_automobile_finished\\evaluation_representation\\BLEURT_scores_automobile.csv", header = TRUE, sep = ";")
View(bluert_scores_file)
str(bluert_scores_file)

gf_boxplot( bluert_score_values ~ 2, data = bluert_scores_file, xlab = element_blank())
gf_point(bluert_scores_file ~ score_id, data = bluert_scores_file)
