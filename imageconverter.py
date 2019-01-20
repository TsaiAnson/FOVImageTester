import argparse, math, os
from PIL import Image

# Converts image (PIL image object) to 24 by 10 ratio
def convert_24_10 (pil_image):
    width, height = pil_image.size
    center_x = width // 2
    center_y = height // 2

    # Using width as reference, will only cut height
    unit = width / 24.0
    keep_height_half = int(unit * 5)

    cropped_image = pil_image.crop((0, center_y - keep_height_half, width, center_y + keep_height_half))

    return cropped_image

# Reduces the image (from both sides) until final_percentage of original size
# Maintains 24 by 10 ratio
def reduce_p (pil_image, final_percentage):
    width, height = pil_image.size
    center_x = width // 2
    center_y = height // 2

    unit_perc = final_percentage / 100.0
    perc_sqrt = math.sqrt(unit_perc)
    keep_width_half = int(perc_sqrt * width * 0.5)
    keep_height_half = int(perc_sqrt * height * 0.5)

    cropped_image = pil_image.crop((center_x - keep_width_half, center_y - keep_height_half, center_x + keep_width_half, center_y + keep_height_half))

    return cropped_image

# Compresses the image to 24 by 10 image (tiny!)
def compress (pil_image):
    resized_image = pil_image.resize((24,10))
    
    return resized_image

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
    file_path = "./%s/" % args.results_dir
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
    results_image_name = "%s/%s" % (args.results_dir, image_file_name)

    # Image Modifications
    pil_image = convert_24_10(pil_image)
    pil_image.save(results_image_name + '_convert_%f.png' % args.resize, 'PNG')

    pil_image = reduce_p(pil_image, args.resize)
    pil_image.save(results_image_name + '_reduce_%f.png' % args.resize, 'PNG')

    pil_image = compress(pil_image)
    pil_image.save(results_image_name + '_compress_%f.png' % args.resize, 'PNG')

    exit()
