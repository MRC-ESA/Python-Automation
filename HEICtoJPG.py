import os
import pyheif
from PIL import Image

def convert_heic_to_jpg(heic_path, jpg_path):
    # Read HEIC file
    heif_file = pyheif.read(heic_path)

    # Convert to PIL image
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )

    # Save as JPG
    image.save(jpg_path, "JPEG")

def convert_all_heic_in_directory(directory):
    # List all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a HEIC file
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(directory, filename)
            jpg_path = os.path.join(directory, filename[:-5] + ".jpg") # Change extension to .jpg
            convert_heic_to_jpg(heic_path, jpg_path)
            print(f"Converted '{heic_path}' to '{jpg_path}'")

# Example usage - replace 'path/to/directory' with your directory path
convert_all_heic_in_directory("path/to/directory")
