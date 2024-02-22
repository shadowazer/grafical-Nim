import pygame_testing
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Mängulaua laius:").grid(column=0, row=3)
ttk.Label(frm, text="Mängulaua pikkus:").grid(column=0, row=5)
ttk.Label(frm, text="ruutu").grid(column=2, row=3)
ttk.Label(frm, text="ruutu").grid(column=2, row=5)
e1 = Entry(frm)
e1.grid(column=1, row=3)
e2 = Entry(frm)
e2.grid(column=1, row=5)

error1 = ttk.Label(frm, text="Sisesta korrektne number!", foreground="Red")
error2 = ttk.Label(frm, text="Sisesta korrektne number!", foreground="Red")
def startgame():
    a = e1.get()
    b = e2.get()
    valid = True
    if not a.isnumeric():
        error1.grid(column=0, row=2)
        valid = False
    else:
        error1.grid_remove()
    if not b.isnumeric():
        error2.grid(column=0, row=4)
        valid = False
    else:
        error2.grid_remove()

    if not valid:
        return
    root.destroy()
    pygame_testing.main(int(a), int(b))


ttk.Button(frm, text="Start", command=startgame).grid(column=1, row=6)

root.mainloop()