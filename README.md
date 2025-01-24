# Image to WebP Converter

A Python script for converting images (JPEG, PNG, and GIF, including animated GIFs) to the WebP format. This tool supports recursive directory processing and offers an option to delete original files after conversion.

---

## Prerequisites

Before using this script, ensure you have the following:

- **Python 3.6 or higher** installed on your system.
- Required Python libraries:
  - `Pillow`
  - `imageio`

You can install the necessary libraries using:

```bash
pip install Pillow imageio
```

Alternatively, you can install the libraries from a requirements file:

```bash
pip install -r requirements.txt
```

---

## Installation

Clone or download this repository to your local machine:

```bash
git clone https://github.com/rv-arteaga/image_to_webp.git
cd image_to_webp
```

---

## Usage

### Basic Usage

Run the script from the command line to convert images in a specified directory to WebP format:

```bash
python image_to_webp.py <directory_path> [options]
```

### Options

- `-r`, `--recursive`: Process the specified directory and all its subdirectories.
- `-d`, `--delete`: Delete the original files after successful conversion. Converted files will remain in the same directory (no `converted_webp` folder is created).

---

## Example Commands

1. **Convert images in a directory** (non-recursive):

   ```bash
   python image_to_webp.py ./images
   ```

2. **Convert images in a directory and its subdirectories**:

   ```bash
   python image_to_webp.py ./images -r
   ```

3. **Convert images and delete the original files**:

   ```bash
   python image_to_webp.py ./images -d
   ```

4. **Convert images recursively and delete the original files**:

   ```bash
   python image_to_webp.py ./images -r -d
   ```

---

## License

This project is licensed under the GNU General Public License v2. See the [LICENSE](LICENSE) file for details.

---
