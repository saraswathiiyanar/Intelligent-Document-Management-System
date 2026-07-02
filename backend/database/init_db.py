import sqlite3

# connect database (file will be created if not exists)
conn = sqlite3.connect("database.db")

# create users table
conn.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database initialized successfully!")