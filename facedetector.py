import numpy as np
import cv2 as cv
import os
from os import listdir
from os.path import isfile, join, basename, splitext
import argparse
import face_recognition

# Creates results directory if it doesn't exist
def create_dir (result_path):
    file_path = "./%s/" % (result_path)
    directory = os.path.dirname(file_path)
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        return result_path
    except Exception as e:
        print("FaceDetector: Unable to create results directory. %s" % str(e))
        exit ()

def generate_image_name (file, suffix, result_path):
    result_dir = './%s/' % result_path
    file_name = basename(file)
    new_file_name = result_dir + splitext(file_name)[0] + '_' + suffix + splitext(file_name)[1]
    return new_file_name

def detect_face_cv_haarcascades (image_file, result_path):
    try:
        face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

        img = cv.imread(image_file)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 1)

        # For debugging
        for (x, y, w, h) in faces:
            cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        cv.imshow('img', img)
        new_image_name = generate_image_name(image_file, 'haar_def', result_path)
        cv.imwrite(new_image_name, img)
        cv.waitKey(0)
        cv.destroyAllWindows()

        return 'HAAR: ' + new_image_name + ', ' + str(faces) + '\n'

    except Exception as e:
        print(e)
        return ''

def detect_face_cv_haarcascades_alt (image_file, result_path):
    try:
        face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt.xml')

        img = cv.imread(image_file)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 1)

        # For debugging
        for (x, y, w, h) in faces:
            cv.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

        cv.imshow('img', img)
        new_image_name = generate_image_name(image_file, 'haar_alt', result_path)
        cv.imwrite(new_image_name, img)
        cv.waitKey(0)
        cv.destroyAllWindows()

        return 'HAAR ALT: ' + new_image_name + ', ' + str(faces) + '\n'

    except Exception as e:
        print(e)
        return ''

def detect_face_cv_haarcascades_alt2 (image_file, result_path):
    try:
        face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt2.xml')

        img = cv.imread(image_file)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 1)

        # For debugging
        for (x, y, w, h) in faces:
            cv.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)

        cv.imshow('img', img)
        new_image_name = generate_image_name(image_file, 'haar_alt2', result_path)
        cv.imwrite(new_image_name, img)
        cv.waitKey(0)
        cv.destroyAllWindows()

        return 'HAAR ALT2: ' + new_image_name + ', ' + str(faces) + '\n'

    except Exception as e:
        print(e)
        return ''

def detect_face_cv_lbpcascade (image_file, result_path):
    try:
        face_cascade = cv.CascadeClassifier('./data/lbpcascade_frontalface_improved.xml')

        img = cv.imread(image_file)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 1)

        # For debugging
        for (x, y, w, h) in faces:
            cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        cv.imshow('img', img)
        new_image_name = generate_image_name(image_file, 'lbp', result_path)
        cv.imwrite(new_image_name, img)
        cv.waitKey(0)
        cv.destroyAllWindows()

        return 'LBP: ' + new_image_name + ', ' + str(faces) + '\n'

    except Exception as e:
        print(e)
        return ''

# HOG-based model
def detect_face_dlibpypi (image_file, result_path):
    try: 
        # Detecting Faces
        image = face_recognition.load_image_file(image_file)
        faces = face_recognition.face_locations(image)

        # Loading image using cv to draw rectangle
        img = cv.imread(image_file)
        for (top, right, bottom, left) in faces:
            cv.rectangle(img,(left,top),(right,bottom),(0,255,255),2)
        cv.imshow('img', img)
        new_image_name = generate_image_name(image_file, 'dlibpypi', result_path)
        cv.imwrite(new_image_name, img)
        cv.waitKey(0)
        cv.destroyAllWindows()

        return 'DLIBPYPI: ' + new_image_name + ', ' + str(faces) + '\n'

    except Exception as e:
        print(e)
        return ''

