import tkinter as tk
from tkinter import ttk
from ui.loans import Loans
from ui.overview import Overview

class Window:
    def __new__(self):
        root = tk.Tk()
        root.title("Financial Look Over Program")

        notebook = ttk.Notebook(root)
        notebook.pack(fill='both', pady=10, expand=True)

        overview = Overview(notebook)
        loans = Loans(notebook)

        overview_page = overview.frame
        overview_page.pack(fill='both', expand=True)

        loans_page = loans.frame
        loans_page.pack(fill='both', expand=True)

        expences = ttk.Frame(notebook)
        expences.pack(fill='both', expand=True)

        income = ttk.Frame(notebook)
        income.pack(fill='both', expand=True)

        notebook.add(overview_page, text='Overview')
        notebook.add(loans_page, text='Loans')
        notebook.add(expences, text='Expences')
        notebook.add(income, text='Income')

        return root