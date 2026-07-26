from models.db import db


class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    roll_no = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    department = db.Column(
        db.String(100)
    )

    semester = db.Column(
        db.String(20)
    )

    email = db.Column(
        db.String(120)
    )

    phone = db.Column(
        db.String(30)
    )

    attendance = db.relationship(
        "Attendance",
        backref="student",
        cascade="all, delete",
        lazy=True
    )


def add_student(
    name,
    roll_no,
    department,
    semester,
    email,
    phone
):

    student = Student(
        name=name,
        roll_no=roll_no,
        department=department,
        semester=semester,
        email=email,
        phone=phone
    )

    db.session.add(student)
    db.session.commit()


def get_students():

    return Student.query.order_by(
        Student.roll_no
    ).all()


def get_student(student_id):

    return Student.query.get(student_id)


def delete_student(student_id):

    student = Student.query.get(student_id)

    if student:

        db.session.delete(student)

        db.session.commit()


def update_student(
    student_id,
    name,
    roll_no,
    department,
    semester,
    email,
    phone
):

    student = Student.query.get(student_id)

    if student:

        student.name = name
        student.roll_no = roll_no
        student.department = department
        student.semester = semester
        student.email = email
        student.phone = phone

        db.session.commit()
