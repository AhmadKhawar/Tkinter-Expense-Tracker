import tkinter as tk
from tkinter import messagebox
from db import add_expense, create_tables

class ExpenseEntryApp:
    def __init__(self, root, user_id):
        self.root = root
        self.root.title("Add Expense..")
        self.root.geometry("400x350")
        self.user_id = user_id

        self.date_var = tk.StringVar()
        self.category_var = tk.StringVar()
        self.desc_var = tk.StringVar()
        self.amount_var = tk.StringVar()

        tk.Label(root, text="Date (YYYY-MM-DD)").pack(pady=5)
        tk.Entry(root, textvariable=self.date_var).pack(pady=5)

        tk.Label(root, text="Category").pack(pady=5)
        tk.Entry(root, textvariable=self.category_var).pack(pady=5)

        tk.Label(root, text="Description").pack(pady=5)
        tk.Entry(root, textvariable=self.desc_var).pack(pady=5)

        tk.Label(root, text="Amount").pack(pady=5)
        tk.Entry(root, textvariable=self.amount_var).pack(pady=5)

        tk.Button(root, text="Add Expense", command=self.save_expense).pack(pady=15)

    def save_expense(self):
        date = self.date_var.get()
        category = self.category_var.get()
        desc = self.desc_var.get()
        amount = self.amount_var.get()

        if not (date and category and desc and amount):
            messagebox.showwarning("Input Error", "All fields are required.")
            return

        try:
            amount = float(amount)
            add_expense(self.user_id, date, category, desc, amount)
            messagebox.showinfo("Success", "Expense added successfully!")
            self.date_var.set("")
            self.category_var.set("")
            self.desc_var.set("")
            self.amount_var.set("")
        except ValueError:
            messagebox.showerror("Invalid Input", "Amount must be a number.")

# Run for testing
if __name__ == "__main__":
    create_tables()
    root = tk.Tk()
    app = ExpenseEntryApp(root, user_id=1)  # Test with dummy user_id
    root.mainloop()
