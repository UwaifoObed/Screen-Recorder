import threading
from tkinter import filedialog
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from screen_recorder import start_recording, stop_recording

# Create main window
root = tb.Window(themename="darkly")
root.title("🎥 Screen Recorder") # Set the window title
root.geometry("600x500") # Set width x height

recording_folder = ""
save_folder = "."
elapsed_seconds = 0
timer_running = False

# Title Label
title = tb.Label(
    root,
    text="Screen Recorder",
    font=("Helvetica", 18, "bold"))
title.pack(pady=20)

# FPS Dropdown
fps_label = tb.Label(
    root,
    text="Select FPS:",
    font=("Helvetica", 12))
fps_label.pack()

fps_var = tb.StringVar(value="30") # Default FPS
fps_dropdown = tb.Combobox(
    root,
    textvariable=fps_var,
    values=["30", "60", "120"],
    width=10,
    bootstyle="info")
fps_dropdown.pack(pady=10)

# Theme selector (Light/Dark mode or custom theme)
theme_label = tb.Label(
    root,
    text="Theme Selector",
    font=("Helvetica", 12))
theme_label.pack()

theme_mapping = {
    "Dark": "darkly",
    "Light": "flatly",
    "Superhero": "superhero",
    "Cosmo": "cosmo",
    "Morph": "morph"
}

theme_value = tb.StringVar(value="Dark")
theme_dropdown = tb.Combobox(
    root,
    textvariable=theme_value,
    values=list(theme_mapping.keys()),
    width=20,
    bootstyle="info")
theme_dropdown.pack(pady=10)

def change_theme(event=None):
    selected_label = theme_value.get()
    selected_theme = theme_mapping.get(selected_label)
    if selected_theme:
        root.style.theme_use(selected_theme)

theme_dropdown.bind("<<ComboboxSelected>>", change_theme)


# Create label to show selected folder
folder_label = tb.Label(
    root,
    text=f"Save Folder: {save_folder}")
folder_label.pack()

def choose_folder():
    global save_folder
    folder = filedialog.askdirectory()
    if folder:
        save_folder = folder
        folder_label.config(text=f"Save Folder: {save_folder}")
        print(f"Selected folder: {save_folder}")

# Create choose folder button
folder_button = tb.Button(
    root,
    text="Choose Save Folder",
    bootstyle="secondary",
    width=20,
    command=choose_folder)
folder_button.pack(pady=10)

# Function for start Button
def start_button_action():
    global elapsed_seconds, timer_running
    elapsed_seconds = 0
    timer_running = True
    update_timer()
    
    threading.Thread(
        target=start_recording,
        args=(int(fps_var.get()), save_folder),
        daemon=True
    ).start()

# Create a start button
start_button = tb.Button(
    root,
    text="Start Recording",
    bootstyle="success",
    width=20,
    command=start_button_action)
start_button.pack(pady=10)

# Function for stop Button
def stop_button_action():
    global timer_running
    stop_recording()
    timer_running = False
    elapsed_seconds = 0
    elapse_label.config(text="Elapsed Time: 00:00")

# Create stop recording button
stop_button = tb.Button(
    root,
    text="Stop Recording",
    bootstyle="danger", width=20,
    command=stop_button_action)
stop_button.pack(pady=10)

# Elapsed Timer
elapse_label = tb.Label(
    root,
    text="Elapsed Time: 00:00",
    font=("Helvetica", 12))
elapse_label.pack(pady=10)

def update_timer():
    global elapsed_seconds, timer_running
    if timer_running:
        minutes = elapsed_seconds // 60
        seconds = elapsed_seconds % 60
        elapse_label.config(text=f"Elapsed Time: {minutes:02}:{seconds:02}")
        elapsed_seconds += 1
        root.after(1000, update_timer)



# Run the GUI Loop
root.mainloop()