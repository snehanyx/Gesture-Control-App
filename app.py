# app.py
from flask import Flask, render_template, jsonify
import threading
import cv2
import numpy as np
from pynput.mouse import Controller, Button
import time

app = Flask(__name__)
mouse = Controller()
capture_thread = None
running = False

screen_w, screen_h = 1920, 1080  # Change based on your resolution


def get_max_contour(contours, min_area=1000):
    max_c = None
    max_area = min_area
    for c in contours:
        area = cv2.contourArea(c)
        if area > max_area:
            max_area = area
            max_c = c
    return max_c

def gesture_control():
    global running
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    click_cooldown = 1
    last_click_time = 0

    while running:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower = np.array([0, 30, 60])
        upper = np.array([20, 150, 255])
        mask = cv2.inRange(hsv, lower, upper)
        mask = cv2.GaussianBlur(mask, (5, 5), 0)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnt = get_max_contour(contours)

        if cnt is not None:
            x, y, w, h = cv2.boundingRect(cnt)
            cx = x + w // 2
            cy = y + h // 2

            screen_x = np.interp(cx, [0, 640], [0, screen_w])
            screen_y = np.interp(cy, [0, 480], [0, screen_h])
            mouse.position = (screen_x, screen_y)

            if cy < 100 and time.time() - last_click_time > click_cooldown:
                mouse.click(Button.left, 1)
                last_click_time = time.time()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    global running, capture_thread
    if not running:
        running = True
        capture_thread = threading.Thread(target=gesture_control)
        capture_thread.start()
    return jsonify({"status": "started"})

@app.route('/stop')
def stop():
    global running
    running = False
    return jsonify({"status": "stopped"})

if __name__ == '__main__':
    app.run(debug=True)
