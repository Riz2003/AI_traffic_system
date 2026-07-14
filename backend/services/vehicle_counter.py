from ultralytics import YOLO
import cv2

model = YOLO("models/yolov8n.pt")


def count_vehicles(video_path):

    cap = cv2.VideoCapture(video_path)

    counted_ids = set()

    total = 0

    car = 0
    bike = 0
    bus = 0
    truck = 0
    bicycle = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        results = model.track(frame, persist=True)

        if results[0].boxes.id is None:
            continue

        boxes = results[0].boxes

        for box, track_id in zip(boxes, boxes.id):

            track_id = int(track_id)

            class_id = int(box.cls[0])

            name = model.names[class_id]

            if name not in [
                "car",
                "truck",
                "bus",
                "motorcycle",
                "bicycle"
            ]:
                continue

            if track_id in counted_ids:
                continue

            counted_ids.add(track_id)

            total += 1

            if name == "car":
                car += 1

            elif name == "motorcycle":
                bike += 1

            elif name == "bus":
                bus += 1

            elif name == "truck":
                truck += 1

            elif name == "bicycle":
                bicycle += 1

    cap.release()

    return {
        "total": total,
        "cars": car,
        "bikes": bike,
        "buses": bus,
        "trucks": truck,
        "bicycles": bicycle
    }