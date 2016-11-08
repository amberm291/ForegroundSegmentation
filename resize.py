'''
Script to resize images in the images folder
'''

import cv2
import glob

images = glob.glob("images/*")
for image in images:
	img = cv2.imread(image)
	img = cv2.resize(img,(240,320))
	cv2.imwrite(image,img)
	print img.shape