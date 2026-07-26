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
# Mark Attendance
# ==========================================

def mark_attendance(student_id, attendance_date, status):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO attendance
        (
            student_id,
            attendance_date,
            status
        )

        VALUES (?, ?, ?)

    """, (

        student_id,
        attendance_date,
        status

    ))

    conn.commit()

    conn.close()


# ==========================================
# Save Attendance of All Students
# ==========================================

def save_all_attendance(attendance_date, students, form_data):

    conn = get_connection()

    cursor = conn.cursor()

    for student in students:

        student_id = student["id"]

        status = form_data.get(

            f"status_{student_id}",

            "Present"

        )

        cursor.execute("""

            INSERT INTO attendance
            (
                student_id,
                attendance_date,
                status
            )

            VALUES (?, ?, ?)

        """, (

            student_id,
            attendance_date,
            status

        ))

    conn.commit()

    conn.close()


# ==========================================
# Get All Attendance
# ==========================================

def get_attendance():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            attendance.id,

            students.id AS student_id,

            students.name,

            students.roll_no,

            attendance.attendance_date,

            attendance.status

        FROM attendance

        INNER JOIN students

        ON attendance.student_id = students.id

        ORDER BY attendance.attendance_date DESC

    """)

    attendance = cursor.fetchall()

    conn.close()

    return attendance


# ==========================================
# Get Report of One Student
# ==========================================

def get_student_report(student_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            attendance.id,

            students.name,

            students.roll_no,

            attendance.attendance_date,

            attendance.status

        FROM attendance

        INNER JOIN students

        ON attendance.student_id = students.id

        WHERE students.id = ?

        ORDER BY attendance.attendance_date DESC

    """, (student_id,))

    report = cursor.fetchall()

    conn.close()

    return report


# ==========================================
# Attendance Summary
# ==========================================

def get_attendance_summary(student_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            COUNT(*) AS total,

            SUM(CASE WHEN status='Present' THEN 1 ELSE 0 END) AS present,

            SUM(CASE WHEN status='Absent' THEN 1 ELSE 0 END) AS absent,

            SUM(CASE WHEN status='Leave' THEN 1 ELSE 0 END) AS leave_count

        FROM attendance

        WHERE student_id=?

    """, (student_id,))

    summary = cursor.fetchone()

    conn.close()

    return summary


# ==========================================
# Delete Attendance
# ==========================================

def delete_attendance(attendance_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        "DELETE FROM attendance WHERE id=?",

        (attendance_id,)

    )

    conn.commit()

    conn.close()


# ==========================================
# Get Attendance By Date
# ==========================================

def get_attendance_by_date(attendance_date):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            attendance.id,

            students.name,

            students.roll_no,

            attendance.status

        FROM attendance

        INNER JOIN students

        ON attendance.student_id=students.id

        WHERE attendance.attendance_date=?

        ORDER BY students.name

    """, (attendance_date,))

    data = cursor.fetchall()

    conn.close()

    return data