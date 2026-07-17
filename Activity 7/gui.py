"""
gui.py
Purpose: GUI Implementation ( Cyberpunk Theme)
Builds the Tkinter interface with a Cyberpunk-inspired color palette:
Sky blue backgrounds, Dirt brown frames, Grass green buttons, 
and Wooden UI tables.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from student import Student
from database import Database
import validation


class StudentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Information Management System - neon_pink Edition")
        self.root.geometry("780x680")
        self.root.resizable(False, False)

        # Alternative Cyberpunk Theme Colors
        self.bg_sky = "#080B16"       # Midnight blue background
        self.bg_dirt = "#121A2A"      # Dark blue panels
        self.fg_text = "#E6F1FF"      # Cool white text
        self.bg_grass = "#FF6B00"     # Neon orange buttons
        self.bg_wood = "#1B263B"      # Deep blue table
        self.bg_sand = "#0F172A"      # Dark entry fields

        self.neon_orange = "#FF6B00"
        self.neon_blue = "#00BFFF"
        self.neon_yellow = "#FFD166"

        self.font_retro = ("Courier", 10, "bold")
        self.font_title = ("Courier", 15, "bold")

        self.font_retro = ("Courier", 10, "bold")
        self.font_title = ("Courier", 15, "bold")

        # Apply sky background to main window
        self.root.configure(bg=self.bg_sky)

        self.db = Database()

        # Form variables
        self.student_id_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.course_var = tk.StringVar()
        self.year_level_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.email_var = tk.StringVar()

        self.build_widgets()

    # ------------------------------------------------------------------ #
    # UI BUILD
    # ------------------------------------------------------------------ #
    def build_widgets(self):
        title = tk.Label(
            self.root,
            text="STUDENT INFORMATION MANAGEMENT SYSTEM",
            font=self.font_title,
            bg=self.bg_sky,
            fg="#FFD700" # Gold coins/Sun color
        )
        title.pack(pady=10)

        # Form Frame (Dirt block style)
        form_frame = tk.Frame(self.root, bg=self.bg_dirt, bd=4, relief="ridge")
        form_frame.pack(pady=5, padx=20, fill="x")

        # Labels + Entry widgets
        entry_fields = [
            ("Student ID:", self.student_id_var),
            ("Name:", self.name_var),
            ("Course:", self.course_var),
            ("Year Level:", self.year_level_var),
        ]

        for i, (label_text, var) in enumerate(entry_fields):
            tk.Label(
                form_frame, text=label_text, font=self.font_retro, width=12, anchor="w",
                bg=self.bg_dirt, fg=self.fg_text
            ).grid(row=i, column=0, padx=5, pady=6, sticky="w")
            tk.Entry(
                form_frame, textvariable=var, width=42,
                font=("Courier", 10), bg=self.bg_sand, fg="#000000"
            ).grid(row=i, column=1, padx=5, pady=6, sticky="w")

        # Gender radiobuttons
        tk.Label(
            form_frame, text="Gender:", font=self.font_retro, width=12, anchor="w",
            bg=self.bg_dirt, fg=self.fg_text
        ).grid(row=4, column=0, padx=5, pady=6, sticky="w")
        gender_frame = tk.Frame(form_frame, bg=self.bg_dirt)
        gender_frame.grid(row=4, column=1, sticky="w")
        
        tk.Radiobutton(
            gender_frame, text="Male", variable=self.gender_var, value="Male",
            bg=self.bg_dirt, fg=self.fg_text, selectcolor=self.bg_wood, 
            font=self.font_retro, activebackground=self.bg_dirt, activeforeground=self.fg_text
        ).pack(side="left")
        tk.Radiobutton(
            gender_frame, text="Female", variable=self.gender_var, value="Female",
            bg=self.bg_dirt, fg=self.fg_text, selectcolor=self.bg_wood, 
            font=self.font_retro, activebackground=self.bg_dirt, activeforeground=self.fg_text
        ).pack(side="left", padx=(15, 0))

        # Email
        tk.Label(
            form_frame, text="Email:", font=self.font_retro, width=12, anchor="w",
            bg=self.bg_dirt, fg=self.fg_text
        ).grid(row=5, column=0, padx=5, pady=6, sticky="w")
        tk.Entry(
            form_frame, textvariable=self.email_var, width=42,
            font=("Courier", 10), bg=self.bg_sand, fg="#000000"
        ).grid(row=5, column=1, padx=5, pady=6, sticky="w")

        # Buttons (Grass block style)
        button_frame = tk.Frame(self.root, bg=self.bg_sky)
        button_frame.pack(pady=15)

        btn_style = {
            "width": 11, 
            "font": self.font_retro,
            "bg": self.bg_grass,
            "fg": self.fg_text,
            "activebackground": "#388E3C", # Darker green on click
            "activeforeground": self.fg_text,
            "bd": 3,
            "relief": "raised"
        }

        tk.Button(button_frame, text="Save", command=self.save_student, **btn_style).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Search", command=self.search_student, **btn_style).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(button_frame, text="Update", command=self.update_student, **btn_style).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(button_frame, text="Delete", command=self.delete_student, **btn_style).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Display All", command=self.display_all_students, **btn_style).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(button_frame, text="Clear", command=self.clear_fields, **btn_style).grid(row=1, column=2, padx=5, pady=5)
        
        # Exit button gets a Lava / Underworld red color
        exit_btn_style = btn_style.copy()
        exit_btn_style.update({"bg": "#B22222", "activebackground": "#8B0000"})
        tk.Button(button_frame, text="Exit", command=self.root.quit, **exit_btn_style).grid(row=1, column=3, padx=5, pady=5)

        # Student Records table label
        records_label = tk.Label(
            self.root, text="STUDENT RECORDS", font=("Courier", 12, "bold"),
            bg=self.bg_sky, fg="#FFD700"
        )
        records_label.pack(pady=(10, 5))

        # Customizing the Treeview to look like a Wooden Chest Interface
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background=self.bg_wood,
            foreground=self.fg_text,
            rowheight=25,
            fieldbackground=self.bg_wood,
            font=("Courier", 9)
        )
        style.map("Treeview", background=[("selected", "#CD853F")]) # Lighter wood on select
        style.configure(
            "Treeview.Heading", 
            background=self.bg_dirt, 
            foreground=self.fg_text, 
            font=self.font_retro
        )

        columns = ("student_id", "name", "course", "year_level", "gender", "email")
        self.tree = ttk.Treeview(
            self.root, columns=columns, show="headings", height=10
        )
        headings = ["Student ID", "Name", "Course", "Year Level", "Gender", "Email"]
        widths = [80, 160, 90, 90, 70, 190]
        for col, heading, w in zip(columns, headings, widths):
            self.tree.heading(col, text=heading)
            self.tree.column(col, width=w, anchor="center")
        self.tree.pack(pady=5, padx=15, fill="x")

        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)

    # ------------------------------------------------------------------ #
    # HELPERS
    # ------------------------------------------------------------------ #
    def get_form_values(self):
        return (
            self.student_id_var.get().strip(),
            self.name_var.get().strip(),
            self.course_var.get().strip(),
            self.year_level_var.get().strip(),
            self.gender_var.get().strip(),
            self.email_var.get().strip(),
        )

    def clear_fields(self):
        self.student_id_var.set("")
        self.name_var.set("")
        self.course_var.set("")
        self.year_level_var.set("")
        self.gender_var.set("")
        self.email_var.set("")

    def populate_fields(self, row):
        student = Student.from_row(row)
        self.student_id_var.set(student.student_id)
        self.name_var.set(student.name)
        self.course_var.set(student.course)
        self.year_level_var.set(student.year_level)
        self.gender_var.set(student.gender)
        self.email_var.set(student.email)

    def on_row_select(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], "values")
            self.populate_fields(values)

    # ------------------------------------------------------------------ #
    # BUTTON ACTIONS 
    # ------------------------------------------------------------------ #
    def save_student(self):
        student_id, name, course, year_level, gender, email = self.get_form_values()
        is_valid, message = validation.validate_all(
            student_id, name, course, year_level, gender, email
        )
        if not is_valid:
            messagebox.showerror("Validation Error", message)
            return
        if self.db.student_exists(student_id):
            messagebox.showerror("Error", f"Student ID {student_id} already exists.")
            return

        student = Student(student_id, name, course, year_level, gender, email)
        self.db.insert_student(student)
        messagebox.showinfo("Success", "Student record saved successfully.")
        self.clear_fields()
        
        # Clear the display table when saving
        for row in self.tree.get_children():
            self.tree.delete(row)

    def search_student(self):
        student_id = self.student_id_var.get().strip()
        is_valid, message = validation.validate_student_id(student_id)
        if not is_valid:
            messagebox.showerror("Validation Error", message)
            return

        row = self.db.search_student(student_id)
        if row is None:
            messagebox.showinfo("Not Found", f"No student found with ID {student_id}.")
            return

        self.populate_fields(row)
        messagebox.showinfo("Found", "Student record found.")
        
        # Clear the table and display only the searched result
        for child in self.tree.get_children():
            self.tree.delete(child)
        self.tree.insert("", "end", values=row)

    def update_student(self):
        student_id, name, course, year_level, gender, email = self.get_form_values()
        is_valid, message = validation.validate_all(
            student_id, name, course, year_level, gender, email
        )
        if not is_valid:
            messagebox.showerror("Validation Error", message)
            return
        if not self.db.student_exists(student_id):
            messagebox.showerror("Error", f"No student found with ID {student_id}.")
            return

        student = Student(student_id, name, course, year_level, gender, email)
        self.db.update_student(student)
        messagebox.showinfo("Success", "Student record updated successfully.")
        self.clear_fields()
        self.display_all_students()

    def delete_student(self):
        student_id = self.student_id_var.get().strip()
        is_valid, message = validation.validate_student_id(student_id)
        if not is_valid:
            messagebox.showerror("Validation Error", message)
            return
        if not self.db.student_exists(student_id):
            messagebox.showerror("Error", f"No student found with ID {student_id}.")
            return

        confirm = messagebox.askyesno(
            "Confirm Delete", f"Are you sure you want to delete student {student_id}?"
        )
        if confirm:
            self.db.delete_student(student_id)
            messagebox.showinfo("Deleted", "Student record deleted successfully.")
            self.clear_fields()
            self.display_all_students()

    def display_all_students(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for student_row in self.db.fetch_all_students():
            self.tree.insert("", "end", values=student_row)