$sourcePath = "C:\Users\Eric\Documents\FOM Studium\Bachelor-Thesis\finishe_data_evaluation\Testrun_00_fashion_finished\*"
$targetPath = "C:\Users\Eric\Documents\FOM Studium\Bachelor-Thesis\finishe_data_evaluation\Testrun_00_fashion_finished\evaluation_representation\BLEURT_scores_fashion.csv"

$bleurtScoreFiles = Get-ChildItem -Path $sourcePath -Include "*_scores_bleurt.txt"
$counterID = 0
New-Item $targetPath -Value "score_id;bluert_score_values;`n"

foreach($bleurtScoreFile in $bleurtScoreFiles)
    {
    $pegasusGeneratedText = Get-Content $bleurtScoreFile | select -First 1
    $bleurtScores = (Get-Content $bleurtScoreFile | select -Last 1).replace("[","").replace("]","")
    $bleurtScoresSplits = $bleurtScores -split "," -replace " ",""

    foreach($bleurtScoresSplit in $bleurtScoresSplits)
        {
        write-host $bleurtScoresSplit -ForegroundColor Yellow

        $counterID
        $inputBleurtText = [String]$counterID + ";" + $bleurtScoresSplit + ";"
        Add-Content $targetPath -Value $inputBleurtText
        $counterID++

        }


    }