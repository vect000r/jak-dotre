from tkinter import *
from tkinter import ttk

def tkinter_logic():
    root = Tk()
    root.title("Tkinter Logic")
    root.geometry("400x400")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Jaki przystanek chcesz wyświetlić?").grid(column=0, row=0)
    searched_name = ttk.Entry(frm, width=30)
    ttk.Button(frm, text="Wyjście", command = root.destroy).grid(column=1, row=0)
    root.mainloop()
    