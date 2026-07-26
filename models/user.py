# ==========================================
# Student Attendance Management System
# User Model
# ==========================================

import sqlite3
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from config import DATABASE


# ==========================================
# Database Connection
# ==========================================

def get_connection():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn


# ==========================================
# Register User
# ==========================================

def register_user(name, username, email, password):

    conn = get_connection()

    cursor = conn.cursor()

    hashed_password = generate_password_hash(password)

    cursor.execute("""

    INSERT INTO users
    (name, username, email, password)

    VALUES (?,?,?,?)

    """,

    (

        name,

        username,

        email,

        hashed_password

    )

    )

    conn.commit()

    conn.close()


# ==========================================
# Login User
# ==========================================

def login_user(username, password):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM users WHERE username=?",

        (username,)

    )

    user = cursor.fetchone()

    conn.close()

    if user:

        if check_password_hash(

            user["password"],

            password

        ):

            return user

    return None


# ==========================================
# Get User By Username
# ==========================================

def get_user(username):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM users WHERE username=?",

        (username,)

    )

    user = cursor.fetchone()

    conn.close()

    return user


# ==========================================
# Update Profile
# ==========================================

def update_profile(

        username,

        name,

        email

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    UPDATE users

    SET

    name=?,

    email=?

    WHERE username=?

    """,

    (

        name,

        email,

        username

    )

    )

    conn.commit()

    conn.close()


# ==========================================
# Change Password
# ==========================================

def change_password(

        username,

        new_password

):

    conn = get_connection()

    cursor = conn.cursor()

    hashed = generate_password_hash(

        new_password

    )

    cursor.execute("""

    UPDATE users

    SET password=?

    WHERE username=?

    """,

    (

        hashed,

        username

    )

    )

    conn.commit()

    conn.close()


# ==========================================
# Check Username Exists
# ==========================================

def username_exists(username):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        "SELECT id FROM users WHERE username=?",

        (username,)

    )

    user = cursor.fetchone()

    conn.close()

    return user is not None