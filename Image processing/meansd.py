import numpy as np
import cv2
import os
import pandas as pd

base 			= '../Pictures/Worked/'
images 			= os.listdir(base)
faceCascade1 	= cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
mean 			= cv2.imread("../Pictures/Result/Result.png")
urls			= pd.read_csv("Players.csv")

names = []
score = []
url   = []

for i in range(len(images)):

	print(images[i])
	image1 	= cv2.imread(base + images[i])
	gray 	= cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
	output 	= abs(np.subtract(image1, mean))
	faces1 	= faceCascade1.detectMultiScale(gray, 1.1, 5)

	for (x, y, w, h) in faces1:
		roi_difference 	= 	output[y:y+h, x:x+w]
		roi_color 		=	image1[y:y+h, x:x+w]
	
	param = np.mean(roi_difference)

	names.append(images[i][:-4])
	score.append(param)

	# print(temp["Url"])
	# url.append(temp["Url"])

	data = pd.DataFrame({
		"Name" 	: names,
		"Score"	: score,
		# "Url"	: url
		})

	data.to_csv("Wire.csv", index = False)
	# cv2.imwrite("../Pictures/FaceDiffC/" + str(param) + "_" + images[i], roi_color)
	# cv2.imwrite("../Pictures/FaceDiff/" + str(param) + "_" + images[i], roi_difference)
	# cv2.imwrite("../Pictures/Difference/" + str(param) + "_" + images[i], output)