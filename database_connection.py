import mysql.connector
from mysql.connector import Error

def create_connection():
    conn = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            database='library_management_system',
            user="root",
            password='12345678'
        )
        if conn.is_connected():
            print("Connected to MySQL Database")
    except Error as e:
        print(f"Error: {e}")
    return conn