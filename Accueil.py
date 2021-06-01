from tkinter import *
import main
import Nouveaulivre

window = Tk()
window.title("Le livre dont vous êtes le héros")
window.geometry("900x600")
window.minsize(800, 240)
window.resizable()
frame = Frame(window)

frame.pack(side= TOP)



frame = Frame(window)
frame.place(relx=0.5, rely=0.2, anchor=CENTER)
bluebutton = bluebutton = Label(frame, text="Bienvenue dans le jeu dont vous êtes le héros, Voulez vous éditer ou jouer a un livre ?")
bluebutton.pack()

frame2 = Frame(window)
frame2.place(relx=0.45, rely=0.5, anchor=CENTER)
greenbutton = Button(frame2, text="Jouer", command= main)
greenbutton.pack()

frame3 = Frame(window)
frame3.place(relx=0.55, rely=0.5, anchor=CENTER)

bluebutton = Button(frame3, text="Éditer", command=Nouveaulivre)
bluebutton.pack()



frame.mainloop()