# CNN model
def detect_face_dlibpypi_deep (image_file, result_path):
    try: 
        # Detecting Faces
        image = face_recognition.load_image_file(image_file)
        faces = face_recognition.face_locations(image, number_of_times_to_upsample=5, model="cnn")

        # Loading image using cv to draw rectangle
        img = cv.imread(image_file)
        for (top, right, bottom, left) in faces:
            cv.rectangle(img,(left,top),(right,bottom),(0,0,255),1)
        cv.imshow('img', img)
        new_image_name = generate_image_name(image_file, 'dlibpypi', result_path)
        cv.imwrite(new_image_name, img)
        cv.waitKey(0)
        cv.destroyAllWindows()

        return 'DLIBPYPI DEEP: ' + new_image_name + ', ' + str(faces) + '\n'

    except Exception as e:
        print(e)
        return ''

def detect_eyes_cv_haarcascades (image_file, result_path):
    try:
        face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')

        img = cv.imread(image_file)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 1)

        # For debugging
        for (x, y, w, h) in faces:
            cv.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)

        cv.imshow('img', img)
        new_image_name = generate_image_name(image_file, 'haar_def', result_path)
        cv.imwrite(new_image_name, img)
        cv.waitKey(0)
        cv.destroyAllWindows()

        return 'HAAR: ' + new_image_name + ', ' + str(faces) + '\n'

    except Exception as e:
        print(e)
        return ''

def detect_eyes_tree_cv_haarcascades (image_file, result_path):
    try:
        face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

        img = cv.imread(image_file)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 1)

        # For debugging
        for (x, y, w, h) in faces:
            cv.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)

        cv.imshow('img', img)
        new_image_name = generate_image_name(image_file, 'haar_def', result_path)
        cv.imwrite(new_image_name, img)
        cv.waitKey(0)
        cv.destroyAllWindows()

        return 'HAAR: ' + new_image_name + ', ' + str(faces) + '\n'

    except Exception as e:
        print(e)
        return ''

# Runs the face detection algorithms on single image (usually just for debugging)
def run_face_detection_single (image_file, result_path):
    # Creates result directory
    r_dir = create_dir(result_path)
    if r_dir is None:
        return

    # Creating Log File
    log_file = open(join(result_path, "face_detection_results.txt"),"w+")

    # log_file.write(detect_face_cv_haarcascades(image_file, result_path))
    log_file.write(detect_face_cv_lbpcascade(image_file, result_path))

    log_file.close()


# Runs the face detection algorithms on a directory of images
def run_face_detection_dir (image_dir, result_path):
    # Creates result directory
    r_dir = create_dir(result_path)
    if r_dir is None:
        return

    # Creating Log File
    log_file = open(join(result_path, "face_detection_results.txt"),"w+")

    files = [f for f in listdir(image_dir) if isfile(join(image_dir, f))]
    for file in files:
        file_dir = join(image_dir, file)
        # log_file.write(detect_face_cv_haarcascades(file_dir, result_path))
        # log_file.write(detect_face_cv_haarcascades_alt(file_dir, result_path))
        # log_file.write(detect_face_cv_haarcascades_alt2(file_dir, result_path))
        # log_file.write(detect_face_cv_lbpcascade(file_dir, result_path))
        # log_file.write(detect_face_dlibpypi(file_dir, result_path))
        # log_file.write(detect_face_dlibpypi_deep(file_dir, result_path))
        log_file.write(detect_eyes_cv_haarcascades(file_dir, result_path))
        log_file.write(detect_eyes_tree_cv_haarcascades(file_dir, result_path))

    log_file.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_file", help="Path to Compressed Images.")
    parser.add_argument("--image_dir", help="Path to Directory of Compressed Images")
    parser.add_argument("--result_path", default="results", help="Path to processed images.")
    args = parser.parse_args()

    if args.image_file is None and args.image_dir is None:
        print("Image not given. Use `--image_file` or `--image_dir` to declare.")
        exit()

    if args.result_path == 'results':
        print("Using default results directory 'results'. Use `--result_path` to modify.")

    if args.image_file:
        run_face_detection_single(args.image_file, args.result_path)

    if args.image_dir:
        run_face_detection_dir(args.image_dir, args.result_path)

    exit()
