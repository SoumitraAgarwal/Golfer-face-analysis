import numpy as np
import cv2
import os

base = '../Pictures/Difference/'
images = os.listdir(base)
for k in range(0,len(images),110):

	end 	= min(k + 110, len(images))
	output 	= cv2.imread(base + images[k + 0])
	image1 	= cv2.imread(base + images[k + 1])

	cv2.addWeighted(image1, 1.0/(end - k) , output, 1.0/(end - k), 0, output)

	for i in range(2,end - k):

		# load the image
		image1 = cv2.imread(base + images[k + i])
		cv2.addWeighted(image1, 1.0/(end - k), output, 1, 0, output)
	print(k)
	cv2.imwrite("../Pictures/CDifference/Output" + str(k) + ".png", output)

base = '../Pictures/CDifference/'
images = os.listdir(base)

output 	= cv2.imread(base + images[0])
image1 	= cv2.imread(base + images[1])

cv2.addWeighted(image1, 1.0/len(images) , output, 1.0/len(images), 0, output)

for i in range(2, len(images)):

	image1 = cv2.imread(base + images[i])
	cv2.addWeighted(image1, 1.0/len(images), output, 1, 0, output)

cv2.imwrite("../Pictures/Result/Difference.png", output)