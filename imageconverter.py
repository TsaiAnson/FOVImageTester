import argparse, math, os
from PIL import Image

# Converts image (PIL image object) to 24 by 10 ratio
def convert_24_10 (pil_image):
    width, height = pil_image.size
    center_x = width // 2
    center_y = height // 2

    # Mode 1: Keep Whole Face and add Black Bars
    # # Uses the longer unit as reference (keeps original image and pads with zero)
    # unit_width = width / 24.0
    # unit_height = height / 10.0

    # if unit_width > unit_height:
    #     keep_height_half = int(unit_width * 5)
        
    #     cropped_image = pil_image.crop((0, center_y - keep_height_half, width, center_y + keep_height_half))
    # else:
    #     keep_width_half = int(unit_height * 12)

    #     cropped_image = pil_image.crop((center_x - keep_width_half, 0, center_x + keep_width_half, height))

    # Mode 2: Cut Face (More useful for eye detection)
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

def compress_m (pil_image, w, h):
    resized_image = pil_image.resize((w, h))
    
    return resized_image


# Driver Method (returns temporary directory of images)
def process_image (image_file, percentage, result_path):
    # Creates results directory if it doesn't exist
    file_path = "./%s/" % result_path
    directory = os.path.dirname(file_path)
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except Exception as e:
        print("Unable to create results directory. %s" % str(e))
        exit ()

    # Opening Image
    try:
      pil_image = Image.open(image_file)
    except Exception as e:
      print("Error opening file. %s", str(e))
      return 
    image_file_name = os.path.splitext(os.path.basename(image_file))[0]
    results_image_name = "%s/%s" % (result_path, image_file_name)

    # Image Modifications
    pil_image = convert_24_10(pil_image)
    # pil_image.save(results_image_name + '_convert_%f.png' % percentage, 'PNG')

    pil_image = reduce_p(pil_image, percentage)
    # pil_image.save(results_image_name + '_reduce_%f.png' % percentage, 'PNG')

    compressed_image = compress(pil_image)
    compressed_image.save(results_image_name + '_compress_%f.png' % percentage, 'PNG')

    # # For Testing purposes (saving images at different resolutions)
    # compressed_image = compress_m(pil_image, 48, 20)
    # compressed_image.save(results_image_name + '_compress48x20_%f.png' % percentage, 'PNG')

    # compressed_image = compress_m(pil_image, 72, 30)
    # compressed_image.save(results_image_name + '_compress72x30_%f.png' % percentage, 'PNG')

    # compressed_image = compress_m(pil_image, 96, 40)
    # compressed_image.save(results_image_name + '_compress96x40_%f.png' % percentage, 'PNG')

    # compressed_image = compress_m(pil_image, 120, 50)
    # compressed_image.save(results_image_name + '_compress120x50_%f.png' % percentage, 'PNG')

    # compressed_image = compress_m(pil_image, 144, 60)
    # compressed_image.save(results_image_name + '_compress144x60_%f.png' % percentage, 'PNG')

    # compressed_image = compress_m(pil_image, 168, 70)
    # compressed_image.save(results_image_name + '_compress168x70_%f.png' % percentage, 'PNG')

    # compressed_image = compress_m(pil_image, 192, 80)
    # compressed_image.save(results_image_name + '_compress192x80_%f.png' % percentage, 'PNG')

    # compressed_image = compress_m(pil_image, 216, 90)
    # compressed_image.save(results_image_name + '_compress216x90_%f.png' % percentage, 'PNG')

    # compressed_image = compress_m(pil_image, 240, 100)
    # compressed_image.save(results_image_name + '_compress240x100_%f.png' % percentage, 'PNG')

    return

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
    if args.results_dir == "results":
        print("Using default results directory. Use `--results_dir` to customize.")

    process_image(args.image_file, args.resize, args.results_dir)

    exit()
