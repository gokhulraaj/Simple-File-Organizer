# File Organizer Script

This Python script helps organize files in a directory by moving them into folders based on their file types and extensions. It also logs the details of each file move operation.

## Features

- Organizes files into folders based on their MIME type or file extension.
- Creates a log file recording the source and destination of each moved file.
- Handles various file types with predefined folder names and structures.

## Requirements

- Python 3.x
- Required Python libraries:
  - `shutil`
  - `os`
  - `datetime`
  - `sys`
  - `logging`
  - `mimetypes`
  - `filetype` (optional, if additional file type detection is needed)

## Usage

1. **Prepare Your Environment**:
   - Ensure Python 3.x is installed.
   - Install the required Python libraries if they are not already available. You can install the optional `filetype` library using pip if needed:
     ```bash
     pip install filetype
     ```

2. **Run the Script**:
   - The script requires a directory path as a command-line argument. You can run the script using the following command:
     ```bash
     python file_organizer.py /path/to/your/directory
     ```
   - Replace `/path/to/your/directory` with the path to the directory you want to organize.

## How It Works

1. **File Type Detection**:
   - The script determines the type of each file based on its MIME type or extension.
   - Files are moved into folders named according to their MIME type or file extension.

2. **Folder Organization**:
   - Predefined folder names are used for common file types (e.g., `TEXT/HTML`, `APPLICATION/MSWORD`).
   - Files with unknown MIME types or extensions are placed in "OTHER FILES" folders.
   - Blank files (files with no extension) are moved to a `BLANK FILES/` folder.

3. **Logging**:
   - A log file named `Move Records.log` is created in the `LOGS` folder within the specified directory.
   - The log file records the source and destination paths of each moved file along with the timestamp of the operation.

## Example

To organize files in a directory located at `C:/Users/ASUS/Documents/CodeRep/FileOrganizer/`, run:

```bash
python file_organizer.py C:/Users/ASUS/Documents/CodeRep/FileOrganizer/
