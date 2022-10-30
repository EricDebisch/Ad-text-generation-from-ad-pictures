# load packages
library(mosaic)
library(psych)
library(readxl)
#-------Start Import Files-------
#Import of the BLEURT score csv-files
bluert_scores_automobile <- read.csv2("C:\\Users\\Eric\\Documents\\FOM Studium\\Bachelor-Thesis\\finished_data_evaluation_2022-10-30\\Testrun_00_automobile_finished\\evaluation_representation\\BLEURT_scores_automobile.csv", header = TRUE, sep = ";")
bluert_scores_fashion <- read.csv2("C:\\Users\\Eric\\Documents\\FOM Studium\\Bachelor-Thesis\\finished_data_evaluation_2022-10-30\\Testrun_00_fashion_finished\\evaluation_representation\\BLEURT_scores_fashion.csv", header = TRUE, sep = ";")

#Import of the generated Pegasus texts
pegasus_texts_automobile <- read.csv2("C:\\Users\\Eric\\Documents\\FOM Studium\\Bachelor-Thesis\\finished_data_evaluation_2022-10-30\\Testrun_00_automobile_finished\\evaluation_representation\\PEGASUS_texts_automobile.csv", header = TRUE, sep = ";")
pegasus_texts_fashion <- read.csv2("C:\\Users\\Eric\\Documents\\FOM Studium\\Bachelor-Thesis\\finished_data_evaluation_2022-10-30\\Testrun_00_fashion_finished\\evaluation_representation\\PEGASUS_texts_fashion.csv", header = TRUE, sep = ";")

#Import of the overview files
overview_automobile = read.csv2("C:\\Users\\Eric\\Documents\\FOM Studium\\Bachelor-Thesis\\finished_data_evaluation_2022-10-30\\Testrun_00_automobile_finished\\evaluation_representation\\overview_text_evaluation_automobile.csv", header = TRUE, sep = ";")
overview_fashion = read.csv2("C:\\Users\\Eric\\Documents\\FOM Studium\\Bachelor-Thesis\\finished_data_evaluation_2022-10-30\\Testrun_00_fashion_finished\\evaluation_representation\\overview_text_evaluation_fashion.csv", header = TRUE, sep = ";")

#/-------End Import Files-------

#Converting the BLEURT scores from character to numeric values
bleurt_scores_automobile_numeric <- as.numeric(bluert_scores_automobile$bluert_score_values)
bleurt_scores_fashion_numeric <- as.numeric(bluert_scores_fashion$bluert_score_values)

#Displaying the structure of the numeric BLEURT scores
str(bleurt_scores_automobile_numeric)
str(bleurt_scores_fashion_numeric)

#Displaying the mean of the numeric BLEURT scores
mean(bleurt_scores_automobile_numeric)
mean(bleurt_scores_fashion_numeric)

#Displaying a boxplot model of the numeric values
boxplot(bleurt_scores_automobile_numeric)
boxplot(bleurt_scores_fashion_numeric)

#Dislpaying the frequency and difference between generated Pegasus texts
table(pegasus_texts_automobile$pegasus_texts)
table(pegasus_texts_fashion$pegasus_texts)

#Correlation of pegasus inputs and bleurt mean
plot(overview_automobile$mean_bleurt_scores ~ overview_automobile$count_pegasus_input)
plot(overview_automobile$mean_bleurt_scores ~ overview_automobile$count_bleurt_input)

plot(overview_fashion$mean_bleurt_scores ~ overview_fashion$count_pegasus_input)
plot(overview_fashion$mean_bleurt_scores ~ overview_fashion$count_bleurt_input)

#Mean of used texts for BLEURT and Pegasus
mean(overview_automobile$count_bleurt_input)
mean(overview_automobile$count_pegasus_input)

mean(overview_fashion$count_bleurt_input)
mean(overview_fashion$count_pegasus_input)

#Linear regression of used pegasus texts to distribution
testline <- plot(overview_fashion$mean_bleurt_scores ~ overview_fashion$count_bleurt_input)
lines(testline, fitted(linreg), col = "blue")
linreg <- lm(overview_fashion$mean_bleurt_scores ~ overview_fashion$count_pegasus_input)

testmodell <- lm(overview_fashion$mean_bleurt_scores ~ overview_fashion$count_pegasus_input)
koeff.testmodell <- coef(testmodell)
plot(overview_fashion$mean_bleurt_scores ~ overview_fashion$count_pegasus_input)
abline(coef = koeff.testmodell)

testmodellauto <- lm(overview_automobile$mean_bleurt_scores ~ overview_automobile$count_pegasus_input)
koeff.testmodell <- coef(testmodell)
plot(overview_automobile$mean_bleurt_scores ~ overview_automobile$count_pegasus_input)
abline(coef = koeff.testmodell)