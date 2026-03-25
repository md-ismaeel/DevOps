import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="mydb",
        user="myuser",
        password="mypassword",
        port=5432
    )