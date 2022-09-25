from multiprocessing.reduction import duplicate
from PIL import Image, ImageFont, ImageDraw
import csv
from pip._vendor.distlib.util import CSVWriter
import os
from scipy.spatial import KDTree
import webcolors

def getPixelRGB(funcPixelWidth, funcPixelLength):
    #funcR, funcG, funcB = imageRGB.getpixel((funcPixelWidth,funcPixelLength))
    funcValueRGB = imageRGB.getpixel((funcPixelWidth,funcPixelLength))
    #print(funcR, funcG, funcB)
    #funcValueRGB = "(" + str(funcR)  + "," + str(funcG)  + "," + str(funcB) + ")"
    convert_rgb_to_names(funcValueRGB)
    #csvPixelWriter.writerow([csvPixelCoordinate, csvValueRGB])
    
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
    print(names[index])
    write_color_in_file(names[index])

def write_color_in_file(funcColorName):
    funcMetadataColorsContent = open(metadataFileColorPath, "w")
    for colorValue in funcMetadataColorsContent:
        if(funcColorName == colorValue):
            duplicateColorCounter = duplicateColorCounter + 1
        else:
            print("Color already in List")
        
    if(duplicateColorCounter != funcMetadataColorsContent.length):
        metadataFileColorPath.writerow(funcColorName + ";")
    funcMetadataColorsContent.close()


imagesPath = "C:/Users/Eric/Documents/FOM Studium/Bachelor-Thesis/Advertisement_Images/Web Crawling Images/images/fashion/H&M_Test"
imagesPathFolders = os.listdir(imagesPath)

for imageFileName in imagesPathFolders:
    print(imageFileName)
    imageFullPath = imagesPath + "/" + imageFileName
    print(imageFullPath)
    metadataFileColorPath = imagesPath + "/" + "metadata_color_" + imageFileName.replace(".jpg","") + ".txt"
    #open(metadataFileColorPath, "w")
    MetadataColorsContent = open(metadataFileColorPath, "w")
    MetadataColorsContent.write("colorName\n")
    MetadataColorsContent.close()
    image =  Image.open(imageFullPath)
    imageRGB = image.convert('RGB')
    for counterWidth in range(0, image.size[0], 1):
        for counterLength in range(0, image.size[1], 1):
            getPixelRGB(counterWidth, counterLength)
            print(counterLength, counterWidth)


#csvPixelPath = "C:/Users/Eric/Documents/FOM Studium/Bachelor-Thesis/PixelDistribution.csv"
#csvPixelWriter = csv.writer(open(csvPixelPath, "w"))
#csvPixelWriter.writerow(["PixelCoordinate", "ValueRGB"])


        
        

#image.show()


#info_dict = {
#    "Filename": image.filename,
#    "Image Size": image.size,
#    "Image Height": image.height,
#    "Image Width": image.width,
#    "Image Format": image.format,
#    "Image Mode": image.mode,
#    "Image is Animated": getattr(image, "is_animated", False),
#    "Frames in Image": getattr(image, "n_frames", 1)
#}