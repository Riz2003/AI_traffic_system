from ultralytics import YOLO
import sqlite3
from datetime import datetime

model = YOLO("yolov8n.pt")

conn = sqlite3.connect("database/traffic.db")
cursor = conn.cursor()

vehicle_classes = [
    "car",
    "truck",
    "bus",
    "motorcycle",
    "bicycle"
]

results = model("images/test.jpg")

for result in results:

    boxes = result.boxes

    for box in boxes:

        class_id = int(box.cls[0])

        vehicle_name = model.names[class_id]

        confidence = float(box.conf[0])

        if vehicle_name in vehicle_classes:

            current_date = datetime.now().strftime("%d-%m-%Y")
            current_time = datetime.now().strftime("%H:%M:%S")

            cursor.execute("""
            INSERT INTO vehicle_log
            (vehicle_type, confidence, date, time)
            VALUES (?, ?, ?, ?)
            """,
            (
                vehicle_name,
                confidence,
                current_date,
                current_time
            ))

            print(f"{vehicle_name} saved")

conn.commit()
conn.close()

print("Vehicle Detection Completed")