# =====================================
# Database Handler (SQLite)
# =====================================

import sqlite3
import os
from student import StudentRecord

DB_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'student.db')

def connect_db():
    return sqlite3.connect(DB_NAME)

def setup_database():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id_num TEXT PRIMARY KEY,
                full_name TEXT NOT NULL,
                program TEXT NOT NULL,
                year_level INTEGER NOT NULL,
                sex TEXT NOT NULL,
                email_addr TEXT NOT NULL
            )
        """)

def insert_record(record):
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO students (id_num, full_name, program, year_level, sex, email_addr)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (record.id_num, record.full_name, record.program, record.year_level, record.sex, record.email_addr))
            return True
    except sqlite3.IntegrityError:
        return False

def fetch_record(id_num):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id_num = ?", (id_num,))
        row = cursor.fetchone()
        if row:
            return StudentRecord.from_row(row)
    return None

def update_record(record):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE students
            SET full_name = ?, program = ?, year_level = ?, sex = ?, email_addr = ?
            WHERE id_num = ?
        """, (record.full_name, record.program, record.year_level, record.sex, record.email_addr, record.id_num))
        return cursor.rowcount > 0

def delete_record(id_num):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id_num = ?", (id_num,))
        return cursor.rowcount > 0

def fetch_all_records():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        return [StudentRecord.from_row(row) for row in rows]
