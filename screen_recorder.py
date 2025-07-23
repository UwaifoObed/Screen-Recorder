import datetime
import os
import pyautogui
import subprocess

process = None # Global variable to hold the ffmpeg process
output_file = None

def start_recording(fps=30, folder_path="."):
    global process, output_file

    # Output filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(folder_path, f"screen_recording_{timestamp}.mp4")

    # Screen resolution
    screen_size = pyautogui.size()

    # ffmpeg command
    ffmpeg_command = [
        r"C:\ffmpeg\bin\ffmpeg.exe",
        "-y", # Overwrite output file if exists

        # Video input (screen capture)
        "-f", "gdigrab", # Windows screen capture
        "-framerate", str(fps),
        "-video_size", f"{screen_size.width}x{screen_size.height}",
        "-i", "desktop", # Capture entire screen

        # Audio input (microphone)
        "-f", "dshow", # For capturing audio
        "-i", "audio=Mixage stéréo (Realtek(R) Audio)",

        # Encoding options
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "128k",

        # Fix for early termination
        "-movflags", "+faststart",

        # Output file
        output_file
    ]

    try:
        process = subprocess.Popen(ffmpeg_command, stdin=subprocess.PIPE)
        print("Recording started.")
    except Exception as e:
        print(f"Failed to start recording: {e}")

def stop_recording():
    global process
    if process and process.poll() is None:
        process.communicate(input=b'q')
        print(f"Recording stopped. File saved as {output_file}")
        process = None