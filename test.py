from tkinter import *
def enreg():
    "Enregistrer le fichier"
    obfichier = open('fichier','a')
    if entr1.get():
        obfichier.write(entr1.get()+'\n')
    obfichier.close()

fen1 = Tk()
fen1.title("Gestion des membres du club")
tex1 = Label(fen1, text = 'Nom')
entr1 = Entry(fen1)
tex1.grid(row = 0, column = 0)
entr1.grid(row = 0, column = 1)
bou1 = Button(fen1, text = 'Quitter', command = fen1.quit)
bou1.grid(row = 1, column = 1)
bou2 = Button(fen1, text = 'Enregistrer', command = enreg)
bou2.grid(row = 1, column = 0)
fen1.mainloop()
fen1.destroy()