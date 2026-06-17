import sqlite3

conn = sqlite3.connect('database.db')

# 1. Create table
conn.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
''')

# 2. Insert sample data
conn.execute("INSERT INTO users (username, password) VALUES ('admin', '1234')")

conn.commit()

# 3. Check data
print(conn.execute("SELECT * FROM users").fetchall())

conn.close()