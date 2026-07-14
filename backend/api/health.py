from flask import Blueprint, jsonify

health_api = Blueprint("health_api", __name__)

@health_api.route("/health")
def health():
    return jsonify({
        "application": "AI Smart Traffic Monitoring System",
        "backend": "running",
        "version": "1.0"
    })