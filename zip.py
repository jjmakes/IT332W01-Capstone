import zipfile
import os
from datetime import datetime


def zip_directory():
    # Get the current working directory where the script is ran
    root_path = os.getcwd()

    # Create a zip file with the current working directory name
    current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    zip_path = os.path.join(root_path, os.path.basename(
        root_path) + '-' + current_time + '.zip')

    # Get the list of files in the current working directory
    files = os.listdir(root_path)

    # Exclude files from being included in the archive
    exclude = [".env", "zip.py", "main.py",
               "aws.py", "requirements.txt",
               "README.md", ".gitignore"]
    files = [file for file in files if file not in exclude]

    # Zip all directories and files in the current working directory
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(root_path):
            if os.path.basename(root) != '__pycache__':
                for dirname in dirs:
                    # construct the full local path for the directory
                    local_path = os.path.join(root, dirname)
                    # Skip the current zip file
                    if local_path == zip_path:
                        continue
                # construct the relative path
                rel_path = os.path.relpath(local_path, root_path)
                # add the directory to the zip archive
                zipf.write(local_path, rel_path)
                print(f'Zipped {local_path} as {rel_path}')
            for filename in files:
                if filename not in exclude:
                    local_path = os.path.join(root, filename)
                    # construct the relative path
                    rel_path = os.path.relpath(local_path, root_path)
                    # Skip the current zip file
                    if local_path == zip_path:
                        continue
                    # add the file to the zip archive
                    zipf.write(local_path, rel_path, zipfile.ZIP_STORED)
                    print(f'Zipped {local_path} as {rel_path}')

    return zip_path
