# File Organizer Script

## Description
This Python script organizes files from a source directory into categorized folders in a target directory based on their file types. It also handles duplicate files by renaming them and appending timestamps to their names.

## Features
- **Automatic Categorization**: Files are categorized into folders such as `Picture`, `Document`, `Video`, `Audio`, `Web`, `Compressed`, `Programming`, and `Other`.
- **Duplicate Handling**: Automatically renames duplicate files by appending a counter to their name.
- **Timestamped Filenames**: Renames files in the target directory by appending their last modified timestamp.
- **Cross-Platform**: Works on Windows, Mac, and Linux.

## File Categories
- **Picture**: `.jpeg`, `.jpg`, `.png`, `.gif`, etc.
- **Document**: `.pdf`, `.docx`, `.txt`, etc.
- **Video**: `.mp4`, `.avi`, `.mkv`, etc.
- **Audio**: `.mp3`, `.wav`, `.aac`, etc.
- **Web**: `.html`, `.htm`, `.xhtml`, etc.
- **Compressed**: `.zip`, `.rar`, `.7z`, etc.
- **Programming**: `.py`, `.java`, `.cpp`, etc.
- **Other**: Any file type not listed above.

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/buniatyann/File-Organizer.git
2. Navigate to the project directory:
   ```bash
   cd file-organizer-script
3. Run the script:
   ```bash
   python file_organizer.py
4. Enter the source and target directories when prompted.

## Requirements
- Pyton 3.6 or above
- `shutil`, `os` and `datetime` modules (pre installed in Python)

## LICENSE
   This repository is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Constribution
   Feel free to fork the repository and submit pull requests for enhancements or bug fixes.
