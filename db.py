import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Div@4499",
        database="attendance_db"
    );
SELECT * FROM students;