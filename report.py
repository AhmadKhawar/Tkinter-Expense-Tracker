import tkinter as tk
from tkinter import ttk
from db import get_expenses
from collections import defaultdict

class ReportApp:
    def __init__(self, root, user_id):
        self.root = root
        self.root.title("Expense Report")
        self.root.geometry("400x400")
        self.user_id = user_id

        self.total_label = tk.Label(root, text="Total Expense: 0", font=("Arial", 12, "bold"))
        self.total_label.pack(pady=10)

        self.tree = ttk.Treeview(root, columns=("Category", "Amount"), show="headings")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Amount", text="Amount")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.load_report()

    def load_report(self):
        expenses = get_expenses(self.user_id)
        category_totals = defaultdict(float)
        total = 0

        for expense in expenses:
            date, category, desc, amount = expense
            category_totals[category] += float(amount)
            total += float(amount)

        self.total_label.config(text=f"Total Expense: Rs. {total:.2f}")

        for cat, amt in category_totals.items():
            self.tree.insert("", tk.END, values=(cat, f"Rs. {amt:.2f}"))

# For testing without login
if __name__ == "__main__":
    root = tk.Tk()
    app = ReportApp(root, user_id=1)
    root.mainloop()