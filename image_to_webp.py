import os
import sys
from PIL import Image
import imageio
import argparse

def create_output_directory(base_path):
    """Creates a directory for the output WebP files."""
    output_dir = os.path.join(base_path, "converted_webp")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    return output_dir

def copy_file_metadata(input_path, output_path):
    """Copies file metadata (timestamps) from input to output."""
    try:
        # Get timestamps from the input file
        stat_info = os.stat(input_path)
        # Apply timestamps to the output file
        os.utime(output_path, (stat_info.st_atime, stat_info.st_mtime))
    except Exception as e:
        print(f"Error copying metadata from {input_path} to {output_path}: {e}")

def convert_image_to_webp(input_path, output_path):
    """Converts an image to WebP format."""
    try:
        with Image.open(input_path) as img:
            img.save(output_path, format="WEBP", quality=85)
            print(f"Image converted: {input_path} -> {output_path}")
            # Copy metadata
            copy_file_metadata(input_path, output_path)
    except Exception as e:
        print(f"Error converting {input_path}: {e}")
        return False
    return True

def convert_gif_to_webp(input_path, output_path):
    """Converts an animated GIF to WebP format while preserving animation."""
    try:
        gif = imageio.mimread(input_path)
        imageio.mimsave(output_path, gif, format="webp", loop=0, fps=10)
        print(f"Animated GIF converted: {input_path} -> {output_path}")
        # Copy metadata
        copy_file_metadata(input_path, output_path)
    except Exception as e:
        print(f"Error converting GIF {input_path}: {e}")
        return False
    return True

def find_unprocessed_files(original_dir, converted_dir):
    """Finds files in the original directory that have not been converted."""
    supported_formats = {"jpg", "jpeg", "png", "gif"}
    original_files = {
        os.path.splitext(file)[0]
        for file in os.listdir(original_dir)
        if os.path.isfile(os.path.join(original_dir, file)) and file.lower().split(".")[-1] in supported_formats
    }

    converted_files = {
        os.path.splitext(file)[0]
        for file in os.listdir(converted_dir)
        if os.path.isfile(os.path.join(converted_dir, file))
    }

    return original_files - converted_files

def process_files(input_dir, delete_after_conversion=False):
    """Processes images and GIFs in the specified directory."""
    supported_formats = {"jpg", "jpeg", "png", "gif"}

    # Check if there are supported files in the directory
    has_supported_files = any(
        file.lower().split(".")[-1] in supported_formats
        for file in os.listdir(input_dir)
        if os.path.isfile(os.path.join(input_dir, file))
    )

    if not has_supported_files:
        return  # Skip directory if no supported files

    output_dir = None if delete_after_conversion else create_output_directory(input_dir)

    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        ext = file_name.lower().split(".")[-1]

        if ext in supported_formats:
            output_file = os.path.join(input_dir if delete_after_conversion else output_dir, os.path.splitext(file_name)[0] + ".webp")

            # Skip if the file is already converted
            if os.path.exists(output_file):
                continue

            try:
                if ext == "gif":
                    converted = convert_gif_to_webp(file_path, output_file)
                else:
                    converted = convert_image_to_webp(file_path, output_file)

                if converted and delete_after_conversion:
                    os.remove(file_path)
                    print(f"Original file deleted: {file_path}")

                if not converted:
                    print(f"Failed to convert: {file_name}")

            except KeyboardInterrupt:
                print("Process interrupted by user.")
                sys.exit(0)

    # Log unprocessed files if not deleting originals
    if not delete_after_conversion:
        unprocessed_files = find_unprocessed_files(input_dir, output_dir)
        if unprocessed_files:
            print("The following files could not be converted:")
            for file in unprocessed_files:
                print(file)
        else:
            print("All supported files have been processed.")

def process_directory_recursively(input_dir, delete_after_conversion=False):
    """Processes files in the directory and all its subdirectories."""
    for root, _, _ in os.walk(input_dir):
        print(f"Processing directory: {root}")
        process_files(root, delete_after_conversion=delete_after_conversion)

def main():
    parser = argparse.ArgumentParser(description="Convert images to WebP format.")
    parser.add_argument("directory", type=str, help="Path to the directory containing images.")
    parser.add_argument("-r", "--recursive", action="store_true", help="Process directories recursively.")
    parser.add_argument("-d", "--delete", action="store_true", help="Delete original images after successful conversion.")

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: The specified path is not a valid directory: {args.directory}")
        sys.exit(1)

    try:
        if args.recursive:
            process_directory_recursively(args.directory, delete_after_conversion=args.delete)
        else:
            process_files(args.directory, delete_after_conversion=args.delete)

    except KeyboardInterrupt:
        print("Process interrupted by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
