from db import get_connection

conn = get_connection()
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT
);
""")

# Insert
cur.execute(
    "INSERT INTO users (name, email) VALUES (%s, %s)",
    ("Ismail", "ismail@example.com")
)

# Read
cur.execute("SELECT * FROM users;")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.commit()
cur.close()
conn.close()