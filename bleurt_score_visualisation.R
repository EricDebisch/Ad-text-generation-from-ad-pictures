# load packages
library(mosaic)
library(psych)
library(readxl)
library(ggplot2)
library(stringr)
#-------Start Import Files-------
#Import of the BLEURT score csv-files
bluert_scores_automobile <- read.csv2("C:\\Users\\Eric\\Documents\\FOM Studium\\Bachelor-Thesis\\finished_data_evaluation_2022-10-30\\Testrun_00_automobile_finished\\evaluation_representation\\BLEURT_scores_automobile.csv", header = TRUE, sep = ";")
bluert_scores_fashion <- read.csv2("C:\\Users\\Eric\\Documents\\FOM Studium\\Bachelor-Thesis\\finished_data_evaluation_2022-10-30\\Testrun_00_fashion_finished\\evaluation_representation\\BLEURT_scores_fashion.csv", header = TRUE, sep = ";")
bluert_scores_automobile_fashion_combined <- read.csv2("C:\\Users\\Eric\\Documents\\FOM Studium\\Bachelor-Thesis\\finished_data_evaluation_2022-10-30\\Testrun_00_fashion_automobile_combined_finished\\evaluation_representation\\BLEURT_scores_automobile_fashion_combined.csv", header = TRUE, sep = ";")

#Import of the generated Pegasus texts
pegasus_texts_automobile <- read.csv2("C:\\Users\\Eric\\Documents\\FOM Studium\\Bachelor-Thesis\\finished_data_evaluation_2022-10-30\\Testrun_00_automobile_finished\\evaluation_representation\\PEGASUS_texts_automobile.csv", header = TRUE, sep = ";")
pegasus_texts_fashion <- read.csv2("C:\\Users\\Eric\\Documents\\FOM Studium\\Bachelor-Thesis\\finished_data_evaluation_2022-10-30\\Testrun_00_fashion_finished\\evaluation_representation\\PEGASUS_texts_fashion.csv", header = TRUE, sep = ";")
pegasus_texts_automobile_fashion_combined <- read.csv2("C:\\Users\\Eric\\Documents\\FOM Studium\\Bachelor-Thesis\\finished_data_evaluation_2022-10-30\\Testrun_00_fashion_automobile_combined_finished\\evaluation_representation\\PEGASUS_texts_automobile_fashion_combined.csv", header = TRUE, sep = ";")

#Import of the overview files
overview_automobile = read.csv2("C:\\Users\\Eric\\Documents\\FOM Studium\\Bachelor-Thesis\\finished_data_evaluation_2022-10-30\\Testrun_00_automobile_finished\\evaluation_representation\\overview_text_evaluation_automobile.csv", header = TRUE, sep = ";")
overview_fashion = read.csv2("C:\\Users\\Eric\\Documents\\FOM Studium\\Bachelor-Thesis\\finished_data_evaluation_2022-10-30\\Testrun_00_fashion_finished\\evaluation_representation\\overview_text_evaluation_fashion.csv", header = TRUE, sep = ";")
overview_automobile_fashion_combined = read.csv2("C:\\Users\\Eric\\Documents\\FOM Studium\\Bachelor-Thesis\\finished_data_evaluation_2022-10-30\\Testrun_00_fashion_automobile_combined_finished\\evaluation_representation\\overview_text_evaluation_automobile_fashion_combined.csv", header = TRUE, sep = ";")

#/-------End Import Files-------

#Converting the BLEURT scores from character to numeric values
bleurt_scores_automobile_numeric <- as.numeric(bluert_scores_automobile$bluert_score_values)
bleurt_scores_fashion_numeric <- as.numeric(bluert_scores_fashion$bluert_score_values)
bleurt_scores_automobile_fashion_combined_numeric <- as.numeric(bluert_scores_automobile_fashion_combined$bluert_score_values)

#Displaying the structure of the numeric BLEURT scores
str(bleurt_scores_automobile_numeric)
str(bleurt_scores_fashion_numeric)
str(bleurt_scores_automobile_fashion_combined_numeric)

bleurt_scores_automobile_numeric
names(bluert_scores_automobile$bluert_score_values)

#Displaying the mean value of the BLEURT scores
mean(bleurt_scores_automobile_numeric)
mean(bleurt_scores_fashion_numeric)
mean(bleurt_scores_automobile_fashion_combined_numeric)

#Displaying the median of the numeric BLEURT scores
median(bleurt_scores_automobile_numeric)
median(bleurt_scores_fashion_numeric)
median(bleurt_scores_automobile_fashion_combined_numeric)

#Displaying the scatterplot of the numeric BLEURT scores
plot(bleurt_scores_automobile_numeric,
     main = "BLEURT Ergebnisse Automobil Branche",
     ylab = "BLEURT Bewertungen",
     xlab = "ID des Datenpunktes")

plot(bleurt_scores_fashion_numeric,
     main = "BLEURT Ergebnisse Fashion Branche",
     ylab = "BLEURT Bewertungen",
     xlab = "ID des Datenpunktes")

plot(bleurt_scores_automobile_fashion_combined_numeric,
     main = "BLEURT Ergebnisse beide Branchen kombiniert",
     ylab = "BLEURT Bewertungen",
     xlab = "ID des Datenpunktes")

