"""
main.py
Purpose: Starts the application
Entry point for the Student Information Management System.
Run this file to launch the program: python main.py
"""

import tkinter as tk
from gui import StudentGUI


def main():
    root = tk.Tk()
    app = StudentGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()