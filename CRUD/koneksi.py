import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

conn = mysql.connector.connect(
    user=user, password=password, host=host, database="BUKUDB"
)

conn.close()
