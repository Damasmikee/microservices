from fastapi import FastAPI
import mysql.connector
import os

app = FastAPI()

# MySQL connection
db_host = os.getenv("MYSQL_HOST", "mysql")
db_user = os.getenv("MYSQL_USER", "user")
db_pass = os.getenv("MYSQL_PASSWORD", "password")
db_name = os.getenv("MYSQL_DATABASE", "microtaskdb")

conn = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_pass,
    database=db_name
)
cursor = conn.cursor()

@app.get("/users")
def get_users():
    cursor.execute("SELECT id, name, email FROM users")
    rows = cursor.fetchall()
    users = [{"id": r[0], "name": r[1], "email": r[2]} for r in rows]
    return {"users": users}
