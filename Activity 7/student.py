"""
student.py
Purpose: Student Class
Defines the Student object used throughout the application (OOP principle).
"""


class Student:
    """Represents a single student record."""

    def __init__(self, student_id, name, course, year_level, gender, email):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.year_level = year_level
        self.gender = gender
        self.email = email

    def to_tuple(self):
        """Return the student's data as a tuple (useful for DB operations)."""
        return (
            self.student_id,
            self.name,
            self.course,
            self.year_level,
            self.gender,
            self.email,
        )

    @staticmethod
    def from_row(row):
        """Build a Student object from a database row / tuple."""
        return Student(*row)

    def __str__(self):
        return (
            f"Student ID: {self.student_id} | Name: {self.name} | "
            f"Course: {self.course} | Year Level: {self.year_level} | "
            f"Gender: {self.gender} | Email: {self.email}"
        )