Here is a well-formatted `README.md` file for your GitHub repository:

```markdown
# Image to WebP Converter

This Python script converts images (JPEG, PNG, and GIF, including animated GIFs) to WebP format. It includes options for recursive directory processing and for deleting the original images after successful conversion.

## Features

- Converts images in the specified directory to WebP format.
- Processes JPEG, PNG, and GIF (including animated GIFs).
- Supports recursive processing of directories with the `-r` or `--recursive` flag.
- Deletes original files after successful conversion with the `-d` or `--delete` flag.

## Requirements

- Python 3.6 or higher
- Required libraries:
  - `Pillow`
  - `imageio`

You can install the required libraries with:

```bash
pip install Pillow imageio
```

## Usage

Run the script from the command line as follows:

```bash
python image_to_webp.py <directory_path> [options]
```

### Arguments

- `<directory_path>`: Path to the directory containing the images to convert.

### Options

- `-r`, `--recursive`: Process the specified directory and all its subdirectories.
- `-d`, `--delete`: Delete the original files after successful conversion. If used, the converted WebP files will be saved in the same directory as the original images (no `converted_webp` folder will be created).

### Examples

1. Convert images in the current directory:

   ```bash
   python image_to_webp.py ./images
   ```

2. Convert images in a directory and its subdirectories:

   ```bash
   python image_to_webp.py ./images -r
   ```

3. Convert images and delete the original files:

   ```bash
   python image_to_webp.py ./images -d
   ```

4. Convert images recursively and delete the original files:

   ```bash
   python image_to_webp.py ./images -r -d
   ```
