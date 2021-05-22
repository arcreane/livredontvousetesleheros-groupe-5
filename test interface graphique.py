#!/usr/bin/env python

# -*- coding: utf-8 -*-

from tkinter import *

# Toutes les def
def create():
    win = Toplevel(fen_princ)


# Création de la fenêtre
fen_princ = Tk()
fen_princ.title("Le livre dont vous êtes le héros")
fen_princ.geometry("900x600")
fen_princ.resizable(0, 0)



# 1 - Bandeau du haut
    # Création du cadre-conteneur pour les menus
zoneMenu = Frame(fen_princ, borderwidth=3, bg='#557788')
zoneMenu.pack(fill=X)


    # Création de l'onglet Fichier
menuFichier = Menubutton(zoneMenu, text='Fichier', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
menuFichier.grid(row=0,column=0)


    # Création de l'onglet Écriture d'une nouvelle histoire
menunouvellehistoire = Button(zoneMenu, text='Nouvelle Histoire', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED, command = create)
menunouvellehistoire.grid(row=0,column=1)


    # Création de l'onglet Écriture d'une histoire déjà commencé
menuhistoire = Button(zoneMenu, text="Continuer l'écriture", width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
menuhistoire.grid(row=0,column=2)

    # Création de l'onglet Jouer
menujouer = Button(zoneMenu, text='Jouer', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
menujouer.grid(row=0,column=3)

    # Création de l'onglet Quitter
menuquitter = Button(zoneMenu, text='Quitter', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED, command=fen_princ.destroy)
menuquitter.grid(row=0,column=9)

    # Création d'un menu défilant
menuDeroulant1 = Menu(menuFichier)
menuDeroulant1.add_command(label="Nouvelle histoire")
menuDeroulant1.add_command(label="Ouvrir une histoire",)
menuDeroulant1.add_command(label="Jouer")
menuDeroulant1.add_command(label="Quitter", command = fen_princ.destroy)


    # Attribution du menu déroulant au menu Affichage
menuFichier.configure(menu=menuDeroulant1)

# 2 - Coeur de la fenêtre
    # boite
frame_titre_et_sous_titre = Frame(fen_princ)
    # titre fenêtre de démarrage
label_titre = Label(frame_titre_et_sous_titre, text="Bienvenue sur l'application", foreground="black", font=("Arial", 40))
label_titre.pack(expand=YES)

label_sous_titre = Label(frame_titre_et_sous_titre, text="Pour créer une nouvelle histoire, clique sur nouvelle histoire \n Pour reprendre l'écriture d'une histoire, clique sur continuer l'écriture \n Pour jouer à une histoire, clique sur jouer", foreground="black", font=("Arial", 16))
label_sous_titre.pack(expand=YES)

    # ajout boite
frame_titre_et_sous_titre.pack(expand=YES)








# Lancement de la surveillance sur la fenêtre
fen_princ.mainloop()