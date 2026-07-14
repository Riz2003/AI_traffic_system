from database.db import get_connection

def save_vehicle(
    vehicle_type,
    confidence,
    camera_name,
    track_id,
    date,
    time
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO vehicle_history

    (

        vehicle_type,

        confidence,

        camera_name,

        track_id,

        date,

        time

    )

    VALUES

    (?, ?, ?, ?, ?, ?)

    """,

    (

        vehicle_type,

        confidence,

        camera_name,

        track_id,

        date,

        time

    ))

    conn.commit()

    conn.close()