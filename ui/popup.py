import tkinter as tk

def build_popup(text):
    root = tk.Tk()
    root.title("Financial Look Over Program")
    root.geometry("500x200")

    label = tk.Label(root, text=text)
    label.pack(padx=10, pady=10)

    button = tk.Button(root, text="Close", command=root.destroy)
    button.pack(padx=10, pady=10, side=tk.RIGHT)

    return root