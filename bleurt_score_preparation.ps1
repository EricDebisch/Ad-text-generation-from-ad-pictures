$sourcePath = "C:\Users\Eric\Documents\FOM Studium\Bachelor-Thesis\Advertisement_Images\Web Crawling Images\images\Testrun_00_automobile_finished\*"
$targetPath = "C:\Users\Eric\Documents\FOM Studium\Bachelor-Thesis\Advertisement_Images\Web Crawling Images\images\Testrun_00_automobile_finished\evaluation_representation\BLEURT_scores_automobile.csv"

$bleurtScoreFiles = Get-ChildItem -Path $sourcePath -Include "*_scores_bleurt.txt"
$counterID = 0
New-Item $targetPath -Value "score_id;bluert_scores;`n"

foreach($bleurtScoreFile in $bleurtScoreFiles)
    {
    $pegasusGeneratedText = Get-Content $bleurtScoreFile | select -First 1
    $bleurtScores = (Get-Content $bleurtScoreFile | select -Last 1).replace("[","").replace("]","")
    $bleurtScoresSplits = $bluertScores -split "," -replace " ",""

    foreach($bluertScoresSplit in $bluertScoresSplits)
        {
        write-host $bluertScoresSplit -ForegroundColor Yellow

        $counterID
        $inputBleurtText = [String]$counterID + ";" + $bluertScoresSplit + ";"
        Add-Content $targetPath -Value $inputBleurtText
        $counterID++

        }


    }