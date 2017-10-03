import cv2
import os

left 	= os.listdir("../Pictures/Left/")
right 	= os.listdir("../Pictures/Right/")
resize	= os.listdir("../Pictures/Resize/")

size = []

print("Working for left")
for image in left:
	img = cv2.imread("../Pictures/Left/" + image)
	vertical_img = cv2.flip( img, 1 )
	size.append(img.shape)
	cv2.imwrite("../Pictures/Left/" + image, vertical_img)

print(set(size))
print("Working for right")

size = []
for image in right:
	img = cv2.imread("../Pictures/Right/" + image)
	if(img.shape[0]!= 1800 and img.shape[1]!= 2700):
		print(image)
		print(img.shape)

print("Working on resize")

for image in resize:
	img = cv2.imread("../Pictures/Resize/" + image)
	img = cv2.resize(img, (1800, 2700)) 
	cv2.imwrite("../Pictures/Resize/" + image, img)