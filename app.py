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
    flash,
    session
)

from config import Config

from models.db import init_db

from models.user import (
    register_user,
    login_user
)

from models.student import (
    add_student,
    get_students
)

from models.attendance import (
    mark_attendance,
    get_attendance,
    get_student_report,
    total_present,
    total_absent,
    total_leave
)
import os

print(os.getenv("DATABASE_URL"))
# ==========================================
# Flask App
# ==========================================

app = Flask(__name__)

app.config.from_object(Config)

init_db(app)


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

    students = get_students()

    attendance = get_attendance()

    return render_template(

        "dashboard.html",

        username=session.get("username"),

        total_students=len(students),

        present_today=total_present(),

        absent_today=total_absent(),

        leave_today=total_leave(),

        recent_attendance=attendance[:10]
    )
# ==========================================
# Students
# ==========================================

@app.route("/students", methods=["GET","POST"])
def students():

    if request.method == "POST":

        add_student(

            request.form["name"],

            request.form["roll_no"],

            request.form["department"],

            request.form["semester"],

            request.form["email"],

            request.form["phone"]

        )

        flash(
            "Student Added Successfully",
            "success"
        )

        return redirect(
            url_for("students")
        )

    return render_template(

        "students.html",

        students=get_students()
    )

# ==========================================
# Attendance
# ==========================================

@app.route("/attendance", methods=["GET", "POST"])
def attendance():

    students = get_students()

    if request.method == "POST":

        attendance_date = request.form["attendance_date"]

        for student in students:

            status = request.form.get(
                f"status_{student.id}"
            )

            mark_attendance(
                student.id,
                attendance_date,
                status
            )

        flash(
            "Attendance Saved Successfully",
            "success"
        )

        return redirect(
            url_for("attendance")
        )

    return render_template(

        "attendance.html",

        students=students
    )
# ==========================================
# Report
# ==========================================

@app.route("/report", methods=["GET","POST"])
def report():

    students = get_students()

    attendance = []

    if request.method == "POST":

        student_id = request.form["student_id"]

        attendance = get_student_report(
            student_id
        )

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
