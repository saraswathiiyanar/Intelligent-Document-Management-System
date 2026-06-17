import sqlite3

conn = sqlite3.connect('database.db')

rows = conn.execute("SELECT * FROM users").fetchall()

print(rows)

conn.close()