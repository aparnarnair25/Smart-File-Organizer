import os
import shutil
from datetime import datetime

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"]
}

folder_path = input("Enter folder path: ")

os.makedirs("logs", exist_ok=True)

log_file = "logs/activity_log.txt"

if os.path.exists(folder_path):

    files = os.listdir(folder_path)
    total_files = len(files)
    processed = 0  

    print("\nOrganizing files...\n")

    with open(log_file, "a") as log:

        log.write(f"\n--- {datetime.now()} ---\n")

        for file in files:

            full_path = os.path.join(folder_path, file)

            if os.path.isfile(full_path):

                filename, extension = os.path.splitext(file)

                category = "Others"

                for folder, extensions in FILE_TYPES.items():

                    if extension.lower() in extensions:
                        category = folder
                        break

                new_folder = os.path.join(folder_path, category)

                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)

                destination = os.path.join(new_folder, file)

                counter = 1

                while os.path.exists(destination):

                   filename, extension = os.path.splitext(file)

                   new_name = f"{filename}_{counter}{extension}"

                   destination = os.path.join(new_folder, new_name)

                   counter += 1

                shutil.move(full_path, destination)

                message = f"Moved {file} → {category}"

                print(message)
                processed += 1

                progress = int((processed / total_files) * 10)

                bar = "█" * progress + "░" * (10 - progress)

                percent = int((processed / total_files) * 100)

                print(f"[{bar}] {percent}%")
                log.write(message + "\n")

else:
    print("Folder not found")