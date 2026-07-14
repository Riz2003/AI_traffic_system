from db import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
INSERT INTO vehicle_count
(
total_vehicles,
cars,
bikes,
buses,
trucks,
bicycles,
date,
time
)
VALUES
(
20,
10,
5,
2,
2,
1,
'09-07-2026',
'11:30'
)
""")

conn.commit()

conn.close()

print("Data Inserted Successfully")