import sqlite3

conn = sqlite3.connect("8up.db")
with open("schema.sql") as f:
    conn.executescript(f.read())
conn.commit()
conn.close()
print("Database created")