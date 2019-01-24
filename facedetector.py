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
		for (x, y, w, h) in faces:
			cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

		cv.imshow('img', img)
		cv.waitKey(0)
		cv.destroyAllWindows()

		return faces

	except:
		return ''

# Runs the face detection algorithms on single image (usually just for debugging)
def run_face_detection_single (image_file):
    # Creating Log File
    log_file = open("face_detection_results.txt","w+")

    log_file.write(str(detect_face_cv_haarcascades(image_file)) + '\n')

    log_file.close()


# Runs the face detection algorithms on a directory of images
def run_face_detection_dir (image_dir):
    # Creating Log File
    log_file = open(join(image_dir, "face_detection_results.txt"),"w+")

    files = [f for f in listdir(image_dir) if isfile(join(image_dir, f))]
    for file in files:
        file_dir = join(image_dir, file)
        log_file.write(file_dir + ', ' + str(detect_face_cv_haarcascades(file_dir)) + '\n')

    log_file.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_file", help="Path to Compressed Images.")
    parser.add_argument("--image_dir", default="results", help="Path to Directory of Compressed Images")
    args = parser.parse_args()

    if args.image_file is None and args.image_dir is None:
        print("Image not given. Use `--image_file` or `--image_dir` to declare.")
        exit()

    if args.image_file:
    	run_face_detection_single(args.image_file)

    if args.image_dir:
    	run_face_detection_dir(args.image_dir)

    exit()
