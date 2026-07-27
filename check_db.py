import sqlite3

conn = sqlite3.connect("ssl_manager.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM certificate_requests")
rows = cursor.fetchall()

if rows:
    print("Records found:")
    for row in rows:
        print(row)
else:
    print("No records found.")

conn.close()