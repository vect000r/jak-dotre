from classes import TramStop
from tkinter_logic import *

def main():
    root = Tk()
    root.title("Tkinter Logic")
    root.geometry("400x400")

    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Jaki przystanek chcesz wyświetlić?").grid(column=0, row=0)

    searched_name = ttk.Entry(frm, width=30)
    
    searched_name.grid(column=1, row=0)  # Add this line to display the entry field
    
    tram_stop = TramStop(searched_name.get())
    
    ttk.Button(frm, text="Wyświetl", command=tram_stop.get_stop_info).grid(column=0, row=2)  # Change the button text and command
    ttk.Button(frm, text="Wyjście", command=root.destroy).grid(column=0, row=3)
    root.mainloop()
    
    
if __name__ == '__main__':
    main()    






 