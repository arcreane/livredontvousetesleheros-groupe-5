from tkinter import *


def faireApparaitreLeToplevel():
    top = Toplevel(root)
    lab = Label(top, text="Ce soir je vais manger des frites")
    lab.pack()


root = Tk()
go = Button(root, text="lancer", command=faireApparaitreLeToplevel)
go.pack()
root.mainloop()