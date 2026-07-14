from flask import Blueprint, jsonify

camera_api = Blueprint("camera_api", __name__)

@camera_api.route("/camera/status")
def camera_status():
    return jsonify({
        "camera": "offline",
        "status": "ready"
    })