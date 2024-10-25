import argparse
from PIL import Image
import os

def convert_webp_to_png(image_name=None):
    current_directory = os.getcwd()

    if image_name:
        webp_file_path = os.path.join(current_directory, image_name)
        if os.path.isfile(webp_file_path) and image_name.endswith(".webp"):
            png_filename = os.path.splitext(image_name)[0] + ".png"
            png_file_path = os.path.join(current_directory, png_filename)

            with Image.open(webp_file_path) as img:
                img.save(png_file_path, "PNG")
                print(f"Converted {image_name} to {png_filename}")
        else:
            print(f"File {image_name} not found or is not a .webp file.")
    else:
        for filename in os.listdir(current_directory):
            if filename.endswith(".webp"):
                webp_file_path = os.path.join(current_directory, filename)
                png_filename = os.path.splitext(filename)[0] + ".png"
                png_file_path = os.path.join(current_directory, png_filename)

                with Image.open(webp_file_path) as img:
                    img.save(png_file_path, "PNG")
                    print(f"Converted {filename} to {png_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert WebP images to PNG format.")
    parser.add_argument("image_name", nargs="?", help="Specific WebP image to convert (optional)")
    args = parser.parse_args()

    convert_webp_to_png(args.image_name)
