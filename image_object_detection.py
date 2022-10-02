import torch
import json
import re

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom

# Images
img = "C:/Users/Eric/Documents/FOM Studium/Bachelor-Thesis/Result_Website_Crawling_Images/Web Crawling Images/images/fashion/H&M_Test/18900.jpg"  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
#results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
#print(results.pandas().xyxy[0])
objectsJsonFormat = results.pandas().xyxy[0].to_json(orient="records")

separateDetectecObjects = json.loads(results.pandas().xyxy[0].to_json(orient="records"))
print(separateDetectecObjects)
regexNamePattern = "(?<=\'name\':\s\')(.*?)(?=\'\})"
listDetectedObjectsFull = re.findall(regexNamePattern, str(separateDetectecObjects))
listDetectedObjectsReduced = list(dict.fromkeys(listDetectedObjectsFull) )
print(listDetectedObjectsReduced)

file = open("C:/Users/Eric/Documents/FOM Studium/Bachelor-Thesis/Result_Website_Crawling_Images/Web Crawling Images/images/fashion/H&M_Test/textimg.txt", "a")
for detectedObjectReduced in listDetectedObjectsReduced:
    file.write(str(detectedObjectReduced) + "\n")
file.close