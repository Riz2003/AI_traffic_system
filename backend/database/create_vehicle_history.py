import sqlite3

conn = sqlite3.connect("database/traffic.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehicle_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    vehicle_type TEXT,

    confidence REAL,

    camera_name TEXT,

    track_id INTEGER,

    date TEXT,

    time TEXT

)
""")

conn.commit()

conn.close()

print("Vehicle History Table Created Successfully")