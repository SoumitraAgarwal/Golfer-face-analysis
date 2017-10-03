import numpy as np
import dlib
import cv2
import os


def get_params(img, d, l_eyes, r_eyes, mouth, nose):


	# Get the landmarks/parts for the face in box d.
	shape 		= predictor(img, d)
	l_eyes[0] 	+= shape.part(40).x
	l_eyes[1] 	+= shape.part(40).y
	r_eyes[0] 	+= shape.part(43).x
	r_eyes[1] 	+= shape.part(43).y
	mouth[0]  	+= shape.part(49).x + shape.part(55).x
	mouth[1] 	+= shape.part(49).y + shape.part(55).y
	nose[0] 	+= shape.part(28).x + shape.part(31).x 
	nose[1] 	+= shape.part(28).y + shape.part(31).y 

	return l_eyes, r_eyes, mouth, nose

def correct_width(img, correction, start):

	if(correction < 0):

		add = np.zeros((img.shape[0], 1, 3))

		print(img.shape)
		print(add.shape)
		if(start == 0):
			img = np.hstack((add, img))

		else:
			img = np.hstack((img, add))

		img = cv2.resize(img, (img.shape[0], img.shape[1] - 1)) 

	else:
		if(start == 0):
			img = img[:, 0:img.shape[1] - 2]
		else:
			img = img[:, 1:img.shape[1] - 1]
		img = cv2.resize(img, (img.shape[0], img.shape[1] + 1)) 
	return img


def correctposx(img, correction):

	if(correction < 0):

		add = np.zeros((img.shape[0], 1, 3))
		img = img[:, 0:img.shape[1] - 1]
		img = np.hstack((add, img))
		# shift left

	else:
		add = np.zeros((img.shape[0], 1, 3))
		img = img[:, 1:img.shape[1]]
		img = np.hstack((img, add))
	return img


def correctposy(img, correction):

	if(correction < 0):

		add = np.zeros((1,img.shape[1], 3))
		img = img[0:img.shape[0] - 1, :]
		img = np.vstack((add, img))
		# shift down

	else:
		add = np.zeros((1,img.shape[1], 3))
		img = img[ 1:img.shape[0], :]
		img = np.vstack((img, add))
	return img

base 		= '../Pictures/Worked/'
detector 	= dlib.get_frontal_face_detector()
predictor 	= dlib.shape_predictor('dlibcascades/shape_predictor_68_face_landmarks.dat')
images 		= os.listdir(base)
l_eyes 		= [0, 0]
r_eyes		= [0, 0]
mouth 		= [0, 0]
nose 		= [0, 0]


# for image in images:
# 	img = cv2.imread(base + image)
# 	dets = detector(img, 1)
# 	for k, d in enumerate(dets):
# 	    l_eyes, r_eyes, mouth, nose = get_params(img, d, l_eyes, r_eyes, mouth, nose)

# 	print("Training via " + image)

# # Average calculation
# l_eyes 	= [int(x/len(images)) for x in l_eyes]
# r_eyes 	= [int(x/len(images)) for x in r_eyes]
# mouth 	= [int(0.5*x/len(images)) for x in mouth]
# nose 	= [int(0.5*x/len(images)) for x in nose]

# print(l_eyes, r_eyes, mouth, nose)

# lr_mean = [(l_eyes[0] + r_eyes[0])/2.0 ,(l_eyes[1] + r_eyes[1])/2.0]

# for image in images:
# 	img = cv2.imread(base + image)
# 	dets = detector(img, 1)
# 	for k, d in enumerate(dets):
		
# 		print("Working for " + image)
		
# 		# Get the landmarks/parts for the face in box d.
# 		shape = predictor(img, d)
		
# 		sl_eyes = [0, 0]
# 		sr_eyes	= [0, 0]
# 		s_mouth	= [0, 0]
# 		s_nose 	= [0, 0]

# 		sl_eyes, sr_eyes, s_mouth, s_nose = get_params(img, d, sl_eyes, sr_eyes, s_mouth, s_nose)

# 		# Average calculation
# 		s_mouth = [int(0.5*x) for x in s_mouth]
# 		s_nose 	= [int(0.5*x) for x in s_nose]

# 		e_mean 	= [(sl_eyes[0] + sr_eyes[0])/2.0, (sl_eyes[1] + sr_eyes[1])/2.0]

# 		correctionx = e_mean[0] - lr_mean[0]  
# 		correctiony = e_mean[1] - lr_mean[1]
		
# 		cv2.imwrite("../Pictures/Worked/" + image, img)			
# 		start 	= 0
# 		while(abs(correctionx) > 1):
			
