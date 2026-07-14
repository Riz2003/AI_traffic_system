from flask import Blueprint, jsonify
import sqlite3
from database.db import get_connection

vehicle_api = Blueprint("vehicle_api", __name__)

@vehicle_api.route("/vehicles")
def vehicles():

    from database.db import get_connection

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM vehicle_count
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    data = []

    for row in rows:

        data.append({
            "id": row[0],
            "total": row[1],
            "cars": row[2],
            "bikes": row[3],
            "buses": row[4],
            "trucks": row[5],
            "bicycles": row[6],
            "date": row[7],
            "time": row[8]
        })

    return jsonify(data)