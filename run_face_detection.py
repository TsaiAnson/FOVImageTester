import argparse
from imageconverter import *
from facedetector import *

# Driver File
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_file", help="Path to Images.")
    parser.add_argument("--image_dir", help="Path to Directory of Images.")
    parser.add_argument("--percentages", default="50,75,100", help="List of image percentages.")
    parser.add_argument("--result_dir", default="results", help="Path to Result Directory.")
    args = parser.parse_args()

    percentages = [float(value) for value in args.percentages.split(',')]

    if args.image_file:
    	for perc in percentages:
    		process_image(args.image_file, perc, args.result_dir)

    if args.image_dir:

    	files = [join(args.image_dir, f) for f in listdir(args.image_dir) if isfile(join(args.image_dir, f))]
    	for file in files:
    		for perc in percentages:
    			process_image(file, perc, args.result_dir)

    # Face Detection
    run_face_detection_dir(args.result_dir)

    exit()