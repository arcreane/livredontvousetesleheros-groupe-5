from tkinter import *






# Création de la fenêtre
jeu = Tk()
jeu.winfo_screenwidth()
jeu.winfo_screenheight()
jeu.geometry("900x600")


n.add(o2, text='Chapitre 2')  # Nom de l'onglet 2
#Les Frames
    #Frame o1
etiquette = Label(o1, text='Votre histoire :')
etiquette.pack(padx=5, pady=5)
etiquette.place(x=0, y=10)
etiquette.pack(padx=5, pady=5, side=TOP)
etiquette.place(x=5, y=00)

scrollbar = Scrollbar(o1)
texte_histoire = Text(o1, font=("Arial", 10), width=50, yscrollcommand=scrollbar.set)
scrollbar.config(command=texte_histoire.yview)

texte_histoire.place(x=0, y=0, height=50, width=50)
texte_histoire.pack(padx=5, pady=20)
scrollbar.pack(side=RIGHT, fill=Y)

entree = Entry(o1, font=("Arial", 10),width=5000)
entree.place(x=50, y=50, height=200, width=500000)
entree.pack(padx=5, pady=5, side=BOTTOM)

#Les boutons
    #Boutons onglet 1
Button(o1, text="Enregistrer",).pack()
Button(o1, text='Quitter', command=jeu.destroy).pack()
    #Boutons onglet 2
Button(o2, text='En attente', command=None).pack()

jeu.mainloop()