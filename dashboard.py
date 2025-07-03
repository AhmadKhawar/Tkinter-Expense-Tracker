import tkinter as tk
from expense_entry import ExpenseEntryApp
from expense_view import ExpenseViewApp

class Dashboard:
    def __init__(self, root, user_id):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("300x200")
        self.user_id = user_id

        tk.Label(root, text="Expense Tracker Dashboard", font=("Helvetica", 14)).pack(pady=20)

        tk.Button(root, text="Add Expense", command=self.open_add_expense).pack(pady=10)
        tk.Button(root, text="View Expenses", command=self.open_view_expense).pack(pady=10)

    def open_add_expense(self):
        self.root.destroy()
        new_root = tk.Tk()
        ExpenseEntryApp(new_root, self.user_id)
        new_root.mainloop()

    def open_view_expense(self):
        self.root.destroy()
        new_root = tk.Tk()
        ExpenseViewApp(new_root, self.user_id)
        new_root.mainloop()