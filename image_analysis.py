from multiprocessing.reduction import duplicate
from PIL import Image, ImageFont, ImageDraw
import csv
from pip._vendor.distlib.util import CSVWriter
import os
from scipy.spatial import KDTree
import webcolors
import time

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
    #print(names[index])
    return names[index]

#This function receives the colorname and the filepath to the metadata file and writes the colorname into the file, if the color is not already present in the file.
def write_color_in_file(funcColorName, funcMetadataFileColorPath):
    duplicateColorCounter = 0

    funcMetadataColorsContent = open(funcMetadataFileColorPath, "r")
    funcMetadataColorsContentLength = len(funcMetadataColorsContent.readlines())
    print(funcMetadataColorsContentLength)
    print("colorName = " + funcColorName)

    #funcListColorNames = []
    #funcListColorNamesLength =

    for funcColorValue in funcMetadataColorsContent: #Issue: The funcColorValue is currently not beeing read. The textfile cannot be read.
        print("readit" + funcColorValue)
        if(funcColorName == funcColorValue):
            duplicateColorCounter  += 1
            print("duplicate here")
        else:
            print("Color not on the list")

    if(duplicateColorCounter  == 0):
        funcMetadataColorsContentWrite = open(funcMetadataFileColorPath, "a")
        funcMetadataColorsContentWrite.write(funcColorName + "\n")
        funcMetadataColorsContentWrite.close()
    funcMetadataColorsContent.close()
    

listColorNames = []
imagesPath = "C:/Users/Eric/Documents/FOM Studium/Bachelor-Thesis/Advertisement_Images/Web Crawling Images/images/fashion/H&M_Test" #Path to the folder to read all images - Adjustment (optional): Recursive to search in subfolders too
imagesPathFolders = os.listdir(imagesPath) #Lists the imagefile names in the specified folder

#For loop to go through every imagefile to read the pixels
for imageFileName in imagesPathFolders:
    print(imageFileName)
    imageFullPath = imagesPath + "/" + imageFileName #Creates the full pathname to the image file
    print(imageFullPath)
    metadataFileColorPath = imagesPath + "/" + "metadata_color_" + imageFileName.replace(".jpg","") + ".txt" #Creates the full path to the metadata_color file for the specific image
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
               listColorNames.append(colorName) #Issue: Second textfile is empty and does not contain any colors. Please test with smaller image size. Process time is 17 seconds for 10 x 1000 pixels
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
                #print(duplicateColorCounter)


            #write_color_in_file(colorName, metadataFileColorPath) #Opens the function to write the colorname into the metadata file