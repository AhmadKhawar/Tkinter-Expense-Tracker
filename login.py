from dashboard import Dashboard
import tkinter as tk
from tkinter import messagebox
from db import register_user, login_user, create_tables

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login / Register")
        self.root.geometry("300x300")

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.confirm_password_var = tk.StringVar()

        tk.Label(root, text="Username").pack(pady=5)
        tk.Entry(root, textvariable=self.username_var).pack(pady=5)

        tk.Label(root, text="Password").pack(pady=5)
        tk.Entry(root, textvariable=self.password_var, show="*").pack(pady=5)

        tk.Label(root, text="Confirm Password").pack(pady=5)
        tk.Entry(root, textvariable=self.confirm_password_var, show="*").pack(pady=5)

        tk.Button(
            root,
            text="Login",
            command=self.login,
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049"
        ).pack(pady=10)

        tk.Button(
            root,
            text="Register",
            command=self.register,
            bg="#2196F3",
            fg="white",
            activebackground="#1976D2"
        ).pack()

    def login(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if not username or not password:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        user = login_user(username, password)
        if user:
            messagebox.showinfo("Success", f"Welcome {username}!")
            self.root.destroy()
            from dashboard import Dashboard
            new_root = tk.Tk()
            Dashboard(new_root, user[0])
            new_root.mainloop()
        else:
            messagebox.showerror("Failed", "Invalid username or password.")

    def register(self):
        username = self.username_var.get()
        password = self.password_var.get()
        confirm_password = self.confirm_password_var.get()

        if not username or not password or not confirm_password:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        if password != confirm_password:
            messagebox.showerror("Password Mismatch", "Passwords do not match.")
            return

        success = register_user(username, password)
        if success:
            messagebox.showinfo("Success", "User registered successfully!")
        else:
            messagebox.showerror("Failed", "Username already exists!")

# Run only if this file is executed directly
if __name__ == "__main__":
    create_tables()
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
