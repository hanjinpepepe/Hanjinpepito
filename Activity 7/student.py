# =====================================
# Student Record Model
# =====================================
 
class StudentRecord:
    def __init__(self, id_num, full_name, program, year_level, sex, email_addr):
        self.id_num = id_num
        self.full_name = full_name
        self.program = program
        self.year_level = year_level
        self.sex = sex
        self.email_addr = email_addr
 
    def display(self):
        print(f"ID: {self.id_num} | Name: {self.full_name} | Program: {self.program} | Year: {self.year_level} | Sex: {self.sex} | Email: {self.email_addr}")
 
    def to_dict(self):
        return {
            "id_num": self.id_num,
            "full_name": self.full_name,
            "program": self.program,
            "year_level": self.year_level,
            "sex": self.sex,
            "email_addr": self.email_addr
        }
 
    @classmethod
    def from_row(cls, row):
        if not row:
            return None
        return cls(row[0], row[1], row[2], row[3], row[4], row[5])
 
 