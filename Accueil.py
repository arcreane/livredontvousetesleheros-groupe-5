from tkinter import *
import os

window = Tk()
window.title("Le livre dont vous êtes le héros")
window.geometry("900x600")
window.minsize(800, 240)
window.resizable()
frame = Frame(window)

frame.pack(side= TOP)

def startbck():
    os.system('python bck.py')
def startplay():
    os.system('python main.py')

frame_titre = Frame(window)
frame_titre.place(relx=0.5, rely = 0.1, anchor=CENTER)
titre = Label(frame_titre, text="Bienvenue sur l'application : Le livre dont vous êtes le héros", font=("Bahnschrift SemiBold", 20))
titre.pack()

frame = Frame(window)
frame.place(relx=0.5, rely=0.2, anchor=CENTER)
bluebutton = Label(frame, text="Pour créer ou éditer une nouvelle histoire, cliquez sur Éditer \n Pour jouer, cliquez sur Jouer", font=("Bahnschrift", 15))
bluebutton.pack()

frame2 = Frame(window)
frame2.place(relx=0.45, rely=0.5, anchor=CENTER)
greenbutton = Button(frame2, text="Jouer",font=("Bahnschrift", 15), command= startplay)
greenbutton.pack()

frame3 = Frame(window)
frame3.place(relx=0.55, rely=0.5, anchor=CENTER)

bluebutton = Button(frame3, text="Éditer", font=("Bahnschrift", 15), command=startbck)
bluebutton.pack()



frame.mainloop()
