"""
validation.py
Purpose: Input Validation
Contains all field-level validation rules used before saving/updating a
student record. Each function returns a tuple: (is_valid: bool, message: str)
"""

import re


def validate_student_id(student_id):
    student_id = (student_id or "").strip()
    if not student_id:
        return False, "Student ID cannot be empty."
    if not student_id.isdigit():
        return False, "Student ID must contain numbers only."
    return True, ""


def validate_name(name):
    name = (name or "").strip()
    if not name:
        return False, "Name cannot be empty."
    if not re.match(r"^[A-Za-z.\s]+$", name):
        return False, "Name must contain letters only."
    return True, ""


def validate_course(course):
    course = (course or "").strip()
    if not course:
        return False, "Course cannot be empty."
    return True, ""


def validate_year_level(year_level):
    year_level = (year_level or "").strip()
    if not year_level:
        return False, "Year Level cannot be empty."
    if not year_level.isdigit() or not (1 <= int(year_level) <= 6):
        return False, "Year Level must be a number between 1 and 6."
    return True, ""


def validate_gender(gender):
    gender = (gender or "").strip()
    if gender not in ("Male", "Female"):
        return False, "Please select a gender (Male or Female)."
    return True, ""


def validate_email(email):
    email = (email or "").strip()
    if not email:
        return False, "Email cannot be empty."
    pattern = r"^[\w.\-]+@[\w.\-]+\.\w+$"
    if not re.match(pattern, email):
        return False, "Invalid email format."
    return True, ""


def validate_all(student_id, name, course, year_level, gender, email):
    """Run every field validator in order; stop and return on first failure."""
    checks = [
        validate_student_id(student_id),
        validate_name(name),
        validate_course(course),
        validate_year_level(year_level),
        validate_gender(gender),
        validate_email(email),
    ]
    for is_valid, message in checks:
        if not is_valid:
            return False, message
    return True, ""