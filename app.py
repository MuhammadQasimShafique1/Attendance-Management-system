# ==========================================
# Student Attendance Management System
# Developed By: Qasim Shafique
# Backend: Flask
# Database: SQLite
# ==========================================

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

import sqlite3

from config import (
    SECRET_KEY,
    DATABASE,
    UPLOAD_FOLDER
)

from models.db import create_tables

from models.user import (
    register_user,
    login_user
)

from models.student import (
    get_students,
    add_student
)
from models.attendance import (
    get_attendance,
    get_student_report,
    mark_attendance,
    save_all_attendance
)

# ==========================================
# Flask App
# ==========================================

app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

app.secret_key = SECRET_KEY

# Create Database Tables
create_tables()

# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")

# ==========================================
# Login
# ==========================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        user = login_user(username, password)

        if user:

            session["username"] = username

            flash("Login Successful!", "success")

            return redirect(url_for("dashboard"))

        else:

            flash("Invalid Username or Password", "danger")

    return render_template("login.html")

# ==========================================
# Register
# ==========================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]

        username = request.form["username"]

        email = request.form["email"]

        password = request.form["password"]

        register_user(
            name,
            username,
            email,
            password
        )

        flash("Registration Successful", "success")

        return redirect(url_for("login"))

    return render_template("register.html")

# ==========================================
# Dashboard
# ==========================================

@app.route("/dashboard")
def dashboard():

    if "username" not in session:

        return redirect("/login")

    return render_template(
        "dashboard.html",
        username=session["username"]
    )

# ==========================================
# Students
# ==========================================

@app.route("/students", methods=["GET", "POST"])
def students():

    if "username" not in session:

        return redirect("/login")

    if request.method == "POST":

        add_student(

            request.form["name"],
            request.form["roll_no"],
            request.form["department"],
            request.form["semester"],
            request.form["email"],
            request.form["phone"]

        )

        flash("Student Added Successfully", "success")

        return redirect("/students")

    students = get_students()

    return render_template(
        "students.html",
        students=students
    )

# ==========================================
# Attendance
# ==========================================

@app.route("/attendance", methods=["GET", "POST"])
def attendance():

    if "username" not in session:
        return redirect(url_for("login"))

    students = get_students()

    if request.method == "POST":

        attendance_date = request.form["attendance_date"]

        save_all_attendance(
            attendance_date,
            students,
            request.form
        )

        flash("Attendance Saved Successfully!", "success")

        return redirect(url_for("attendance"))

    attendance = get_attendance()

    return render_template(
        "attendance.html",
        students=students,
        attendance=attendance
    )
# ==========================================
# Report
# ==========================================

@app.route("/report", methods=["GET", "POST"])
def report():

    if "username" not in session:
        return redirect(url_for("login"))

    students = get_students()

    attendance = []

    if request.method == "POST":

        student_id = request.form.get("student_id")

        if student_id:

            attendance = get_student_report(student_id)

    return render_template(
        "report.html",
        students=students,
        attendance=attendance
    )

# ==========================================
# Profile
# ==========================================

@app.route("/profile")
def profile():

    if "username" not in session:

        return redirect("/login")

    return render_template(

        "profile.html",

        username=session["username"]

    )

# ==========================================
# Logout
# ==========================================

@app.route("/logout")
def logout():

    session.clear()

    flash("Logged Out Successfully", "info")

    return redirect("/login")

# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    app.run(

        debug=True

    )