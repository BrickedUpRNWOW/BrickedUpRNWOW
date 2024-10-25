from PIL import Image
import os

def convert_webp_to_png():
    # Get the current working directory
    current_directory = os.getcwd()

    # Iterate through all files in the current directory
    for filename in os.listdir(current_directory):
        if filename.endswith(".webp"):
            webp_file_path = os.path.join(current_directory, filename)
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_file_path = os.path.join(current_directory, png_filename)

            # Open the WebP image and convert to PNG
            with Image.open(webp_file_path) as img:
                img.save(png_file_path, "PNG")
                print(f"Converted {filename} to {png_filename}")

if __name__ == "__main__":
    convert_webp_to_png()
