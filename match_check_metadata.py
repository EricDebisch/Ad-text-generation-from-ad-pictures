import os
import re
import codecs

sourceImagePath = "C:/Users/Eric/Documents/FOM Studium/Bachelor-Thesis/Advertisement_Images/Web Crawling Images/images/Testrun_00/18894.jpg"
sourceImageMetadataObjectsPath = sourceImagePath.replace(".jpg","_metadata_objects.txt"  )
sourceImageMetadataColorsPath = sourceImagePath.replace(".jpg","_metadata_color.txt"  )
textInputPegasusFile = sourceImagePath.replace(".jpg","_input_text_pegasus.txt"  )
textInputBLEURTFile = sourceImagePath.replace(".jpg","_input_text_bleurt.txt"  )
print(sourceImageMetadataObjectsPath)
matchingPercentageThreshhold = 0.5

listColorNames = [] #List for colornames, that are in the metadata file
listImagesInFolder = [] #List for only jpg or jpeg files in the target foler. All other file types will be ignored
listInputTextForPegasus = []
listInputTextForBLEURT = []
regexImageFile = ".+\.jpe?g" #Reguluar expression for a file name with .jpg or jpeg file extension
imagesPath = "C:/Users/Eric/Documents/FOM Studium/Bachelor-Thesis/Advertisement_Images/Web Crawling Images/images/Testrun_00" #Path to the folder to read all images - Adjustment (optional): Recursive to search in subfolders too
imagesPathFolders = os.listdir(imagesPath) #Lists the imagefile names in the specified folder
print(textInputPegasusFile)
textInputPegasus = open(textInputPegasusFile, "w")
textInputPegasus.close()
textInputBLEURT = open(textInputBLEURTFile, "w")
textInputBLEURT.close()
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

    if matchObjectPercentage >= matchingPercentageThreshhold:
        print("Read Line for Pegasus: " + str(metadataFileZeroShotText.readline()))
        #
        inputTextForPegasus = str(metadataFileZeroShotText.readline(0))
        print("Read Line for Pegasus: " + str(inputTextForPegasus))
        with open(metadataFileZeroShotTextPath, "r") as zeroshotFile, open(textInputPegasusFile, "a") as textInputPegasus:
            #zeroshotFile.decode("utf-16")
            for line in zeroshotFile:
                #line.decode("utf-16")
                inputPegasus = line + str("\n")
                print("Okay, the line is: " + str(line))
                listInputTextForPegasus.append(str(line))
                textInputPegasus.write(inputPegasus)
                #textInputPegasus.close()

    else:
        print(metadataFileZeroShotText.readline())
        listInputTextForBLEURT.append(str(metadataFileZeroShotText.readline()))
        textInputBLEURT = open(textInputBLEURTFile, "a")
        textInputBLEURT.write(metadataFileZeroShotText.readline())
        textInputBLEURT.close()
    


    sourceImageMetadataObjects.close()
    sourceImageMetadataColor.close()
    referenceMetadataObjects.close()
    referenceMetadataColor.close()
    metadataFileZeroShotText.close()

print("Pegasus Texts: " + str(listInputTextForPegasus))
print("BLEURT Texts: " + str(listInputTextForBLEURT))