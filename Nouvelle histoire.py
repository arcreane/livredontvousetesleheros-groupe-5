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


#Les onglets + frames
n = ttk.Notebook(jeu, width=900, height=600)  # Création du système d'onglets

n.pack()

    #Onglet 1
o1 = Frame()  # Ajout de l'onglet 1
o1.pack()
n.add(o1, text='Chapitre 1')  # Nom de l'onglet 1


    #Onglet 2
o2 = Frame()  # Ajout de l'onglet 2
o2.pack(expand=YES)
n.add(o2, text='Chapitre 2')  # Nom de l'onglet 2




#Les Frames
    #Frame o1
etiquette = Label(o1, text='Votre histoire :')
etiquette.pack(padx=5, pady=5)
etiquette.place(x=0, y=10)


entree = Entry(o1, font=("Arial", 10),width=5000)
entree.place(x=50, y=50, height=200, width=500000)
entree.pack(padx=5, pady=5, side=BOTTOM)

#Les boutons
Button(o1, text='Quitter', command=jeu.destroy).pack()
Button(o2, text='En attente', command=None).pack()

jeu.mainloop()