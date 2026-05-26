import customtkinter as ctk
from tkinter import filedialog
import os
import shutil
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"]
}

def select_folder():
    folder = filedialog.askdirectory()

    if folder:
        folder_label.configure(text=folder)

def organize_files():

    folder_path = folder_label.cget("text")

    if folder_path == "No folder selected":
        status_label.configure(
            text="Please select a folder"
        )
        return

    os.makedirs("logs", exist_ok=True)

    log_file = "logs/activity_log.txt"

    files = os.listdir(folder_path)
    total_files = len(files)
    processed = 0

    moved_count = 0

    stats = {
        "Images": 0,
        "Documents": 0,
        "Videos": 0,
        "Music": 0,
        "Others": 0
    }

    with open(log_file, "a", encoding="utf-8") as log:

        log.write(f"\n--- {datetime.now()} ---\n")

        for file in files:

            full_path = os.path.join(
                folder_path,
                file
            )

            if os.path.isfile(full_path):

                filename, extension = os.path.splitext(file)

                category = "Others"

                for folder, extensions in FILE_TYPES.items():

                    if extension.lower() in extensions:
                        category = folder
                        break

                new_folder = os.path.join(
                    folder_path,
                    category
                )

                os.makedirs(
                    new_folder,
                    exist_ok=True
                )

                destination = os.path.join(
                    new_folder,
                    file
                )

                counter = 1

                while os.path.exists(destination):

                    new_name = (
                        f"{filename}_{counter}{extension}"
                    )

                    destination = os.path.join(
                        new_folder,
                        new_name
                    )

                    counter += 1

                shutil.move(
                    full_path,
                    destination
                )

                log.write(
                    f"Moved {file} to {category}\n"
                )

                moved_count += 1
                processed += 1

                progress_bar.set(
                    processed / total_files
                )

                app.update()

                stats[category] += 1

    status_label.configure(
        text=f"Done! {moved_count} files organized"
    )

    stats_label.configure(
        text=
        f"Images: {stats['Images']}\n"
        f"Documents: {stats['Documents']}\n"
        f"Videos: {stats['Videos']}\n"
        f"Music: {stats['Music']}\n"
        f"Others: {stats['Others']}"
    )


app = ctk.CTk()

app.geometry("700x500")

app.title(
    "Smart File Organizer Pro"
)

title = ctk.CTkLabel(
    app,
    text="Smart File Organizer Pro",
    font=("Arial",25,"bold")
)

title.pack(pady=20)

folder_label = ctk.CTkLabel(
    app,
    text="No folder selected"
)

folder_label.pack()

select_button = ctk.CTkButton(
    app,
    text="Select Folder",
    command=select_folder
)

select_button.pack(pady=10)

organize_button = ctk.CTkButton(
    app,
    text="Organize Files",
    command=organize_files
)

organize_button.pack(pady=10)

status_label = ctk.CTkLabel(
    app,
    text=""
)

status_label.pack(pady=10)

stats_label = ctk.CTkLabel(
    app,
    text="No statistics yet",
    font=("Arial",14)
)

stats_label.pack(pady=20)

progress_bar = ctk.CTkProgressBar(app)

progress_bar.pack(pady=10)

progress_bar.set(0)
app.mainloop()