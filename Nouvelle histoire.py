## Onglets

from tkinter import *
from tkinter import ttk

# Toutes les def
def afficheZoneSaisie():
    global entree
    zoneSaisie = entree.get()
    print('Votre mot de passe secret est : '+zoneSaisie)
    # return inutile : modification d'une variable globale


# Création de la fenêtre
jeu = Tk()
jeu.geometry("900x600")
jeu.resizable(0, 0)

#Les onglets + frames
n = ttk.Notebook(jeu)  # Création du système d'onglets
n.pack()

    #Onglet 1
o1 = Frame(n)  # Ajout de l'onglet 1

o1.pack()
n.add(o1, text='Chapitre 1')  # Nom de l'onglet 1


    #Onglet 2
o2 = Frame(n)  # Ajout de l'onglet 2
o2.pack()
n.add(o2, text='Chapitre 2')  # Nom de l'onglet 2


#Les boutons
Button(o1, text='Quitter', command=jeu.destroy).pack()
Button(o2, text='En attente', command=None).pack()

#Les Frames
    #Frame o1
etiquette = Label(o1, text='Votre histoire :')
etiquette.pack(padx=5, pady=5)
etiquette.place(x=0, y=10)

entree = Entry(o1, width=50, font=("Elvetica", 12))
entree.place(height=100, width=500)
entree.pack(padx=5, pady=5)
entree.focus_force()

jeu.mainloop()