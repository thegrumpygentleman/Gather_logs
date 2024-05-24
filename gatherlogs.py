import os
import shutil

# Get the current directory
current_dir = os.getcwd()

def get_unique_filename(directory, filename):
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base}_{counter}{extension}"
        counter += 1
    return new_filename

# Walk through all subdirectories
for root, dirs, files in os.walk(current_dir):
    for file in files:
        if file.endswith(".log"):
            # Construct the full file path
            file_path = os.path.join(root, file)
            # Get a unique filename to avoid overwriting
            unique_filename = get_unique_filename(current_dir, file)
            # Move the file to the current directory with the unique filename
            shutil.move(file_path, os.path.join(current_dir, unique_filename))
            print(f"Moved: {file_path} to {os.path.join(current_dir, unique_filename)}")
