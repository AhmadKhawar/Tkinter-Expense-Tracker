from login import LoginApp
from db import create_tables
import tkinter as tk

if __name__ == "__main__":
    create_tables()  # Ensure DB is ready
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()