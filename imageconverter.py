import argparse, os
from PIL import Image

# Converts image (PIL image object) to 24 by 10 ratio
def convert_24_10 (pil_image):
  return pil_image

# Reduces the image (from both sides) until final_percentage of original size
# Maintains 24 by 10 ratio
def reduce_p (pil_image, final_percentage):
  return pil_image

# Compresses the image to 24 by 10 image (tiny!)
def compress (pil_image):
  return pil_image

if __name__ == "__main__":
    # Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_file", help="Path to Pre-Converted Image.")
    parser.add_argument("--resize", type=float, help="Percentage of Pre-Converted Image to Keep")
    parser.add_argument("--results_dir", default="results", help="Changes the name of the directory where the converted images are stored.")
    args = parser.parse_args()

    if args.image_file is None:
        print("Image not given. Use `--image_file` to declare.")
        exit()
    if args.resize is None:
        print("Converting percentage is not given. Use `--resize` to declare.")
        exit()

    # Creates results directory if it doesn't exist
    # file_path = "./%s/" % args.results_dir
    file_path = "./results/"
    directory = os.path.dirname(file_path)
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except Exception as e:
        print("Unable to create results directory. %s" % str(e))
        exit()

    # Opening Image
    try:
      pil_image = Image.open(args.image_file)
    except Exception as e:
      print("Error opening file. %s", str(e))
      exit()
    image_file_name = os.path.splitext(os.path.basename(args.image_file))[0]
    results_image_name = "results/%s" % image_file_name

    # Image Modifications
    pil_image = convert_24_10(pil_image)
    pil_image.save(results_image_name + '_convert.png', 'PNG')

    pil_image = reduce_p(pil_image, args.resize)
    pil_image.save(results_image_name + '_reduce.png', 'PNG')

    pil_image = compress(pil_image)
    pil_image.save(results_image_name + '_compress.png', 'PNG')

    exit()
