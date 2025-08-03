# 🖐️ Gesture-Based Mouse Control Web App

This is a real-time hand gesture recognition system that allows users to control their mouse cursor using gestures detected from a webcam. Built using **Flask**, **OpenCV**, and **Pynput**, it detects hand movement, translates it into screen coordinates, and performs actions like mouse movement and clicking.

---
## 🔍 Features

- Tracks hand gestures in real-time via webcam
- Moves mouse cursor based on hand position
- Performs click gesture based on hand height
- Simple Flask interface to start and stop gesture recognition

---
## 🧠 How It Works
-Uses HSV color filtering to isolate hand gestures
-Maps centroid of hand to screen resolution using numpy.interp
-Performs mouse click when hand is near the top of the frame
-Mouse actions handled via pynput.mouse.Controller

---
## 🧩 Requirements
-Python 3.7+
-Webcam

---
## Libraries:
-Flask
-OpenCV
-NumPy
-Pynput

---

## 🔧 Future Enhancements
-Enhance gesture detection accuracy using custom-trained deep learning models
-Add multi-language speech feedback for accessibility
-Implement AI-powered gesture classification for more complex commands (e.g., drag, zoom)
-Add a GUI dashboard to configure gesture sensitivity and control actions
-Deploy as a standalone desktop app using PyInstaller or Electron-Python bridge

---

