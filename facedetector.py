import numpy as np
import cv2 as cv
import os
from os import listdir
from os.path import isfile, join
import argparse

def detect_face_cv_haarcascades (image_file):
	try:
		face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

		img = cv.imread(image_file)
		gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

		faces = face_cascade.detectMultiScale(gray, 1.03, 5)

		# For debugging
		# for (x, y, w, h) in faces:
		# 	cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

		# cv.imshow('img', img)
		# cv.waitKey(0)
		# cv.destroyAllWindows()

		return faces

	except:
		return ''

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_file", help="Path to Compressed Images.")
    parser.add_argument("--image_dir", help="Path to Directory of Compressed Images")
    args = parser.parse_args()

    if args.image_file is None and args.image_dir is None:
        print("Image not given. Use `--image_file` or `--image_dir` to declare.")
        exit()

    if args.image_file:
    	# Creating Log File
    	log_file = open("face_detection_results.txt","w+")

    	log_file.write(str(detect_face_cv_haarcascades(args.image_file)) + '\n')

    	log_file.close()

    if args.image_dir:
    	# Creating Log File
    	log_file = open(join(args.image_dir, "face_detection_results.txt"),"w+")

    	files = [f for f in listdir(args.image_dir) if isfile(join(args.image_dir, f))]
    	for file in files:
    		file_dir = join(args.image_dir, file)
    		log_file.write(file_dir + ', ' + str(detect_face_cv_haarcascades(file_dir)) + '\n')

    	log_file.close()

    exit()
