from flask import Blueprint, jsonify
from database.db import get_connection

dashboard_api = Blueprint("dashboard_api", __name__)

@dashboard_api.route("/dashboard")
def dashboard():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        total_vehicles,
        cars,
        bikes,
        buses,
        trucks,
        bicycles
    FROM vehicle_count
    ORDER BY id DESC
    LIMIT 1
    """)

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return jsonify({
            "total":0,
            "cars":0,
            "bikes":0,
            "buses":0,
            "trucks":0,
            "bicycles":0
        })

    return jsonify({
        "total":row["total_vehicles"],
        "cars":row["cars"],
        "bikes":row["bikes"],
        "buses":row["buses"],
        "trucks":row["trucks"],
        "bicycles":row["bicycles"]
    })