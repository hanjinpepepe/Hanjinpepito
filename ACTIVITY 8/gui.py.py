# =====================================
# GUI Module (Dark Mode)
# =====================================
 
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import database 
from student import StudentRecord
from validation import validate_record_data
 
class StudentGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Information Management System")
        self.root.geometry("880x760")
        self.root.minsize(800, 700)
        self.root.configure(bg="#1e1e24")
 
        database.setup_database()
        self.setup_styles()
 
        self.create_header()
        self.create_main_container()
        self.create_form_fields()
        self.create_button_panel()
        self.create_records_table()
        self.create_status_bar()
 
 
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        self.style.configure("Treeview",
                            background="#cdcfce",
                            foreground="#290ec7",
                            rowheight=26,
                            fieldbackground="#ececec",
                            font=("Segoe UI", 9))
        self.style.map("Treeview",
                       background=[("selected", "#065285")],
                       foreground=[("selected", "#ffffff")])
        
        self.style.configure("Treeview.Heading",
                            background="#0202d3",
                            foreground="#ffffff",
                            font=("Segoe UI", 10, "bold"),
                            borderwidth=1)
 
    def create_header(self):
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=60)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
 
        title_label = tk.Label(header_frame, 
                               text="STUDENT INFORMATION MANAGEMENT SYSTEM", 
                               font=("Segoe UI", 16, "bold"), 
                               fg="#ffffff", 
                               bg="#0070e0")
        title_label.pack(expand=True, fill=tk.BOTH)
 
    def create_main_container(self):
        self.container = tk.Frame(self.root, bg="#1e1e24", padx=20, pady=15)
        self.container.pack(fill=tk.BOTH, expand=True)
 
    def create_form_fields(self):
        self.form_frame = tk.LabelFrame(self.container, 
                                        text=" Student Information Form ", 
                                        font=("Segoe UI", 11, "bold"), 
                                        fg="#ffffff", 
                                        bg="#0101b6", 
                                        padx=15, 
                                        pady=15, 
                                        relief="solid", 
                                        bd=1)
        self.form_frame.pack(fill=tk.X, pady=(0, 10))
 
        self.form_frame.columnconfigure(0, weight=1)
        self.form_frame.columnconfigure(1, weight=3)
 
        self.var_id = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_program = tk.StringVar()
        self.var_year = tk.StringVar()
        self.var_sex = tk.StringVar(value="Male")
        self.var_email = tk.StringVar()
 
        fields = [
            ("STUDENT ID :", self.var_id, 0),
            ("NAME :", self.var_name, 1),
            ("COURSE :", self.var_program, 2),
            ("YEAR LEVEL :", self.var_year, 3)
        ]
 
        for label_text, var, row in fields:
            lbl = tk.Label(self.form_frame, text=label_text, font=("Segoe UI", 10, "bold"), bg="#2a2a35", fg="#e2e8f0", anchor="w")
            lbl.grid(row=row, column=0, sticky="w", pady=6, padx=(0, 10))
            
            entry = tk.Entry(self.form_frame, textvariable=var, font=("Segoe UI", 10), bg="#3f3f4c", fg="#ffffff", insertbackground="#ffffff", bd=1, relief="solid")
            entry.grid(row=row, column=1, sticky="ew", pady=6)
 
        lbl_gender = tk.Label(self.form_frame, text="GENDER :", font=("Segoe UI", 10, "bold"), bg="#2a2a35", fg="#e2e8f0", anchor="w")
        lbl_gender.grid(row=4, column=0, sticky="w", pady=6, padx=(0, 10))
 
        gender_subframe = tk.Frame(self.form_frame, bg="#2a2a35")
        gender_subframe.grid(row=4, column=1, sticky="w", pady=6)
 
        self.radio_male = tk.Radiobutton(gender_subframe, text="Male", variable=self.var_sex, value="Male", 
                                         font=("Segoe UI", 10), bg="#2a2a35", fg="#ffffff", selectcolor="#3f3f4c", activebackground="#2a2a35", activeforeground="#ffffff")
        self.radio_male.pack(side=tk.LEFT, padx=(0, 20))
        
        self.radio_female = tk.Radiobutton(gender_subframe, text="Female", variable=self.var_sex, value="Female", 
                                           font=("Segoe UI", 10), bg="#2a2a35", fg="#ffffff", selectcolor="#3f3f4c", activebackground="#2a2a35", activeforeground="#ffffff")
        self.radio_female.pack(side=tk.LEFT)
 
        lbl_email = tk.Label(self.form_frame, text="EMAIL :", font=("Segoe UI", 10, "bold"), bg="#2a2a35", fg="#e2e8f0", anchor="w")
        lbl_email.grid(row=5, column=0, sticky="w", pady=6, padx=(0, 10))
        
        entry_email = tk.Entry(self.form_frame, textvariable=self.var_email, font=("Segoe UI", 10), bg="#3f3f4c", fg="#ffffff", insertbackground="#ffffff", bd=1, relief="solid")
        entry_email.grid(row=5, column=1, sticky="ew", pady=6)
 
    def create_button_panel(self):
        self.btn_frame = tk.Frame(self.container, bg="#1e1e24")
        self.btn_frame.pack(fill=tk.X, pady=(5, 15))
 
        row1_frame = tk.Frame(self.btn_frame, bg="#1e1e24")
        row1_frame.pack(anchor="center", pady=(0, 5))
 
        row2_frame = tk.Frame(self.btn_frame, bg="#1e1e24")
        row2_frame.pack(anchor="center")
 
        self.btn_save = self.create_button(row1_frame, "SAVE", "#2ecc71", "#27ae60", self.save_record)
        self.btn_save.pack(side=tk.LEFT, padx=8)
 
        self.btn_search = self.create_button(row1_frame, "SEARCH", "#3498db", "#2980b9", self.search_record)
        self.btn_search.pack(side=tk.LEFT, padx=8)
 
        self.btn_update = self.create_button(row1_frame, "UPDATE", "#f39c12", "#d35400", self.update_record)
        self.btn_update.pack(side=tk.LEFT, padx=8)
 
        self.btn_delete = self.create_button(row2_frame, "DELETE", "#e74c3c", "#c0392b", self.delete_record)
        self.btn_delete.pack(side=tk.LEFT, padx=8)
 
        self.btn_display = self.create_button(row2_frame, "DISPLAY", "#9b59b6", "#8e44ad", self.display_all_records)
        self.btn_display.pack(side=tk.LEFT, padx=8)
 
        self.btn_clear = self.create_button(row2_frame, "CLEAR", "#7f8c8d", "#718093", self.clear_fields)
        self.btn_clear.pack(side=tk.LEFT, padx=8)
 
        self.btn_exit = self.create_button(row2_frame, "EXIT", "#2c3e50", "#1a252f", self.exit_application)
        self.btn_exit.pack(side=tk.LEFT, padx=8)
 
    def create_button(self, parent, text, bg_color, hover_color, command):
        btn = tk.Button(parent, 
                        text=text, 
                        bg=bg_color, 
                        fg="#ffffff", 
                        activebackground=hover_color, 
                        activeforeground="#ffffff", 
                        font=("Segoe UI", 10, "bold"), 
                        relief="flat", 
                        bd=0, 
                        cursor="hand2", 
                        width=12, 
                        pady=6)
        
        btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg_color))
        btn.config(command=command)
        return btn
 
    def create_records_table(self):
        table_container = tk.Frame(self.container, bg="#1e1e24")
        table_container.pack(fill=tk.BOTH, expand=True)
 
        lbl_records = tk.Label(table_container, 
                               text="STUDENT RECORDS", 
                               font=("Segoe UI", 11, "bold"), 
                               fg="#ffffff", 
                               bg="#1e1e24")
        lbl_records.pack(anchor="w", pady=(5, 5))
 
        tree_frame = tk.Frame(table_container, bd=1, relief="solid")
        tree_frame.pack(fill=tk.BOTH, expand=True)
 
        columns = ("id", "name", "course", "year", "gender", "email")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
        
        self.tree.heading("id", text="STUDENT ID")
        self.tree.heading("name", text="NAME")
        self.tree.heading("course", text="COURSE")
        self.tree.heading("year", text="YEAR")
        self.tree.heading("gender", text="GENDER")
        self.tree.heading("email", text="EMAIL")
 
        self.tree.column("id", width=100, anchor="center")
        self.tree.column("name", width=180, anchor="w")
        self.tree.column("course", width=110, anchor="center")
        self.tree.column("year", width=70, anchor="center")
        self.tree.column("gender", width=80, anchor="center")
        self.tree.column("email", width=180, anchor="w")
 
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
 
        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)
 
    def create_status_bar(self):
        self.status_var = tk.StringVar(value="Ready")
 
        status_frame = tk.Frame(self.root, bg="#12121a", height=28)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.pack_propagate(False)
 
        self.status_label = tk.Label(status_frame,
                                     textvariable=self.status_var,
                                     font=("Segoe UI", 9),
                                     fg="#9aa0a6",
                                     bg="#12121a",
                                     anchor="w",
                                     padx=10)
        self.status_label.pack(fill=tk.BOTH, expand=True)
 
    # --- Threading Helpers ---
    # All database work happens on a background thread so the window never
    # freezes. The background thread never touches Tkinter widgets directly;
    # it only computes a result, then hands off to the main thread via
    # self.root.after(), which is the only safe way to update the GUI.
 
    def set_busy(self, is_busy, message="Ready"):
        state = tk.DISABLED if is_busy else tk.NORMAL
        for btn in (self.btn_save, self.btn_search, self.btn_update,
                    self.btn_delete, self.btn_display, self.btn_clear):
            btn.config(state=state)
        self.status_var.set(message)
 
    def run_in_background(self, task, on_done, busy_message="Working, please wait..."):
        """
        Runs `task` (a no-argument function) on a background thread.
        When it finishes, `on_done(result, error)` is scheduled to run
        back on the main GUI thread. `error` is None on success, or the
        raised Exception if `task` failed.
        """
        self.set_busy(True, busy_message)
 
        def worker():
            try:
                result = task()
                error = None
            except Exception as e:
                result = None
                error = e
            self.root.after(0, lambda: on_done(result, error))
 
        threading.Thread(target=worker, daemon=True).start()
 
    def on_row_select(self, event):
        selected_items = self.tree.selection()
        if not selected_items:
            return
        
        item_values = self.tree.item(selected_items[0])["values"]
        
        self.var_id.set(item_values[0])
        self.var_name.set(item_values[1])
        self.var_program.set(item_values[2])
        self.var_year.set(item_values[3])
        self.var_sex.set(item_values[4])
        self.var_email.set(item_values[5])
 
    def refresh_table(self, records_list=None):
        for item in self.tree.get_children():
            self.tree.delete(item)
 
        if records_list is None:
            records_list = database.fetch_all_records()
 
        for s in records_list:
            self.tree.insert("", tk.END, values=(s.id_num, s.full_name, s.program, s.year_level, s.sex, s.email_addr))
 
    # --- Button Function Handlers ---
 
    def save_record(self):
        id_num = self.var_id.get().strip()
        name = self.var_name.get().strip()
        program = self.var_program.get().strip()
        year = self.var_year.get().strip()
        sex = self.var_sex.get()
        email = self.var_email.get().strip()
 
        is_valid, errors = validate_record_data(id_num, name, program, year, sex, email)
        if not is_valid:
            error_message = "\n".join([f"- {msg}" for msg in errors.values()])
            messagebox.showwarning("Validation Error", f"Please fix the following errors:\n\n{error_message}")
            return
 
        def task():
            existing = database.fetch_record(id_num)
            if existing:
                return {"status": "duplicate"}
            new_student = StudentRecord(id_num, name, program, int(year), sex, email)
            success = database.insert_record(new_student)
            return {"status": "done", "success": success}
 
        def on_done(result, error):
            self.set_busy(False)
            if error:
                messagebox.showerror("Error", f"An unexpected error occurred:\n{error}")
                return
 
            if result["status"] == "duplicate":
                messagebox.showwarning("Duplicate Entry", f"Student ID '{id_num}' already exists in records.\nTo modify it, please use the UPDATE button.")
                return
 
            if result["success"]:
                messagebox.showinfo("Success", "Student record successfully saved!")
                self.clear_fields()
            else:
                messagebox.showerror("Error", "An error occurred while inserting the record.")
 
        self.run_in_background(task, on_done, "Saving record...")
 
    def search_record(self):
        id_num = self.var_id.get().strip()
        if not id_num:
            messagebox.showwarning("Missing Input", "Please enter a Student ID to search.")
            return
 
        def task():
            return database.fetch_record(id_num)
 
        def on_done(student, error):
            self.set_busy(False)
            if error:
                messagebox.showerror("Error", f"An unexpected error occurred:\n{error}")
                return
 
            if student:
                self.clear_fields()
                self.var_id.set(student.id_num)
                self.var_name.set(student.full_name)
                self.var_program.set(student.program)
                self.var_year.set(str(student.year_level))
                self.var_sex.set(student.sex)
                self.var_email.set(student.email_addr)
 
                for item in self.tree.get_children():
                    if self.tree.item(item)["values"][0] == student.id_num:
                        self.tree.selection_set(item)
                        self.tree.see(item)
                        break
 
                messagebox.showinfo("Search Results", f"Student Record for ID '{id_num}' found.")
            else:
                messagebox.showinfo("Search Results", f"Student Record with ID '{id_num}' was not found.")
 
        self.run_in_background(task, on_done, "Searching...")
 
    def update_record(self):
        id_num = self.var_id.get().strip()
        name = self.var_name.get().strip()
        program = self.var_program.get().strip()
        year = self.var_year.get().strip()
        sex = self.var_sex.get()
        email = self.var_email.get().strip()
 
        is_valid, errors = validate_record_data(id_num, name, program, year, sex, email)
        if not is_valid:
            error_message = "\n".join([f"- {msg}" for msg in errors.values()])
            messagebox.showwarning("Validation Error", f"Please fix the following errors:\n\n{error_message}")
            return
 
        def task():
            existing = database.fetch_record(id_num)
            if not existing:
                return {"status": "missing"}
            updated_student = StudentRecord(id_num, name, program, int(year), sex, email)
            success = database.update_record(updated_student)
            return {"status": "done", "success": success}
 
        def on_done(result, error):
            self.set_busy(False)
            if error:
                messagebox.showerror("Error", f"An unexpected error occurred:\n{error}")
                return
 
            if result["status"] == "missing":
                messagebox.showwarning("Record Missing", f"Student ID '{id_num}' does not exist.\nCannot update a non-existent record.")
                return
 
            if result["success"]:
                messagebox.showinfo("Success", "Student record successfully updated!")
                self.clear_fields()
                self.refresh_table()
            else:
                messagebox.showerror("Error", "No changes made, or update failed.")
 
        self.run_in_background(task, on_done, "Updating record...")
 
    def delete_record(self):
        id_num = self.var_id.get().strip()
        if not id_num:
            messagebox.showwarning("Missing Input", "Please enter or select a Student ID to delete.")
            return
 
        student = database.fetch_record(id_num)
        if not student:
            messagebox.showinfo("Not Found", f"Student Record with ID '{id_num}' does not exist.")
            return
 
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to permanently delete the student record for:\n\nID: {student.id_num}\nName: {student.full_name}?")
        if not confirm:
            return
 
        def task():
            return database.delete_record(id_num)
 
        def on_done(success, error):
            self.set_busy(False)
            if error:
                messagebox.showerror("Error", f"An unexpected error occurred:\n{error}")
                return
 
            if success:
                messagebox.showinfo("Success", "Student record successfully deleted.")
                self.clear_fields()
                self.refresh_table()
            else:
                messagebox.showerror("Error", "Failed to delete the record.")
 
        self.run_in_background(task, on_done, "Deleting record...")
 
    def display_all_records(self):
        def task():
            return database.fetch_all_records()
 
        def on_done(records, error):
            self.set_busy(False)
            if error:
                messagebox.showerror("Error", f"An unexpected error occurred:\n{error}")
                return
 
            self.refresh_table(records)
            if not records:
                messagebox.showinfo("Records Display", "No student records found in the database.")
            else:
                messagebox.showinfo("Records Display", f"Loaded {len(records)} records from the database.")
 
        self.run_in_background(task, on_done, "Loading records...")
 
    def clear_fields(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_program.set("")
        self.var_year.set("")
        self.var_sex.set("Male")
        self.var_email.set("")
        self.tree.selection_remove(self.tree.selection())
 
    def exit_application(self):
        confirm = messagebox.askyesno("Confirm Exit", "Are you sure you want to exit the application?")
        if confirm:
            self.root.destroy()