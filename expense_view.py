import tkinter as tk
from tkinter import ttk
from db import get_expenses, create_tables

class ExpenseViewApp:
    def __init__(self, root, user_id):
        self.root = root
        self.root.title("View Expenses")
        self.root.geometry("600x400")
        self.user_id = user_id

        self.tree = ttk.Treeview(root, columns=("Date", "Category", "Description", "Amount"), show="headings")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Amount", text="Amount")

        self.tree.column("Date", width=100)
        self.tree.column("Category", width=120)
        self.tree.column("Description", width=200)
        self.tree.column("Amount", width=80)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Add vertical scrollbar
        scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.load_expenses()

    def load_expenses(self):
        expenses = get_expenses(self.user_id)
        for row in expenses:
            self.tree.insert("", tk.END, values=row)

# For testing
if __name__ == "__main__":
    create_tables()
    root = tk.Tk()
    app = ExpenseViewApp(root, user_id=1)
    root.mainloop()