from tkinter import *

fenetre = Tk()

cadre = Frame(fenetre, width=50, height=30, borderwidth=1)
cadre.pack()

indication_nom = Label(cadre, text="Saisissez votre nom en majuscule")
indication_nom.pack()

nom = StringVar()
recuperation_nom = nom.get()
saisir_nom = Entry(cadre, textvariable=nom, width=50)
saisir_nom.pack()

afficher_nom = Label(cadre4, text="Nom: ")
afficher_nom.pack(side="left")

le_nom = Label(cadre4, text=recuperation_nom)
le_nom.pack(side="left")