#Displaying the quantiles of the numeric BLEURT scores
quantile(bleurt_scores_automobile_numeric)
quantile(bleurt_scores_fashion_numeric)
quantile(bleurt_scores_automobile_fashion_combined_numeric)

#Displaying a boxplot model of the numeric values
boxplot(bleurt_scores_automobile_numeric)
boxplot(bleurt_scores_fashion_numeric)
boxplot(bleurt_scores_automobile_fashion_combined_numeric)

boxplot(bleurt_scores_automobile_numeric,bleurt_scores_fashion_numeric, bleurt_scores_automobile_fashion_combined_numeric,
        main = "Boxplots nach Branchen",
        ylab = "BLEURT Bewertungen",
        names = c("Automobile", "Fashion", "Beide kombiniert"))

#Dislpaying the frequency and difference between generated Pegasus texts
table(pegasus_texts_automobile$pegasus_texts)
table(pegasus_texts_fashion$pegasus_texts)
table(pegasus_texts_automobile_fashion_combined$pegasus_texts)

par(mar=c(11,4,4,4))
barplot(table(pegasus_texts_automobile$pegasus_texts), horiz =  TRUE,
        main = "H??ufigkeit der Pegasustexte Automobil Branche",
        xlab = "Generierte Texte",
        ylab = "H??ufigkeit der selben Texte",
        las = 2,
        cex.names = 0.8
        )


barplot(table(pegasus_texts_fashion$pegasus_texts), horiz =  FALSE,
        main = "H??ufigkeit der Pegasustexte Fashion Branche",
        xlab = "Generierte Texte",
        ylab = "H??ufigkeit der selben Texte"
)

barplot(table(pegasus_texts_automobile_fashion_combined$pegasus_texts), horiz =  FALSE,
        main = "H??ufigkeit der Pegasustexte Branchen kombinierte",
        xlab = "Generierte Texte",
        ylab = "H??ufigkeit der selben Texte"
)

#Correlation of Pegasus inputs and bleurt mean
plot(overview_automobile$mean_bleurt_scores ~ overview_automobile$count_pegasus_input,
     main = "Streudiagramm Automobil Branche",
     xlab = "Anzahl der Eingangstexte f??r Pegasus",
     ylab = "Durchschnittliches BLEURT Ergebnis"
     )

plot(overview_fashion$mean_bleurt_scores ~ overview_fashion$count_pegasus_input,
     main = "Streudiagramm Fashion Branche",
     xlab = "Anzahl der Eingangstexte f??r Pegasus",
     ylab = "Durchschnittliches BLEURT Ergebnis"
)

plot(overview_automobile_fashion_combined$mean_bleurt_scores ~ overview_automobile_fashion_combined$count_pegasus_input,
     main = "Streudiagramm beide Branchen kombiniert",
     xlab = "Anzahl der Eingangstexte f??r Pegasus",
     ylab = "Durchschnittliches BLEURT Ergebnis"
)

#Mean of used texts for BLEURT and Pegasus
mean(overview_automobile$count_bleurt_input)
mean(overview_automobile$count_pegasus_input)

mean(overview_fashion$count_bleurt_input)
mean(overview_fashion$count_pegasus_input)

mean(overview_automobile_fashion_combined$count_bleurt_input)
mean(overview_automobile_fashion_combined$count_pegasus_input)

#Linear regression of used pegasus texts to distribution
testmodellauto <- lm(overview_automobile$mean_bleurt_scores ~ overview_automobile$count_pegasus_input)
koeff.testmodellauto <- coef(testmodellauto)
plot(overview_automobile$mean_bleurt_scores ~ overview_automobile$count_pegasus_input,
     main = "Lineare Regression Automobil Branche",
     xlab = "Anzahl Eingangstexte f??r Pegasus",
     ylab = "Durchschnittliches BLEURT Ergebnis"
     )
abline(coef = koeff.testmodellauto)


testmodellfashion <- lm(overview_fashion$mean_bleurt_scores ~ overview_fashion$count_pegasus_input)
koeff.testmodellfashion <- coef(testmodellfashion)
plot(overview_fashion$mean_bleurt_scores ~ overview_fashion$count_pegasus_input,
     main = "Lineare Regression Fashion Branche",
     xlab = "Anzahl Eingangstexte f??r Pegasus",
     ylab = "Durchschnittliches BLEURT Ergebnis"
)
abline(coef = koeff.testmodellfashion)


testmodellautomobilefashion <- lm(overview_automobile_fashion_combined$mean_bleurt_scores ~ overview_automobile_fashion_combined$count_pegasus_input)
koeff.testmodellautomobilefashion <- coef(testmodellautomobilefashion)
plot(overview_automobile_fashion_combined$mean_bleurt_scores ~ overview_automobile_fashion_combined$count_pegasus_input,
     main = "Lineare Regression beide Branchen kombiniert",
     xlab = "Anzahl Eingangstexte f??r Pegasus",
     ylab = "Durchschnittliches BLEURT Ergebnis"
     )
abline(coef = koeff.testmodellautomobilefashion)

#Linear regression values of BLEURT score to amount of input texts for pegasus 
lm(overview_automobile$mean_bleurt_scores ~ overview_automobile$count_pegasus_input)
lm(overview_fashion$mean_bleurt_scores ~ overview_fashion$count_pegasus_input)
lm(overview_automobile_fashion_combined$mean_bleurt_scores ~ overview_automobile_fashion_combined$count_pegasus_input)