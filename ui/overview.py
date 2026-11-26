import helpers.numbers_helper as num_helper
import tkinter as tk
from tkinter import ttk

class Overview:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        sub_frame_1 = tk.Frame(self.frame)
        sub_frame_2 = tk.Frame(self.frame)
        sub_frame_3 = tk.Frame(self.frame)

        label_1 = tk.Label(sub_frame_1, text="Total Income: ")
        self.value_1 = tk.Label(sub_frame_1, text="DUMMY TOTAL")

        label_2 = tk.Label(sub_frame_2, text="Total Spendings: ")
        self.value_2 = tk.Label(sub_frame_2, text="DUMMY TOTAL")

        label_3 = tk.Label(sub_frame_3, text="Net Money: ")
        self.value_3 = tk.Label(sub_frame_3, text="DUMMY TOTAL")

        button = tk.Button(self.frame, text="Recalculate", command=self.refresh())

        label_1.pack(padx=10, pady=10, side=tk.LEFT)
        self.value_1.pack(padx=10, pady=10, side=tk.LEFT)
        label_2.pack(padx=10, pady=10, side=tk.LEFT)
        self.value_2.pack(padx=10, pady=10, side=tk.LEFT)
        label_3.pack(padx=10, pady=10, side=tk.LEFT)
        self.value_3.pack(padx=10, pady=10, side=tk.LEFT)

        sub_frame_1.pack()
        sub_frame_2.pack()
        sub_frame_3.pack()

        button.pack(padx=10, pady=10)

        self.refresh()

    def refresh(self):
        incomes = num_helper.get_incomes()
        tot_i = 0
        for income in incomes:
            tot_i = tot_i + income.monthly.value

        expences = num_helper.get_expences()
        loans = num_helper.get_loans()

        tot_s = 0
        for expence in expences:
            tot_s = tot_s + expence.amount.value

        for loan in loans:
            tot_s = tot_s + loan.payment.value

        net = tot_i - tot_s

        self.value_1.config(text=f"${tot_i:,.2f}")
        self.value_2.config(text=f"${tot_s:,.2f}")
        self.value_3.config(text=f"${net:,.2f}")