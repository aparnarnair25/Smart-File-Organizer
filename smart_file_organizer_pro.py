import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.geometry("1400x800")
app.title("Smart File Organizer Pro")

# ========= SIDEBAR =========

sidebar = ctk.CTkFrame(
    app,
    width=250,
    corner_radius=0
)

sidebar.pack(
    side="left",
    fill="y"
)

title = ctk.CTkLabel(
    sidebar,
    text="Smart File Organizer",
    font=("Arial",22,"bold")
)

title.pack(pady=30)

buttons = [
    "📊 Dashboard",
    "📁 Organize",
    "📜 Logs",
    "⚙ Settings"
]

for item in buttons:

    btn = ctk.CTkButton(
        sidebar,
        text=item,
        width=200,
        height=45
    )

    btn.pack(
        pady=10
    )

# ========= MAIN CONTENT =========

main = ctk.CTkFrame(
    app
)

main.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

heading = ctk.CTkLabel(
    main,
    text="Folder Overview",
    font=("Arial",28,"bold")
)

heading.pack(
    anchor="w",
    pady=20
)

cards_frame = ctk.CTkFrame(
    main,
    fg_color="transparent"
)

cards_frame.pack()

categories = [
    "🖼 Images",
    "📄 Documents",
    "🎵 Music",
    "🎬 Videos"
]

for i,text in enumerate(categories):

    card = ctk.CTkFrame(
        cards_frame,
        width=180,
        height=120
    )

    card.grid(
        row=0,
        column=i,
        padx=15
    )

    label = ctk.CTkLabel(
        card,
        text=text,
        font=("Arial",18)
    )

    label.pack(
        pady=15
    )

    count = ctk.CTkLabel(
        card,
        text="0 files",
        font=("Arial",16)
    )

    count.pack()

# ========= ACTION PANEL =========

action_frame = ctk.CTkFrame(
    main
)

action_frame.pack(
    fill="x",
    pady=40
)

select_btn = ctk.CTkButton(
    action_frame,
    text="Select Folder"
)

select_btn.pack(
    side="left",
    padx=20,
    pady=20
)

organize_btn = ctk.CTkButton(
    action_frame,
    text="Organize Files"
)

organize_btn.pack(
    side="left"
)

progress = ctk.CTkProgressBar(
    main,
    width=600
)

progress.pack(
    pady=30
)

progress.set(0.3)

app.mainloop()
