# load packages
library(mosaic)
library(psych)
library(readxl)

bluert_scores <- read.csv2("C:\\Users\\Eric\\Documents\\FOM Studium\\Bachelor-Thesis\\Advertisement_Images\\Web Crawling Images\\images\\Testrun_00_automobile_finished\\evaluation_representation\\BLEURT_scores_automobile.csv", header = FALSE, sep = ";")
View(bluert_scores)

boxplot(bluert_scores)
mean(bluert_scores)