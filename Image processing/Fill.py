import Image
from PIL import Image
import os
import numpy as np
from resizeimage import resizeimage

base 		= '../Pictures/Worked/'
images 		= os.listdir(base)

for image in images:
	print(image)
	img = Image.open(base + image)
	img = img.convert("RGBA")
	datas = img.getdata()

	newData = []
	for item in datas:
	    if item[3] == 0:
	        newData.append((9, 46, 32, 255))
	    else:
	        newData.append(item)

	img.putdata(newData)
	img.save("../Pictures/Worked/" + image, "PNG")