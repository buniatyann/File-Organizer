import os
import shutil
from datetime import datetime

def categorize_file(path_to_file):
    _, extension = os.path.splitext(path_to_file)
    
    categories = {
        "Web": [".html", ".html5", ".htm", ".xhtml"],
        "Picture": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"],
        "Video": [".avi", ".mkv", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
        "Document": [".oxps", ".epub", ".pages", ".docx", ".txt", ".pdf", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn",
                     ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Compressed": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
        "Audio": [".aac", ".aa", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
        "Programming": [".cpp", ".c", ".java", ".py", ".js", ".go", ".swift", ".rs"],
        "Other": []  # category if not found
    }

    for category, extensions in categories.items():
        if extension.lower() in extensions:
            return category
    
    return "Other"  # Default category

def create_folders(target_directory):
    categories = ["Picture", "Document", "Video", "Audio", "Web", "Compressed", "Programming", "Other"]
   
    for category in categories:
        os.makedirs(os.path.join(target_directory, category), exist_ok=True)

def move_and_rename_file(file_path, target_directory):
    file_name = os.path.basename(file_path)
    file_category = categorize_file(file_name)
    target_path = os.path.join(target_directory, file_category, file_name)
    
    try:
        if os.path.exists(target_path):
            base_name, ext = os.path.splitext(file_name)
            counter = 1
            
            while os.path.exists(target_path):
                new_name = f"{base_name}_{counter}{ext}"
                target_path = os.path.join(target_directory, file_category, new_name)
                counter += 1

        shutil.copy2(file_path, target_path)

        file_date = datetime.fromtimestamp(os.path.getmtime(file_path))
        new_file_name = f"{file_date.isoformat()}-{file_name}"
        os.rename(target_path, os.path.join(os.path.dirname(target_path), new_file_name))

    except PermissionError as e:
        print(f"Permission error with file '{file_path}': {e}")
    except FileNotFoundError as e:
        print(f"File not found '{file_path}': {e}")
    except OSError as e:
        print(f"OS error moving '{file_path}': {e}")
    except Exception as e:
        print(f"Unexpected error with file '{file_path}': {e}")

def file_sort(source_directory, target_directory):
    """Sorts and moves files from source to target based on categories."""
    for root, _, files in os.walk(source_directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            move_and_rename_file(file_path, target_directory)

def main():
    source_directory = input("Enter source directory: ")
    target_directory = input("Enter target directory: ")

    # Create category folders in the target directory
    create_folders(target_directory)

    # Sort and move files
    file_sort(source_directory, target_directory)

    print("Action completed!")

if __name__ == "__main__":
    main()
