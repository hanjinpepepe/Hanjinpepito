# =====================================
# Main Application Entry Point
# =====================================

import tkinter as tk
from gui import StudentGui

def main():
    root = tk.Tk()
    app = StudentGui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
