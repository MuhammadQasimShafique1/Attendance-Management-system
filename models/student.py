import sqlite3
from config import DATABASE


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# ==========================
# Add Student
# ==========================

def add_student(name, roll_no, department, semester, email, phone):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students
        (name, roll_no, department, semester, email, phone)

        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, roll_no, department, semester, email, phone))

    conn.commit()
    conn.close()


# ==========================
# Get All Students
# ==========================

def get_students():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    return students