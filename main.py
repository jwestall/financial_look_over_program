import os
import tkinter as tk
from ui.popup import build_popup
from ui.window import Window

path = '~/Library/Mobile Documents/com~apple~Numbers/Documents/'
file = path + 'Finances.numbers'
root = {}

if os.path.exists(os.path.expanduser(file)):
    root = Window()
else:
    root = build_popup("Finance spreadsheet not found. Please create and try again.")

root.mainloop()