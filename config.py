# ==========================================
# Student Attendance Management System
# Configuration File
# ==========================================

import os

# ------------------------------------------
# Base Directory
# ------------------------------------------

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# ------------------------------------------
# Secret Key
# ------------------------------------------

SECRET_KEY = "Qasim_Student_Attendance_2026"

# ------------------------------------------
# Database Location
# ------------------------------------------

DATABASE = os.path.join(
    BASE_DIR,
    "instance",
    "database.db"
)

# ------------------------------------------
# Upload Folder
# ------------------------------------------

UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "uploads",
    "student_photos"
)

# ------------------------------------------
# Allowed Image Extensions
# ------------------------------------------

ALLOWED_EXTENSIONS = {

    "png",

    "jpg",

    "jpeg",

    "gif"

}

# ------------------------------------------
# Maximum Upload Size
# ------------------------------------------

MAX_CONTENT_LENGTH = 5 * 1024 * 1024

# 5 MB

# ------------------------------------------
# Attendance Status
# ------------------------------------------

ATTENDANCE_STATUS = [

    "Present",

    "Absent",

    "Leave"

]

# ------------------------------------------
# Default Admin Account
# ------------------------------------------

DEFAULT_ADMIN = {

    "username": "admin",

    "password": "admin123"

}