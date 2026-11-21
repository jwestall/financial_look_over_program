import helpers.numbers_helper as num_helper
import tkinter as tk
from tkinter import ttk

class Loans:
    def __new__(self, parent):
        frame = tk.Frame(parent)
        self.loans = []
        self.refresh_rows(self, frame)

        return frame

    def refresh_rows(self, parent):
        self.loans = num_helper.get_loans()

        for loan in self.loans:
            row = tk.Frame(parent)
            name = tk.Label(row, text=loan.label.value)
            total = tk.Label(row, text=f'${loan.total.value:,.2f}')

            name.pack(padx=10, pady=10, side=tk.LEFT)
            total.pack(padx=10, pady=10, side=tk.LEFT)

            row.pack()