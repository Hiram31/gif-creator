#!/usr/bin/env python3

from PIL import Image
import os

def get_image_files(folder_path, prefix=None):
    """
    Method to get all image files from a folder that end with "_0X".
        
        :param folder_path: Path to the folder containing the images.
        :return: List of image files.
    """
    valid_extensions = ('.png', '.jpg', '.jpeg')

    return [
        os.path.join(folder_path, f)
        for f in sorted(os.listdir(folder_path))
        if os.path.isfile(os.path.join(folder_path, f))
        and f.lower().endswith(valid_extensions)
        and f.lower().rsplit('.', 1)[0].startswith(prefix)  # Ensuring the filename (without extension)"
    ]


def create_gif_from_folder(folder_path, output_gif_path, prefix=None, duration=100, resize_ratio=0.5):
    """
    Method to create a GIF from all images in a folder.
            
            :param folder_path: Path to the folder containing the images.
            :param output_gif_path: Path to the output GIF file.
            :param duration: Duration of each frame in the GIF.
            :return: None
    """
    
    # Get all image files from the folder using the optimized function
    image_files = get_image_files(folder_path, prefix)

    # Initialize list to store opened images
    images = []

    # Open all images using Pillow, optionally resize them, and handle any errors
    for image_path in image_files:
        try:
            img = Image.open(image_path)
            new_dimensions = (int(img.width * resize_ratio), int(img.height * resize_ratio))
            img_resized = img.resize(new_dimensions, Image.LANCZOS)
            images.append(img_resized)
        except IOError:
            print(f"Skipping corrupted or unsupported file: {image_path}")

    if not images:
        print("No valid images found to create a GIF.")
        return

    # Save as a GIF
    images[0].save(
        output_gif_path,
        save_all=True,
        append_images=images[1:],
        optimize=True,
        duration=duration,
        loop=0
    )

if __name__ == "__main__":
    folder_path = "/PATH/"  # Replace with your folder path
    prefix = 'prefix'  # Define the prefix variable
    output_gif = "output/result.gif"  # Desired GIF file name with prefix
    print(f"\nCreating GIF from images in folder: {folder_path}")
    create_gif_from_folder(folder_path, output_gif, prefix=prefix, duration=100, resize_ratio=0.2)  # Use the prefix variable here
    print(f"\nDone! {output_gif}\n")
