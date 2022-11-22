import os
import re
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch
from bleurt import score

def __generate_Pegasus_Text__(funcListInputForPegasus):

    #The script is an example from HuggingFace.
    #Source URL: https://huggingface.co/docs/transformers/model_doc/pegasus
    #Example text, how the data could be modeled in order to be used to generate text.

    src_text = funcListInputForPegasus

    model_name = "google/pegasus-xsum"

    device = "cuda" if torch.cuda.is_available() else "cpu"

    tokenizer = PegasusTokenizer.from_pretrained(model_name)

    model = PegasusForConditionalGeneration.from_pretrained(model_name).to(device)

    batch = tokenizer(src_text, truncation=True, padding="longest", return_tensors="pt").to(device)

    translated = model.generate(**batch)

    tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    print(tgt_text[0])
    return tgt_text[0]

def __evaluate_Pegasus_text_with_BLEURT__(funcListInputTextForBLEURT, funcListGeneratedPegasusText):

    checkpoint = "D:/Applications/Programming/Python/Python310/Lib/site-packages/bleurt/BLEURT-20"
    references = funcListInputTextForBLEURT
    candidates = funcListGeneratedPegasusText
    #Score is determined as -1.306936502456665. The score is supposed to be between 0 and 1, where 0 is random and 1 is a perfect match.
    #The current score would indicate a random output without context. By the first look, book now could be a fitting text for a picture of a beach in the context of a travel advertisement.
    #The exact evaluation of the score by BLEURT needs to be evaluated, if only longer sentences are scored higher than short sentences.
    #The script scores.py needed to use int64 input tokens as described in https://github.com/yongchanghao/bleurt/commit/e2a36c2bc9bbaef2d18b04eff105fc65466a55ad

    scorer = score.BleurtScorer(checkpoint)
    scores = scorer.score(references=references, candidates=candidates)
    assert type(scores) == list and len(scores) > 0
    print(scores)
    return scores

matchingPercentageThreshhold = 0.25
listImagesInFolder = [] #List for only jpg or jpeg files in the target foler. All other file types will be ignored
regexImageFile = ".+\.jpe?g" #Reguluar expression for a file name with .jpg or jpeg file extension
imagesPath = "C:/Users/Eric/Documents/FOM Studium/Bachelor-Thesis/finished_data_evaluation_2022-10-30/Testrun_00_fashion_automobile_combined_finished" #Path to the folder to read all images - Adjustment (optional): Recursive to search in subfolders too
imagesPathFolders = os.listdir(imagesPath) #Lists the imagefile names in the specified folder 
print(imagesPathFolders)
#Loop to add only jpg or jpeg files to the list
for imagePathFolder in imagesPathFolders:
    if(re.match(regexImageFile, imagePathFolder)):
        listImagesInFolder.append(imagePathFolder)

print(listImagesInFolder)

