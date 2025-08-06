# 🧹 Desktop Cleaner 

A simple Python script that automatically organizes files in a folder by grouping them into subfolders based on their file extensions.

---

## 🚀 Features

- **Automatic Organization**: Sorts files into folders based on their file extensions (e.g., PDF Files, JPG Files, TXT Files)
- **Duplicate Handling**: Automatically renames duplicate files by adding a counter (e.g., `document (1).pdf`)
- **Hidden File Protection**: Handles hidden files (starting with `.`) by placing them in an "Other Files" folder
- **Safe File Operations**: Uses `shutil.move()` for reliable file operations
- **Detailed Logging**: Prints the movement of each file for transparency

---

## 🛠️ How It Works

The script scans the specified folder and:
1. Creates subfolders based on file extensions (e.g., "PDF Files", "JPG Files")
2. Moves files into their corresponding subfolders
3. Handles naming conflicts by adding numbers to duplicate filenames
4. Places files without extensions or hidden files into an "Other Files" folder

---

## Prerequisites

- Python 3.x
- No additional packages required (uses only built-in libraries)

---

## 📦 Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/desktop-cleaner.git
   cd desktop-cleaner
   ```

2. **Edit the folder path**:
   Open the script and modify this line to point to your desired folder:
   ```python
   folderPath=r"C:\Users\kanch\Downloads"  # Change this to your folder path
   ```

3. **Run the script**:
   ```bash
   python desktop_cleaner.py
   ```
---

## Example

**Before running the script:**
```
Downloads/
├── document.pdf
├── photo.jpg
├── music.mp3
├── presentation.pptx
└── script.py
```

**After running the script:**
```
Downloads/
├── PDF Files/
│   └── document.pdf
├── JPG Files/
│   └── photo.jpg
├── MP3 Files/
│   └── music.mp3
├── PPTX Files/
│   └── presentation.pptx
└── PY Files/
    └── script.py
```

---

## 🛠️ Configuration

To use the script with different folders, simply modify the `folderPath` variable:

```python
# For Windows
folderPath = r"C:\Users\YourUsername\Desktop"

# For macOS/Linux
folderPath = "/Users/YourUsername/Desktop"
```

---

## 🛟 Safety Features

- **Non-destructive**: Only moves files, never deletes them
- **Duplicate protection**: Automatically renames files to prevent overwrites
- **Path validation**: Checks if the specified folder exists before proceeding
- **File verification**: Ensures files are valid before attempting to move them

---

## 🗃️ Supported File Types

The script works with any file extension, including but not limited to:
- Documents: `.pdf`, `.docx`, `.txt`, `.xlsx`
- Images: `.jpg`, `.png`, `.gif`, `.bmp`
- Audio: `.mp3`, `.wav`, `.flac`
- Video: `.mp4`, `.avi`, `.mkv`
- Archives: `.zip`, `.rar`, `.7z`
- And many more!



