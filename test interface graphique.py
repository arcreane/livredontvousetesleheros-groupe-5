from tkinter import *
#début des paramètres de la fenêtre
window = Tk()
window.title("Le livre d'on vous êtes le héros.")
window.geometry("1080x720")
window.minsize(480, 360)
window.maxsize(1920, 1080)
window.iconbitmap("Morellonomicon_Obj.ico")
window.config(background="#f0f0d1")
#fin des paramètres de la fenêtre

#début des paramètres des boutons
bouton_1 = Button(window, text="Chapitre suivant",)
bouton_2 = Button(window, text = "Quitter la partie", command = window.destroy) #bouton Quitter
bouton_1.pack()
bouton_2.pack()

fenetre.mainloop()


#fin des paramètres des boutons

#début des chapitres
label_title = Label(window, text="Bienvenue sur notre nouveau jeu : 'Le livre d'on vous êtes le héros'", font =("Baskerville", 16), background ="#f0f0d1", foreground = "black" )

#fin des chapitres
window.mainloop()
