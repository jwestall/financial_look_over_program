import helpers.numbers_helper as num_helper
import tkinter as tk
from tkinter import ttk

class Loans:
    def __new__(self, parent):
        self.frame = tk.Frame(parent)
        self.loans = []
        self.refresh_rows(self, self.frame)

        return self.frame

    def refresh_rows(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()

        self.loans = num_helper.get_loans()

        for loan in self.loans:
            row = tk.Frame(parent)
            name = tk.Label(row, text=loan.label.value)
            total = tk.Label(row, text=f'${loan.total.value:,.2f}')
            remove = tk.Button(row, text="Remove", command=lambda: self.remove_row(self, loan.label.value))

            name.pack(padx=10, pady=10, side=tk.LEFT)
            total.pack(padx=10, pady=10, side=tk.LEFT)
            remove.pack(padx=10, pady=10, side=tk.LEFT)

            row.pack()

    def remove_row(self, loan):
        num_helper.remoe_loan(loan)
        self.refresh_rows(self, self.frame)