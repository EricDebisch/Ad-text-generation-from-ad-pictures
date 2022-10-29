$sourcePath = "C:\Users\Eric\Documents\FOM Studium\Bachelor-Thesis\finishe_data_evaluation\Testrun_00_automobile_finished\*"
$targetPath = "C:\Users\Eric\Documents\FOM Studium\Bachelor-Thesis\finishe_data_evaluation\Testrun_00_automobile_finished\evaluation_representation\PEGASUS_texts_automobile.csv"

$bleurtScoreFiles = Get-ChildItem -Path $sourcePath -Include "*_scores_bleurt.txt"
$counterID = 0
New-Item $targetPath -Value "text_id;pegasus_texts;`n"

foreach($bleurtScoreFile in $bleurtScoreFiles)
    {
    $pegasusGeneratedText = Get-Content $bleurtScoreFile | select -First 1

    $counterID
    $inputPegasusText = [String]$counterID + ";" + $pegasusGeneratedText + ";"
    Add-Content $targetPath -Value $inputPegasusText
    $counterID++

    }