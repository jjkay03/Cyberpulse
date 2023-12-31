# Cyberpulse utility module by jjkay03

from .logger import log  # Cyberpulse modules
import os

# Function: Deletes all files inside a dir
def clear_dir(directory, ignored_files=[]):

    ignored_files.append(".gitkeep")  # Ensure .gitkeep is always ignored
    
    try:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            # Check if the file is not in the ignored_files list and it's a regular file
            if filename not in ignored_files and os.path.isfile(file_path):
                os.remove(file_path)
        
        log(f"Deleted all files from dir: '{directory}'", debug=True)
    
    except Exception as e:
        print(f"An error occurred: {e}")