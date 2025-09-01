from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
import os
import requests
import json

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
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50)
)
""")

class User(BaseModel):
    name: str
    email: str

@app.post("/users")
def create_user(user: User):
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (user.name, user.email))
    conn.commit()
    # Publish to Kafka via Dapr
    dapr_pub_url = "http://localhost:3500/v1.0/publish/messagebus/users"
    payload = json.dumps({"name": user.name, "email": user.email})
    requests.post(dapr_pub_url, data=payload)
    return {"status": "user created", "user": user}
