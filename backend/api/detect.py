from flask import Blueprint, jsonify
from ultralytics import YOLO
import cv2

# Create Blueprint
detect_api = Blueprint("detect_api", __name__)

# Load YOLO Model
model = YOLO("models/yolov8n.pt")

# Open Camera
camera = cv2.VideoCapture(0)

# Generate Frames
def generate_frames():

    while True:

        success, frame = camera.read()

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

# Test API
@detect_api.route("/detect", methods=["GET"])
def detect():

    return jsonify({
        "status": "success",
        "message": "YOLO Detection API Working"
    })

