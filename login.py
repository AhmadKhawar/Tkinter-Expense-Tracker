from dashboard import Dashboard
import tkinter as tk
from tkinter import messagebox
from db import register_user, login_user, create_tables

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login / Register")
        self.root.geometry("300x250")

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        tk.Label(root, text="Username").pack(pady=5)
        tk.Entry(root, textvariable=self.username_var).pack(pady=5)

        tk.Label(root, text="Password").pack(pady=5)
        tk.Entry(root, textvariable=self.password_var, show="*").pack(pady=5)

        tk.Button(root, text="Login", command=self.login).pack(pady=10)
        tk.Button(root, text="Register", command=self.register).pack()

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
            # You can launch main app here
            
        else:
            messagebox.showerror("Failed", "Invalid username or password.")

    def register(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if not username or not password:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
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
