import os
import shutil

categories = {
    "jpg": "Images",
    "png": "Images",
    "pdf": "Documents",
    "docx": "Documents",
    "txt": "Documents",
    "mp3": "Audio",
    "wav": "Audio"
}

folder = input("Enter folder path: ")

for file in os.listdir(folder):

    file_path = os.path.join(folder, file)

    if os.path.isfile(file_path):

        extension = file.split(".")[-1].lower()

        if extension in categories:

            target = os.path.join(folder,
                                  categories[extension])

            os.makedirs(target, exist_ok=True)

            shutil.move(file_path,
                        os.path.join(target, file))

print("Organisation complete!")


