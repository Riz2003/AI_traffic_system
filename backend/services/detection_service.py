from ultralytics import YOLO
import cv2
from datetime import datetime

from database.db import get_connection
from database.history_db import save_vehicle

model = YOLO("models/yolov8n.pt")

# Prevent duplicate counting
counted_ids = set()


def generate_frames():

    cap = cv2.VideoCapture(0)
    # For video testing:
    # cap = cv2.VideoCapture("videos/traffic.mp4")

    while True:

        success, frame = cap.read()

        if not success:
            break

        # YOLO Tracking
        results = model.track(frame, persist=True)

        cars = 0
        bikes = 0
        buses = 0
        trucks = 0
        bicycles = 0

        if results[0].boxes.id is not None:

            boxes = results[0].boxes

            for box, track in zip(boxes, boxes.id):

                track_id = int(track)

                class_id = int(box.cls[0])

                confidence = float(box.conf[0])

                vehicle = model.names[class_id]

                if vehicle not in [
                    "car",
                    "motorcycle",
                    "bus",
                    "truck",
                    "bicycle"
                ]:
                    continue

                # Count each object only once
                if track_id not in counted_ids:

                    counted_ids.add(track_id)

                    now = datetime.now()

                    save_vehicle(
                        vehicle,
                        confidence,
                        "Camera 1",
                        track_id,
                        now.strftime("%Y-%m-%d"),
                        now.strftime("%H:%M:%S")
                    )

                # Live counts
                if vehicle == "car":
                    cars += 1

                elif vehicle == "motorcycle":
                    bikes += 1

                elif vehicle == "bus":
                    buses += 1

                elif vehicle == "truck":
                    trucks += 1

                elif vehicle == "bicycle":
                    bicycles += 1

        total = cars + bikes + buses + trucks + bicycles

        # Update dashboard table
        conn = get_connection()

        cursor = conn.cursor()

        now = datetime.now()

        cursor.execute("""
        INSERT INTO vehicle_count
        (
            total_vehicles,
            cars,
            bikes,
            buses,
            trucks,
            bicycles,
            date,
            time
        )
        VALUES
        (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            total,
            cars,
            bikes,
            buses,
            trucks,
            bicycles,
            now.strftime("%Y-%m-%d"),
            now.strftime("%H:%M:%S")
        ))

        conn.commit()

        conn.close()

        annotated = results[0].plot()

        cv2.putText(
            annotated,
            f"Total: {total}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        _, buffer = cv2.imencode(".jpg", annotated)

        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            frame +
            b'\r\n'
        )

    cap.release()