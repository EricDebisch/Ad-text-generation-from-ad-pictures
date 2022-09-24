from PIL import Image, ImageFont, ImageDraw
import csv
from pip._vendor.distlib.util import CSVWriter
import os
from webcolors import rgb_to_name

def getPixelRGB(funcPixelWidth, funcPixelLength):
    funcR, funcG, funcB = imageRGB.getpixel((funcPixelWidth,funcPixelLength))
    print(funcR, funcG, funcB)
    csvPixelCoordinate = str(counterWidth) + ":" + str(counterLength)
    csvValueRGB = str(funcR)  + ":" + str(funcG)  + ":" + str(funcB)
    csvPixelWriter.writerow([csvPixelCoordinate, csvValueRGB])
    




imagesPath = "C:/Users/Eric/Documents/FOM Studium/Bachelor-Thesis/Advertisement_Images/Web Crawling Images/images/fashion/H&M"
imagesPathFolders = os.listdir(imagesPath)

for imageFileName in imagesPathFolders:
    print(folderImage)
    imageFullPath = imagesPath + "/" + imageFileName
image =  Image.open(imageFullPath)
imageRGB = image.convert('RGB')
csvPixelPath = "C:/Users/Eric/Documents/FOM Studium/Bachelor-Thesis/PixelDistribution.csv"
csvPixelWriter = csv.writer(open(csvPixelPath, "w"))
csvPixelWriter.writerow(["PixelCoordinate", "ValueRGB"])

info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image": getattr(image, "n_frames", 1)
}

print(image.size[1])

#for counterWidth in range(0, image.size[0], 1):
#    for counterLength in range(0, image.size[1], 1):
#        getPixelRGB(counterWidth ,counterLength)
#        print(counterLength, counterWidth)
        
        

#image.show()