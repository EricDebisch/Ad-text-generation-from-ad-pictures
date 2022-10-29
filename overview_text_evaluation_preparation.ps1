$sourcePath = "C:\Users\Eric\Documents\FOM Studium\Bachelor-Thesis\finishe_data_evaluation\Testrun_00_fashion_finished\*"
$targetPath = "C:\Users\Eric\Documents\FOM Studium\Bachelor-Thesis\finishe_data_evaluation\Testrun_00_fashion_finished\evaluation_representation\overview_text_evaluation_fashion.csv"

$counterID = 0

$bleurtScoreFiles = Get-ChildItem -Path $sourcePath -Include "*_scores_bleurt.txt"
$bleurtInputFiles = Get-ChildItem -Path $sourcePath -Include "*_input_text_bleurt.txt"
$pegasusInputFiles = Get-ChildItem -Path $sourcePath -Include "*_input_text_pegasus.txt"

New-Item $targetPath -Value "overview_ID;count_bleurt_input;count_pegasus_input;pegaus_text;mean_bleurt_scores;`n"

for($counterID = 0;$counterID -lt $bleurtScoreFiles.count;$counterID++)
    {
    $counterID
    $bleurtScoreSum = 0
    $lengthInputBLEURT = (Get-Content $bleurtInputFiles[$counterID] | Measure-Object -Line).Lines
    $lengthInputPegasus = (Get-Content $pegasusInputFiles[$counterID] | Measure-Object -Line).Lines
    $generatedPegasusText = Get-Content $bleurtScoreFiles[$counterID] | select -First 1

    $bleurtScores = (Get-Content $bleurtScoreFiles[$counterID] | select -Last 1).replace("[","").replace("]","")
    $bleurtScoresSplits = $bleurtScores -split "," -replace " ",""

    

        foreach($bleurtScoresSplit in $bleurtScoresSplits)
        {

        $bleurtScoreSum += $bleurtScoresSplit
        #write-host $bleurtScoresSplit -ForegroundColor Yellow

        }
    $bleurtScoreMean = $bleurtScoreSum / $bleurtScoresSplits.Length

    write-host "Ssum = " $bleurtScoreSum "Mean = " $bleurtScoreMean
    $inputOverviewText = [String]$counterID + ";" + [String]$lengthInputBLEURT + ";" + [String]$lengthInputPegasus + ";" + $generatedPegasusText + ";" + [String]$bleurtScoreMean + ";"
    Add-Content $targetPath -Value $inputOverviewText


    }

