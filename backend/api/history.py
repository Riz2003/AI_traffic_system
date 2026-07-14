from flask import Blueprint, jsonify
from database.db import get_connection

history_api = Blueprint("history_api", __name__)

@history_api.route("/history")
def history():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        vehicle_type,
        confidence,
        camera_name,
        track_id,
        date,
        time
    FROM vehicle_history
    ORDER BY id DESC
    LIMIT 50
    """)

    rows = cursor.fetchall()

    conn.close()

    data = []

    for row in rows:

        data.append({

            "id": row["id"],

            "vehicle": row["vehicle_type"],

            "confidence": round(row["confidence"] * 100, 2),

            "camera": row["camera_name"],

            "track": row["track_id"],

            "date": row["date"],

            "time": row["time"]

        })

    return jsonify(data)