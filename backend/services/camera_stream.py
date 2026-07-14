from ultralytics import YOLO
import cv2

model = YOLO("models/yolov8n.pt")

cap = cv2.VideoCapture(0)  # 0 = default webcam

def generate_frames():

    while True:

        success, frame = cap.read()

        if not success:
            break

        results = model(frame)

        annotated = results[0].plot()

        ret, buffer = cv2.imencode(".jpg", annotated)

        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            frame +
            b'\r\n'
        )