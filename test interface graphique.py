from tkinter import *
#début des paramètres de la fenêtre
window = Tk()
window.title("Le livre d'on vous êtes le héros.")
window.geometry("1080x720")
window.minsize(480, 360)
window.maxsize(1920, 1080)
window.iconbitmap("Morellonomicon_Obj.ico")
window.config(background="grey")
#fin des paramètres de la fenêtre

#texte affichés
label = Label(window, text="Éditeur le livre d'on vous êtes le héros")
label.pack()

#début des paramètres des boutons
bouton_1 = Button(window, text="Chapitre suivant",)
bouton_2 = Button(window, text = "Quitter la partie", command = window.destroy) #bouton Quitter
bouton_1.pack()
bouton_2.pack()

# entrée
value = StringVar()
value.set("texte par défaut")
entree = Entry(window, width=30)
entree.pack()

window.mainloop()


#fin des paramètres des boutons

#début des chapitres
label_title = Label(window, text="Bienvenue sur notre nouveau jeu : 'Le livre d'on vous êtes le héros'", font =("Baskerville", 16), background ="#f0f0d1", foreground = "black" )

#fin des chapitres
window.mainloop()