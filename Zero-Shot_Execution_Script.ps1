cd C:\Users\Eric\github\zero-shot-image-to-text

$sourceFolder = "C:\Users\Eric\Documents\FOM Studium\Bachelor-Thesis\Advertisement_Images\Web Crawling Images\images\fashion\H&M"

$fileImages = Get-ChildItem $sourceFolder

foreach($image in $fileImages)
    {
    $imageFullPath = $sourceFolder + "\" + $image.name
    $metadataFileName = $image.name.Replace(".jpg","") + "_metadata_zero-shot_text.txt"
    $metadataFilePath = $sourceFolder + "\" + $metadataFileName
    New-Item $metadataFilePath
    write-host "The following image will be read:" $imageFullPath -ForegroundColor Yellow

    & python run.py  --reset_context_delta --caption_img_path $imageFullPath --multi_gpu >> $metadataFilePath
    }


