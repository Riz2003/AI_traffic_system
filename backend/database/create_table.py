import sqlite3

conn = sqlite3.connect("traffic.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehicle_count (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    total_vehicles INTEGER,
    cars INTEGER,
    bikes INTEGER,
    buses INTEGER,
    trucks INTEGER,
    bicycles INTEGER,
    date TEXT,
    time TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")