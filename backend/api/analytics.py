from flask import Blueprint, jsonify
from database.db import get_connection

analytics_api = Blueprint("analytics_api", __name__)

@analytics_api.route("/analytics")
def analytics():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        SUM(cars),
        SUM(bikes),
        SUM(buses),
        SUM(trucks),
        SUM(bicycles)
    FROM vehicle_count
    """)

    row = cursor.fetchone()

    conn.close()

    return jsonify({

        "cars": row[0] or 0,

        "bikes": row[1] or 0,

        "buses": row[2] or 0,

        "trucks": row[3] or 0,

        "bicycles": row[4] or 0

    })