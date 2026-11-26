import helpers.numbers_helper as num_helper
import tkinter as tk
from tkinter import ttk

class Loans:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.loans = []
        self.refresh_rows(self.frame)

    def refresh_rows(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()

        self.loans = num_helper.get_loans()

        for loan in self.loans:
            label = loan.label.value

            row = tk.Frame(parent)
            name = tk.Label(row, text=label)
            total = tk.Label(row, text=f'${loan.total.value:,.2f}')
            remove = tk.Button(row, text="Remove", command=lambda label=label: self.remove_row(label))

            name.pack(padx=10, pady=10, side=tk.LEFT)
            total.pack(padx=10, pady=10, side=tk.LEFT)
            remove.pack(padx=10, pady=10, side=tk.LEFT)

            row.pack()

    def remove_row(self, loan):
        num_helper.remove_loan(loan)
        self.refresh_rows(self.frame)