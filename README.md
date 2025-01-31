# Image to WebP Converter

A Python script to convert images (JPG, PNG, GIF) to WebP format, with support for batch processing and optional deletion of original files.

## Features

- Converts JPG, PNG, and GIF images to WebP format.
- Supports animated GIF to WebP conversion using `ffmpeg`.
- Recursive directory processing for batch conversions.
- Option to delete original files after successful conversion.
- Preserves file metadata (timestamps) during conversion.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/image_to_webp.git
   cd image_to_webp
   ```

2. Install dependencies:
   ```bash
   pip install .
   ```

3. Ensure `ffmpeg` is installed for GIF conversion:
   - On Ubuntu/Debian/Linux Mint:
     ```bash
     sudo apt install ffmpeg
     ```
   - On Arch Linux
     ```bash
     sudo pacman -S ffmpeg
     ```
   - On Fedora
     ```bash
     sudo dnf install ffmpeg
     ```

## Usage

Run the script from the command line:

```bash
python -m image_to_webp /path/to/images [options]
```

### Options

- `-r`, `--recursive`: Process directories recursively.
- `-d`, `--delete`: Delete original files after successful conversion.

### Example

Convert all images in a directory (non-recursive):
```bash
python -m image_to_webp /path/to/images
```

Convert all images recursively and delete originals:
```bash
python -m image_to_webp /path/to/images -r -d
```

## License

This project is licensed under the **GNU General Public License v2 (GPL-2.0)**. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
