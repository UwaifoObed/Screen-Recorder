# 🎥 Screen Recorder (Python + Tkinter + ttkbootstrap)

## 📌 Description

A beautiful, modern **GUI-based screen recorder** built with Python, using `Tkinter` and `ttkbootstrap` for styling. This tool allows users to:
- Start and stop screen recording
- Choose FPS (30, 60, 120)
- Select the destination folder to save recordings
- Track elapsed time during recording
- Switch between light and dark themes using a built-in theme selector

---

## 🖥 Features

✅ Modern user interface using `ttkbootstrap`  
✅ Light, Dark, and Custom themes  
✅ Elapsed recording timer  
✅ FPS selector (30/60/120 FPS)  
✅ Choose save folder via dialog  
✅ Saves recording as `.mp4` using `pyautogui` and `opencv`  
✅ Clean architecture using functions and modular design

---

## 🚀 How to Run

1. **Clone the repo**:
   ```bash
   git clone https://github.com/Uwaifoobed/screen-recorder.git
   cd screen-recorder
   ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the GUI**:
   ```bash
   python gui.py
   ```

---

## 📂 Project Structure

```
📁 screen-recorder/
├── gui.py                  # Main GUI logic
├── screen_recorder.py      # Recording logic (OpenCV + pyautogui)
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files/folders
└── README.md               # Project documentation
```

---

## 🧩 Dependencies

- `ttkbootstrap`
- `pyautogui`
- `opencv-python`
- `numpy`

Install them using:

```bash
pip install -r requirements.txt
```

---

## 📷 Sample Screenshot

![Screen Recorder GUI](screenshot.png)

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Author

Developed by **Uwaifo Obed**  
Feel free to connect or contribute!