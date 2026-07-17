"""
database.py
Purpose: SQLite Database
Handles all database connections and CRUD (Create, Read, Update, Delete)
operations for student records. student.db is created automatically the
first time the application runs.
"""

import sqlite3


class Database:
    def __init__(self, db_name="student.db"):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        """Create the students table automatically if it doesn't exist."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                course TEXT NOT NULL,
                year_level TEXT NOT NULL,
                gender TEXT NOT NULL,
                email TEXT NOT NULL
            )
            """
        )
        conn.commit()
        conn.close()

    def insert_student(self, student):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO students
                (student_id, name, course, year_level, gender, email)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            student.to_tuple(),
        )
        conn.commit()
        conn.close()

    def update_student(self, student):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE students
            SET name = ?, course = ?, year_level = ?, gender = ?, email = ?
            WHERE student_id = ?
            """,
            (
                student.name,
                student.course,
                student.year_level,
                student.gender,
                student.email,
                student.student_id,
            ),
        )
        conn.commit()
        conn.close()

    def delete_student(self, student_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        conn.commit()
        conn.close()

    def search_student(self, student_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
        row = cursor.fetchone()
        conn.close()
        return row

    def fetch_all_students(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students ORDER BY student_id")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def student_exists(self, student_id):
        return self.search_student(student_id) is not None