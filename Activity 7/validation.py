# =====================================
# Input Validator
# =====================================
 
import re
 
def check_id(id_num):
    val = str(id_num).strip()
    if not val:
        return False, "Student ID cannot be empty."
    if not val.isdigit():
        return False, "Student ID must be a positive integer."
    num = int(val)
    if num < 5000:
        return False, "Student ID must be 5000 or greater."
    return True, ""
 
def check_name(name):
    val = str(name).strip()
    if not val:
        return False, "Name cannot be empty."
    if not re.match(r"^[a-zA-Z\s.'-]+$", val):
        return False, "Name must only contain letters, spaces, periods, hyphens, or apostrophes."
    return True, ""
 
def check_program(program):
    val = str(program).strip()
    if not val:
        return False, "Course cannot be empty."
    if not re.match(r"^[a-zA-Z0-9\s.-]+$", val):
        return False, "Course must only contain letters, numbers, spaces, periods, or hyphens."
    return True, ""
 
def check_year(year):
    val = str(year).strip()
    if not val:
        return False, "Year Level cannot be empty."
    if not val.isdigit():
        return False, "Year Level must be a positive integer."
    num = int(val)
    if num < 1 or num > 4:
        return False, "Year Level must be between 1 and 4."
    return True, ""
 
def check_gender(sex):
    val = str(sex).strip()
    if val not in ["Male", "Female"]:
        return False, "Gender must be either 'Male' or 'Female'."
    return True, ""
 
def check_email(email):
    val = str(email).strip()
    if not val:
        return False, "Email cannot be empty."
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(pattern, val):
        return False, "Invalid email format (e.g. user@domain.com)."
    return True, ""
 
def validate_record_data(id_num, name, program, year, sex, email):
    errors = {}
   
    ok, msg = check_id(id_num)
    if not ok:
        errors["id_num"] = msg
       
    ok, msg = check_name(name)
    if not ok:
        errors["name"] = msg
       
    ok, msg = check_program(program)
    if not ok:
        errors["program"] = msg
       
    ok, msg = check_year(year)
    if not ok:
        errors["year_level"] = msg
       
    ok, msg = check_gender(sex)
    if not ok:
        errors["gender"] = msg
       
    ok, msg = check_email(email)
    if not ok:
        errors["email"] = msg
       
    is_valid = len(errors) == 0
    return is_valid, errors
 