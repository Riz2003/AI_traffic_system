from flask import Blueprint, jsonify
from services.vehicle_counter import count_vehicles

detect_api = Blueprint("detect_api", __name__)

@detect_api.route("/detect")
def detect():

    result = count_vehicles("uploads/traffic.mp4")

    return jsonify(result)