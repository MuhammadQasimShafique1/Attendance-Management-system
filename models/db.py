# ==========================================
# Student Attendance Management System
# Database File
# ==========================================

import sqlite3
from config import DATABASE


# ==========================================
# Database Connection
# ==========================================

def get_connection():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn


# ==========================================
# Create Tables
# ==========================================

def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    # ======================================
    # Users Table
    # ======================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        username TEXT UNIQUE NOT NULL,

        email TEXT UNIQUE,

        password TEXT NOT NULL

    )

    """)

    # ======================================
    # Students Table
    # ======================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS students(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        roll_no TEXT UNIQUE NOT NULL,

        department TEXT,

        semester TEXT,

        email TEXT,

        phone TEXT,

        photo TEXT

    )

    """)

    # ======================================
    # Attendance Table
    # ======================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS attendance(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        student_id INTEGER,

        attendance_date TEXT,

        status TEXT,

        FOREIGN KEY(student_id)

        REFERENCES students(id)

    )

    """)

    conn.commit()

    conn.close()


# ==========================================
# Initialize Database
# ==========================================

if __name__ == "__main__":

    create_tables()

    print("Database Created Successfully.")