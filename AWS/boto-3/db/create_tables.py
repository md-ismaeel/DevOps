import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
schema_path=os.path.join(BASE_DIR, "schema.sql")
seed_path=os.path.join(BASE_DIR, "seed.sql")

conn = psycopg2.connect(
    host=os.getenv("DATABASE_URL"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT"),
    sslmode="require"
)

cur = conn.cursor()

# Run schema
# with open(schema_path, "r") as f:
#     cur.execute(f.read())

# Run seed data
# with open(seed_path, "r") as f:
#     cur.execute(f.read())

data=[
    ("Rajesh", "rajesh@example.com"),
    ("Santosh", "santosh@example.com"),
    ("Vishal", "vishal@example.com"),
    ("Rakesh", "rakesh@example.com"),
    ("Praveen", "praveen@example.com")
]

execute_values(
    cur,
    """
    INSERT INTO users (name, email) VALUES %s
    ON CONFLICT (email) DO NOTHING
    """,
    data
)

cur.execute("SELECT * FROM users");
print(cur.fetchall())
cur.execute("SELECT * FROM products");
print(cur.fetchall())
cur.execute("SELECT * FROM orders");
print(cur.fetchall())
cur.execute("SELECT * FROM order_items");
print(cur.fetchall())

conn.commit()

cur.close()
conn.close()

print("Tables created & data inserted!")