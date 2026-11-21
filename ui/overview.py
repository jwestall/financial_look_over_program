import tkinter as tk
from tkinter import ttk

class Overview:
    def __new__(self, parent):
        frame = tk.Frame(parent)
        sub_frame_1 = tk.Frame(frame)
        sub_frame_2 = tk.Frame(frame)
        sub_frame_3 = tk.Frame(frame)

        label_1 = tk.Label(sub_frame_1, text="Total Income: ")
        self.value_1 = tk.Label(sub_frame_1, text="DUMMY TOTAL")

        label_2 = tk.Label(sub_frame_2, text="Total Expences: ")
        self.value_2 = tk.Label(sub_frame_2, text="DUMMY TOTAL")

        label_3 = tk.Label(sub_frame_3, text="Net Money: ")
        self.value_3 = tk.Label(sub_frame_3, text="DUMMY TOTAL")

        button = tk.Button(frame, text="Recalculate")

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

        return frame