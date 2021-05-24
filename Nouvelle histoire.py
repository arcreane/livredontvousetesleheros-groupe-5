## Onglets

from tkinter import *
from tkinter import ttk

# Toutes les def
def afficheZoneSaisie():
    global entree
    zoneSaisie = entree.get()
    print('Votre mot de passe secret est : '+zoneSaisie)
    # return inutile : modification d'une variable globale
def enreg():
    "Enregistrer le fichier"
    obfichier = open('fichier','a')
    if entr1.get():
        obfichier.write(entr1.get()+'\n')
    obfichier.close()

# Création de la fenêtre
jeu = Tk()
jeu.winfo_screenwidth()
jeu.winfo_screenheight()
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
etiquette.pack(padx=5, pady=5, side=TOP)
etiquette.place(x=5, y=00)

scrollbar = Scrollbar(o1)
texte_histoire = Text(o1, font=("Arial", 10), width=50, yscrollcommand=scrollbar.set)
scrollbar.config(command=texte_histoire.yview)

texte_histoire.place(x=0, y=0, height=50, width=50)
texte_histoire.pack(padx=5, pady=20)
scrollbar.pack(side=RIGHT, fill=Y)


#Les boutons
    #Boutons onglet 1
Button(o1, text="Enregistrer",).pack()
Button(o1, text='Quitter', command=jeu.destroy).pack()
    #Boutons onglet 2
Button(o2, text='En attente', command=None).pack()

jeu.mainloop()