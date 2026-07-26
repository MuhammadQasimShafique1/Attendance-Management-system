from datetime import date

from models.db import db


class Attendance(db.Model):

    __tablename__ = "attendance"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )

    attendance_date = db.Column(
        db.Date,
        nullable=False,
        default=date.today
    )

    status = db.Column(
        db.String(20),
        nullable=False
    )


def mark_attendance(student_id, attendance_date, status):

    record = Attendance(
        student_id=student_id,
        attendance_date=attendance_date,
        status=status
    )

    db.session.add(record)
    db.session.commit()


def get_attendance():

    return Attendance.query.order_by(
        Attendance.attendance_date.desc()
    ).all()


def get_student_report(student_id):

    return Attendance.query.filter_by(
        student_id=student_id
    ).order_by(
        Attendance.attendance_date.desc()
    ).all()


def total_present():

    return Attendance.query.filter_by(
        status="Present"
    ).count()


def total_absent():

    return Attendance.query.filter_by(
        status="Absent"
    ).count()


def total_leave():

    return Attendance.query.filter_by(
        status="Leave"
    ).count()
