import os
import shutil
from pathlib import Path

# --- FOLDER MAP ---
# Keys = folder names to create, Values = file extensions that belong there
FOLDER_MAP = {
    "Images":    [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos":    [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
    "Audio":     [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Code":      [".py", ".js", ".html", ".css", ".json", ".ts", ".java"],
    "Archives":  [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Others":    []  # catch-all for anything not matched above
}
def get_destination(extension):
    """Given a file extension, return the folder it belongs in."""
    for folder, extensions in FOLDER_MAP.items():
        if extension.lower() in extensions:
            return folder
    return "Others"  # nothing matched, goes to catch-all
def organize_folder(folder_path):
    """Scan a folder and move files into subfolders by type."""
    folder = Path(folder_path)
    
    # Make sure the folder actually exists
    if not folder.exists():
        print(f"Folder not found: {folder_path}")
        return

    for file in folder.iterdir():
        # Skip subfolders, only process files
        if not file.is_file():
            continue

        # Get the file's extension and find its destination
        extension = file.suffix
        destination_folder = get_destination(extension)

        # Create the destination folder if it doesn't exist yet
        destination_path = folder / destination_folder
        destination_path.mkdir(exist_ok=True)

        # Move the file!
        shutil.move(str(file), str(destination_path / file.name))
        print(f"Moved: {file.name} → {destination_folder}")
        # --- MAIN ---
if __name__ == "__main__":
    folder_to_organize = input("Enter the full path of the folder you want to organize: ")
    organize_folder(folder_to_organize)
    print("Done! Your folder is organized! 🎉")

        