# 			print(correctionx)	
# 			start += 1
# 			img 	= correctposx(img, correctionx) 
# 			cv2.imwrite("../Pictures/Worked/" + image, img)
			
# 			sl_eyes = [0, 0]
# 			sr_eyes	= [0, 0]
# 			img 	= cv2.imread("../Pictures/Worked/" + image)
# 			detsp 	= detector(img, 1)
# 			for k1, d1 in enumerate(detsp):
# 				sl_eyes, sr_eyes, s_mouth, s_nose = get_params(img, d1, sl_eyes, sr_eyes, s_mouth, s_nose)
# 				e_mean 	= [(sl_eyes[0] + sr_eyes[0])/2.0, (sl_eyes[1] + sr_eyes[1])/2.0]
# 				correctionx = e_mean[0] - lr_mean[0]  
# 				correctiony = e_mean[1] - lr_mean[1]


# for image in images:

# 	print("Working for " + image)
# 	img = cv2.imread("../Pictures/Worked/" + image)
# 	dets = detector(img, 1)
# 	for k, d in enumerate(dets):
		
# 		# Get the landmarks/parts for the face in box d.
# 		shape = predictor(img, d)
		
# 		sl_eyes = [0, 0]
# 		sr_eyes	= [0, 0]
# 		s_mouth	= [0, 0]
# 		s_nose 	= [0, 0]

# 		sl_eyes, sr_eyes, s_mouth, s_nose = get_params(img, d, sl_eyes, sr_eyes, s_mouth, s_nose)

# 		# Average calculation
# 		s_mouth = [int(0.5*x) for x in s_mouth]
# 		s_nose 	= [int(0.5*x) for x in s_nose]

# 		e_mean 	= [(sl_eyes[0] + sr_eyes[0])/2.0, (sl_eyes[1] + sr_eyes[1])/2.0]

# 		correctionx = e_mean[0] - lr_mean[0]  
# 		correctiony = e_mean[1] - lr_mean[1]
		
# 		cv2.imwrite("../Pictures/Worked/" + image, img)			
# 		start 	= 0
# 		while(abs(correctiony) > 1):
			
# 			print(correctiony)	
# 			start += 1
# 			img 	= correctposy(img, correctiony) 
# 			cv2.imwrite("../Pictures/../Pictures/Worked/" + image, img)
			
# 			sl_eyes = [0, 0]
# 			sr_eyes	= [0, 0]
# 			img 	= cv2.imread("../Pictures/Worked/" + image)
# 			detsp 	= detector(img, 1)
# 			for k1, d1 in enumerate(detsp):
# 				sl_eyes, sr_eyes, s_mouth, s_nose = get_params(img, d1, sl_eyes, sr_eyes, s_mouth, s_nose)
# 				e_mean 	= [(sl_eyes[0] + sr_eyes[0])/2.0, (sl_eyes[1] + sr_eyes[1])/2.0]
# 				correctionx = e_mean[0] - lr_mean[0]  
# 				correctiony = e_mean[1] - lr_mean[1]
# 			

l_eyes = [1331, 601];
r_eyes = [1523, 577];
mouth  = [1432, 833];
nose   = [1406, 684];

for image in images:
	print("Working for " + image)
	img 		= cv2.imread(base + image)
	dets 		= detector(img, 1)
	rows,cols,ch = img.shape
	for k, d in enumerate(dets):
		
		# Get the landmarks/parts for the face in box d.
		shape = predictor(img, d)
		sl_eyes = [0, 0]
		sr_eyes	= [0, 0]
		s_mouth	= [0, 0]
		s_nose 	= [0, 0]

		sl_eyes, sr_eyes, s_mouth, s_nose = get_params(img, d, sl_eyes, sr_eyes, s_mouth, s_nose)
		s_mouth = [int(0.5*x) for x in s_mouth]
		pts1 = np.float32([sl_eyes, sr_eyes, s_mouth])
		pts2 = np.float32([l_eyes, r_eyes, mouth])

		# for i in range(68):
		# 	# cv2.circle(img,(shape.part(i).x,shape.part(i).y),4,(0,0,255))
		# 	cv2.circle(img,(s_mouth[0],s_mouth[1]),4,(0,0,255))
		
		print(sl_eyes, sr_eyes, s_mouth)
		print(l_eyes, r_eyes, mouth)	
		M = cv2.getAffineTransform(pts1,pts2)
		dst = cv2.warpAffine(img,M,(cols,rows))	
		cv2.imwrite("../Pictures/Worked/" + image, dst)