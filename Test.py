from tkinter import*

fenetre = Tk()

fenetre.title("JEU")

#Canevas
canevas = Canvas(fenetre, width=1280, height=1280, background="green")

bouton_quitter = Button(fenetre, text="Quitter", command = fenetre.quit)
bouton_quitter.pack()

Nom = Entry(fenetre)
Nom.pack()

canevas.pack()

canevas.create_text(640, 640, text="Début du jeu",fill="blue",font="Arial 20")

fenetre.mainloop()