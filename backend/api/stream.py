from flask import Blueprint, Response
from services.detection_service import generate_frames

stream_api = Blueprint("stream_api", __name__)

@stream_api.route("/video_feed")
def video_feed():

    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )