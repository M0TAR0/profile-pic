import tkinter as tk
from tkinter import ttk


def Say_hi(button):
    print("Hello World")
    button.config(text="You clicked!")


root = tk.Tk()
root.title("Hello Magnificent world!")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=("N", "W", "E", "S"))

hello_label = ttk.Label(mainframe, text="Tkinter says: ")
hello_label.grid(column=1, row=2, sticky=("N"))

hello_button = ttk.Button(mainframe, text="Hello World")
hello_button.config(command=lambda: Say_hi(hello_button))
hello_button.grid(column=2, row=2, sticky=("E"))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