#For loop to go through every imagefile to read the pixels
for imageFileName in listImagesInFolder:
    print("ImageFileName Path is: " + str(imageFileName))
    sourceImagePath = imagesPath + "/" + imageFileName
    inputSentencesBLEURT = ""
    generatedPegasusText = []
    
    sourceImageMetadataObjectsPath = sourceImagePath.replace(".jpg","_metadata_objects.txt"  )
    sourceImageMetadataColorsPath = sourceImagePath.replace(".jpg","_metadata_color.txt"  )
    textInputPegasusFile = sourceImagePath.replace(".jpg","_input_text_pegasus.txt"  )
    textInputBLEURTFile = sourceImagePath.replace(".jpg","_input_text_bleurt.txt"  )
    metadataOverviewPath = sourceImagePath.replace(".jpg","_metadata_results_overview.csv"  )
    metadaOverviewHeadline = "ImagesForPegasus;InputTextForPegasus;ImagesForBLEURT;InputTextForBLEURT;GeneratedTextPegasus;ScoresBLEURT;"
    scoresBLEURTFile = sourceImagePath.replace(".jpg","_scores_bleurt.txt"  )
    print(sourceImageMetadataObjectsPath)
    

    listColorNames = [] #List for colornames, that are in the metadata file
    listImagesInFolder = [] #List for only jpg or jpeg files in the target foler. All other file types will be ignored
    listInputTextForPegasus = []
    listInputTextForBLEURT = []
    listInputImagesForPegasus = []
    listInputImagesForBLEURT = []
    regexImageFile = ".+\.jpe?g" #Reguluar expression for a file name with .jpg or jpeg file extension
    #imagesPath = "C:/Users/Eric/Documents/FOM Studium/Bachelor-Thesis/Advertisement_Images/Web Crawling Images/images/Testrun_00_prototype" #Path to the folder to read all images - Adjustment (optional): Recursive to search in subfolders too
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
        matchObjectPercentage = 0
        matchCounterColor = 0
        matchColorPercentage = 0
        print("image Name: " + str(imageFileName))
        imageFullPath = imagesPath + "/" + imageFileName #Creates the full pathname to the image file
        #print(imageFullPath)
        metadataFileColorPath = imagesPath + "/" +  imageFileName.replace(".jpg","") + "_metadata_color" + ".txt" #Creates the full path to the metadata_color file for the specific image
        metadataFileObjectsPath = imagesPath + "/" + imageFileName.replace(".jpg","") + "_metadata_objects" + ".txt" #Creates the full path to the metadata_color file for the specific image

        listSourceImageMetadataObjects = []
        #sourceImageMetadataObjects = open(sourceImageMetadataObjectsPath, "r")
        sourceImageMetadataColor = open(sourceImageMetadataColorsPath, "r")

        listReferenceMetadataObjects = []
        #referenceMetadataObjects = open(metadataFileObjectsPath, "r")
        referenceMetadataColor = open(metadataFileColorPath, "r")
        #------Part to estimate the object matching percentage for the images------
        referenceMetadataObjects = open(metadataFileObjectsPath, "r")
        referenceMetadataColor = open(metadataFileColorPath, "r")

        with open(sourceImageMetadataObjectsPath, "r") as sourceImageMetadataObjects, open(metadataFileObjectsPath, "r") as referenceMetadataObjects:
            for lineObject in sourceImageMetadataObjects:
                #inputPegasus = line + str("\n")
                print("Okay, the line is: " + str(sourceImageMetadataObjects))
                listSourceImageMetadataObjects.append(str(lineObject))
                #textInputPegasus.write(inputPegasus)
            for lineObjectReference in referenceMetadataObjects:
                listReferenceMetadataObjects.append(str(lineObjectReference))

        #print("Source Objects = " + str(sourceImageMetadataObjects.readlines()))
        #print("Reference Objects = " + str(referenceMetadataObjects.readlines())) 

        for lineSourceObject in listSourceImageMetadataObjects:
            for lineReferenceObject in listReferenceMetadataObjects:
                print("Source Object: " + str(lineSourceObject))
                print("Reference Object: " + str(lineReferenceObject))
                if(lineSourceObject == lineReferenceObject):
                    matchCounterObject += 1
                    #print("Match found")
                    #print(matchCounterObject)
                    break
                else:
                    i = 0
                    #print("No match")
        

        referenceMetadataObjectsLengthRead = open(metadataFileObjectsPath, "r").readlines()
        referenceMetadataObjectsLength = len(referenceMetadataObjectsLengthRead)
        print("Matches and no: " + str(matchCounterObject))
        if(referenceMetadataObjectsLength > 0):
            matchObjectPercentage = matchCounterObject / referenceMetadataObjectsLength
        else:
            matchObjectPercentage = 1

    #------Part to estimate the color matching percentage for the images------   
        for lineSourceColor in sourceImageMetadataColor:        
            for lineReferenceColor in referenceMetadataColor:
                #print("Source Object: " + str(lineSourceColor))
                #print("Reference Object: " + str(lineReferenceColor))
                if(lineSourceColor == lineReferenceColor):
                    matchCounterColor += 1
                    #print("Match found in the color")
                    #print(matchCounterColor)
                    break
                else:
                    i = 0
                    #print("No match")
                
        referenceMetadataColorLengthRead = open(metadataFileColorPath, "r").readlines()
        referenceMetadataColorLength = len(referenceMetadataColorLengthRead)
        #print(referenceMetadataColorLength)
        if(referenceMetadataColorLength > 0):
            matchColorPercentage = matchCounterColor / referenceMetadataColorLength
        else:
            matchColorPercentage = 1

        matchColorAndObjectPercentage = (matchObjectPercentage + matchColorPercentage) / 2

        print("Matching Percentage Object is: " + str(matchObjectPercentage) )
        print("Matching Percentage Color is: " + str(matchColorPercentage) )
        print("Matching Percentage overall is: " + str(matchColorAndObjectPercentage) )
        
        metadataFileZeroShotTextPath = imagesPath + "/" + imageFileName.replace(".jpg","") + "_metadata_zero-shot_text.txt"
        metadataFileZeroShotText = open(metadataFileZeroShotTextPath, "r")

        if matchColorAndObjectPercentage >= matchingPercentageThreshhold:
            print("Read Line for Pegasus: " + str(metadataFileZeroShotText.readline()))
            #
            inputTextForPegasus = str(metadataFileZeroShotText.readline(0))
            print("Read Line for Pegasus: " + str(inputTextForPegasus))
            listInputImagesForPegasus.append(imageFileName)
            with open(metadataFileZeroShotTextPath, "r") as zeroshotFile, open(textInputPegasusFile, "a") as textInputPegasus:
                for line in zeroshotFile:
                    inputPegasus = line + str("\n")
                    print("Okay, the line is: " + str(line))
                    listInputTextForPegasus.append(str(line))
                    textInputPegasus.write(inputPegasus)

        else:
            print(metadataFileZeroShotText.readline())
            listInputTextForBLEURT.append(str(metadataFileZeroShotText.readline()))
            listInputImagesForBLEURT.append(imageFileName)
            with open(metadataFileZeroShotTextPath, "r") as zeroshotFile, open(textInputBLEURTFile, "a") as textInputBLEURT:
                for line in zeroshotFile:
                    inputBLEURT = line + str("\n")
                    print("Okay, the line is: " + str(line))
                    listInputTextForBLEURT.append(str(line))
                    textInputBLEURT.write(inputBLEURT)
                    inputSentencesBLEURT = inputSentencesBLEURT + str(line)
        


        sourceImageMetadataObjects.close()
        sourceImageMetadataColor.close()
        referenceMetadataObjects.close()
        referenceMetadataColor.close()
        metadataFileZeroShotText.close()

    listInputTextForPegasus = list(filter(None, listInputTextForPegasus))
    listInputTextForBLEURT = list(filter(None, listInputTextForBLEURT))
    #listInputTextForBLEURT = open(textInputBLEURTFile, "r").readlines()
    #listInputTextForBLEURT = inputSentencesBLEURT
    print("Pegasus Texts: " + str(listInputTextForPegasus))
    print("BLEURT Texts: " + str(listInputTextForBLEURT))
    generatedPegasusText = __generate_Pegasus_Text__(listInputTextForPegasus)
    listGeneratedPegasusText = []
    while len(listGeneratedPegasusText) < len(listInputTextForBLEURT):
        listGeneratedPegasusText.append(generatedPegasusText)
    print("generated Text is: " + str(generatedPegasusText))
    scoresBLEURT =  __evaluate_Pegasus_text_with_BLEURT__(listInputTextForBLEURT, listGeneratedPegasusText)

    metadataOverviewFile = open(metadataOverviewPath, "a")
    metadataOverviewFile.write(metadaOverviewHeadline + "\n")
    metadataOverviewFile.write(str(listInputImagesForPegasus).replace("[","").replace("]","").replace("\'","") + ";" + str(listInputTextForPegasus).replace("[","").replace("]","").replace("\'","") + ";" + str(listInputImagesForBLEURT).replace("[","").replace("]","").replace("\'","") + ";" + str(listInputTextForBLEURT).replace("[","").replace("]","").replace("\'","") + ";" + str(generatedPegasusText) + ";" + str(scoresBLEURT).replace("[","").replace("]","").replace("\'","") + ";" + "\n")
    metadataOverviewFile.close()

    scoresBLEURTValue = open(scoresBLEURTFile, "a")
    scoresBLEURTValue.write(str(generatedPegasusText + "\n"))
    scoresBLEURTValue.write(str(scoresBLEURT))
    scoresBLEURTValue.close()