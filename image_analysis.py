from multiprocessing.reduction import duplicate
from PIL import Image, ImageFont, ImageDraw
from pip._vendor.distlib.util import CSVWriter
import os
from scipy.spatial import KDTree
import webcolors
import re
import torch


#This function reads the RGB value for a specific pixel and returns the RGB value
def getPixelRGB(funcPixelWidth, funcPixelLength):
    funcValueRGB = imageRGB.getpixel((funcPixelWidth,funcPixelLength))
    return funcValueRGB

#This function receives the RGB value and converts it to the closets colorname according to the css3 definition
def convert_rgb_to_names(func_rgb_tuple):
    # a dictionary of all the hex and their respective names in css3
    css3_db = webcolors.CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []

    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(webcolors.hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    
    distance, index = kdt_db.query(func_rgb_tuple)
    return names[index]

#Function to detect the objects on the iamge with YOLOv5 and writing tthe detected objects in a textfile
def detect_objects(funcImagePathObjectDetection, funcMetadataFileObjects, ):
    # Model
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom

    # Images
    img = funcImagePathObjectDetection  # or file, Path, PIL, OpenCV, numpy, list

    # Inference
    results = model(img)

    # Results
    #results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
    #print(results.pandas().xyxy[0])
    separateDetectecObjects = json.loads(results.pandas().xyxy[0].to_json(orient="records"))
    print(separateDetectecObjects)
    regexNamePattern = "(?<=\'name\':\s\')(.*?)(?=\'\})"
    listDetectedObjectsFull = re.findall(regexNamePattern, str(separateDetectecObjects))
    listDetectedObjectsReduced = list(dict.fromkeys(listDetectedObjectsFull) )
    print(listDetectedObjectsReduced)

    funcMetadataObjectsFile = open(funcMetadataFileObjects, "a")
    for detectedObjectReduced in listDetectedObjectsReduced:
        funcMetadataObjectsFile.write(str(detectedObjectReduced) + "\n")
    funcMetadataObjectsFile.close

listColorNames = [] #List for colornames, that are in the metadata file
listImagesInFolder = [] #List for only jpg or jpeg files in the target foler. All other file types will be ignored
regexImageFile = ".+\.jpe?g" #Reguluar expression for a file name with .jpg or jpeg file extension
imagesPath = "C:/Users/Eric/Documents/FOM Studium/Bachelor-Thesis/Advertisement_Images/Web Crawling Images/images/fashion/H&M_Test" #Path to the folder to read all images - Adjustment (optional): Recursive to search in subfolders too
imagesPathFolders = os.listdir(imagesPath) #Lists the imagefile names in the specified folder
print(imagesPathFolders)
#Loop to add only jpg or jpeg files to the list
for imagePathFolder in imagesPathFolders:
    if(re.match(regexImageFile, imagePathFolder)):
        listImagesInFolder.append(imagePathFolder)

print(listImagesInFolder)
#For loop to go through every imagefile to read the pixels
for imageFileName in listImagesInFolder:
    print(imageFileName)
    imageFullPath = imagesPath + "/" + imageFileName #Creates the full pathname to the image file
    print(imageFullPath)
    metadataFileColorPath = imagesPath + "/" + "metadata_color_" + imageFileName.replace(".jpg","") + ".txt" #Creates the full path to the metadata_color file for the specific image
    metadataFileObjectsPath = imagesPath + "/" + imageFileName.replace(".jpg","") + "_metadata_objects" + ".txt" #Creates the full path to the metadata_color file for the specific image
    detect_objects(imageFullPath, metadataFileColorPath) #Detects the objects contained in the image file
    
    MetadataColorsContent = open(metadataFileColorPath, "a") #Creates a metadata textfile
    MetadataColorsContent.close() #Closing the textfile. Will be opened later
    image =  Image.open(imageFullPath) #Opens the imagefile with all information like, image resolution
    imageRGB = image.convert('RGB') #Converts the imgage pixels to the RGB value

    #Two loop that through each pixel. The first for loop for the width, the secend for loop for the length. Both parameters combined result to a specific pixel on the image
    for counterWidth in range(0, image.size[0], 1):
        for counterLength in range(0, image.size[1], 1):
            valueRGB = getPixelRGB(counterWidth, counterLength) #Opens the function to read the RGB value for the pixel
            colorName = convert_rgb_to_names(valueRGB) #Opens the function to convert the rgb value to a colorname that is the closest to the RGB value
            duplicateColorCounter = 0
            print(counterWidth, counterLength)
            listColorNamesLength = len(listColorNames)
           #print(listColorNamesLength)
            if(listColorNamesLength == 0):
               listColorNames.append(colorName)
               metadataColorsContentWrite = open(metadataFileColorPath, "a")
               metadataColorsContentWrite.write(colorName + "\n")
               metadataColorsContentWrite.close()
            else:               
                for colorNameValue in listColorNames:
                    #print("value = " + colorNameValue)
                    #print("name = " + colorName)
                    if(colorName == colorNameValue):
                        duplicateColorCounter  += 1
                        #print("duplicate here")

                if(duplicateColorCounter  == 0):
                    #print("write in file")
                    listColorNames.append(colorName)
                    metadataColorsContentWrite = open(metadataFileColorPath, "a")
                    metadataColorsContentWrite.write(colorName + "\n")
                    metadataColorsContentWrite.close()