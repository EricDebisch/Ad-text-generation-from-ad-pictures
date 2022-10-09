import os
import re

sourceImagePath = "C:/Users/Eric/Documents/FOM Studium/Bachelor-Thesis/Advertisement_Images/Web Crawling Images/images/fashion/H&M/18894.jpg"
sourceImageMetadataObjectsPath = sourceImagePath.replace(".jpg","_metadata_objects.txt"  )
sourceImageMetadataColorsPath = sourceImagePath.replace(".jpg","_metadata_color.txt"  )

matchingPercentageThreshhold = 0.5

listColorNames = [] #List for colornames, that are in the metadata file
listImagesInFolder = [] #List for only jpg or jpeg files in the target foler. All other file types will be ignored
listInputTextForPegasus = []
listInputTextForBLEURT = []
regexImageFile = ".+\.jpe?g" #Reguluar expression for a file name with .jpg or jpeg file extension
imagesPath = "C:/Users/Eric/Documents/FOM Studium/Bachelor-Thesis/Advertisement_Images/Web Crawling Images/images/fashion/H&M" #Path to the folder to read all images - Adjustment (optional): Recursive to search in subfolders too
imagesPathFolders = os.listdir(imagesPath) #Lists the imagefile names in the specified folder
print(imagesPathFolders)
#Loop to add only jpg or jpeg files to the list
for imagePathFolder in imagesPathFolders:
    if(re.match(regexImageFile, imagePathFolder)):
        listImagesInFolder.append(imagePathFolder)

for imageFileName in listImagesInFolder:
    matchCounterObject = 0
    atchObjectPercentage = 0
    print("image Name: " + str(imageFileName))
    imageFullPath = imagesPath + "/" + imageFileName #Creates the full pathname to the image file
    #print(imageFullPath)
    metadataFileColorPath = imagesPath + "/" +  imageFileName.replace(".jpg","") + "_metadata_color" + ".txt" #Creates the full path to the metadata_color file for the specific image
    metadataFileObjectsPath = imagesPath + "/" + imageFileName.replace(".jpg","") + "_metadata_objects" + ".txt" #Creates the full path to the metadata_color file for the specific image

    sourceImageMetadataObjects = open(sourceImageMetadataObjectsPath, "r")
    sourceImageMetadataColor = open(sourceImageMetadataColorsPath, "r")

    referenceMetadataObjects = open(metadataFileObjectsPath, "r")
    referenceMetadataColor = open(metadataFileColorPath, "r")

    for lineSourceObject in sourceImageMetadataObjects:        
        for lineReferenceObject in referenceMetadataObjects:
            print("Source Object: " + str(lineSourceObject))
            print("Reference Object: " + str(lineReferenceObject))
            if(lineSourceObject == lineReferenceObject):
                matchCounterObject += 1
                print("Match found")
                print(matchCounterObject)
                break
            else:
                i = 0
                #print("No match")
            
    referenceMetadataObjectsLengthRead = open(metadataFileObjectsPath, "r").readlines()
    referenceMetadataObjectsLength = len(referenceMetadataObjectsLengthRead)
    #print(referenceMetadataObjectsLength)
    if(referenceMetadataObjectsLength > 0):
        matchObjectPercentage = matchCounterObject / referenceMetadataObjectsLength
    else:
        matchObjectPercentage = 1
    
    print("Matching Percentage is: " + str(matchObjectPercentage) )
    
    metadataFileZeroShotTextPath = imagesPath + "/" + imageFileName.replace(".jpg","") + "_metadata_zero-shot_text.txt"
    metadataFileZeroShotText = open(metadataFileZeroShotTextPath, "r")

    if(matchObjectPercentage >= matchingPercentageThreshhold):
        listInputTextForPegasus.append(metadataFileZeroShotText.readline())

    else:
        listInputTextForBLEURT.append(metadataFileZeroShotText.readline())
    

    sourceImageMetadataObjects.close()
    sourceImageMetadataColor.close()
    referenceMetadataObjects.close()
    referenceMetadataColor.close()
    metadataFileZeroShotText.close()
    



