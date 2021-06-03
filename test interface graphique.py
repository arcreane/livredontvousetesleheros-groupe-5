#!/usr/bin/env python

# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import filedialog
import tkinter.filedialog
import os
# Toutes les def
<<<<<<< HEAD
=======
"""def nouvellehistoire():
    filetypes = (("py files", "*.py"), ("All files", "*.*"))
    file_name = filedialog.askopenfilename(title="Selectionnez le fichier", filetypes=filetypes)
    print(file_name)"""
>>>>>>> 87d686129b448bc30a0b89a35dc35006ff05608e

def create():
    win = Toplevel(fen_princ)
    win.update()
    filetypes = (("text files", "*.txt"),("All files", "*.*"))
    file_name = filedialog.askopenfilename(initialdir = "/",title = "Selectionnez le fichier",filetypes = filetypes)
    print(file_name)


# Création de la fenêtre
fen_princ = Tk()
fen_princ.title("Le livre dont vous êtes le héros")
fen_princ.geometry("900x600")
fen_princ.minsize(800, 240)
fen_princ.resizable()



# 1 - Bandeau du haut
    # Création du cadre-conteneur pour les menus
zoneMenu = Frame(fen_princ, borderwidth=3, bg='#557788')
zoneMenu.pack(fill=X)


    # Création de l'onglet Fichier
menuFichier = Menubutton(zoneMenu, text='Fichier', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
menuFichier.grid(row=0, column=0)


    # Création de l'onglet Écriture d'une nouvelle histoire
menunouvellehistoire = Menubutton(zoneMenu, text='Nouvelle Histoire', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
menunouvellehistoire.grid(row=0,column=1)


    # Création de l'onglet Écriture d'une histoire déjà commencé
menuhistoire = Button(zoneMenu, text="Continuer l'écriture", width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED, command = tkinter.filedialog.askopenfilename)
menuhistoire.grid(row=0,column=2)

    # Création de l'onglet Jouer
menujouer = Button(zoneMenu, text='Jouer', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED, command = tkinter.filedialog.askopenfilename)
menujouer.grid(row=0,column=3)

    # Création de l'onglet Quitter
menuquitter = Button(zoneMenu, text='Quitter', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED, command=fen_princ.destroy)
menuquitter.grid(row=0,column=9)

    # Création d'un menu défilant
        #Menu déroulant du bouton fichier
menuDeroulant1 = Menu(menuFichier)
menuDeroulant1.add_command(label="Nouvelle histoire")
menuDeroulant1.add_command(label="Continuer l'écriture", command = tkinter.filedialog.askopenfilename)
menuDeroulant1.add_command(label="Jouer", command = menujouer)
menuDeroulant1.add_command(label="Quitter", command = fen_princ.destroy)

        #Menu déroulant du bouton nouvelle histoire
menuDeroulant2 = Menu(menunouvellehistoire)
menuDeroulant2.add_command(label="5 Chapitres",command = tkinter.filedialog.askopenfilename() )


    # Attribution du menu déroulant aux différents menus
menuFichier.configure(menu=menuDeroulant1)
menunouvellehistoire.configure(menu=menuDeroulant2)
# 2 - Coeur de la fenêtre
    # boite
frame_titre_et_sous_titre = Frame(fen_princ)
    # titre fenêtre de démarrage
label_titre = Label(frame_titre_et_sous_titre, text="Bienvenue sur l'application", foreground="black", font=("Arial", 40))
label_titre.pack()

label_sous_titre = Label(frame_titre_et_sous_titre, text="Pour créer une nouvelle histoire, clique sur nouvelle histoire \n Pour reprendre l'écriture d'une histoire, clique sur continuer l'écriture \n Pour jouer à une histoire, clique sur jouer", foreground="black", font=("Arial", 16))
label_sous_titre.pack()

    # ajout boite
frame_titre_et_sous_titre.pack(expand=YES)








# Lancement de la surveillance sur la fenêtre
fen_princ.mainloop()