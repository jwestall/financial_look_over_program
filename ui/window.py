import tkinter as tk
from tkinter import ttk
from ui.overview import Overview

class Window:
    def __new__(self):
        root = tk.Tk()
        root.title("Financial Look Over Program")

        notebook = ttk.Notebook(root)
        notebook.pack(fill='both', pady=10, expand=True)

        overview = Overview(notebook)
        overview.pack(fill='both', expand=True)

        loans = ttk.Frame(notebook)
        loans.pack(fill='both', expand=True)

        notebook.add(overview, text='Overview')
        notebook.add(tab2, text='Loans')

        return root