## Onglets

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import tkinter.filedialog
from tkinter import scrolledtext

import os

# Toutes les def
def afficheZoneSaisie():
    global entree
    zoneSaisie = entree.get()
    # return inutile : modification d'une variable globale



def clean_exit():
    window.destroy()

def alternate_window(is_in_root, is_in_window, window):
    def alternate_processing():
        if is_in_root and not is_in_window:




def alternate_window(is_in_window, is_in_root, window):
    def alternate_processing():
        if is_in_root and not is_in_root:

            window.withdraw()
            window.deiconify()
        else:
            window.withdraw()
            window.deiconify()

    return alternate_processing


def create_window(window, text_label):
    label = tk.Label(window, text=text_label)
    button = tk.Button(window, text="Revenir vers window", command=alternate_window(False, True, window))
    label.grid(column=0, row=0)
    button.grid(column=0, row=1)
    window.protocol("WM_DELETE_WINDOW", clean_exit)


# Création de la fenêtre
window = tk.Tk()

window.geometry("900x600")




#Les Frames
    #Frame preview chapitre
chapitre = tk.Label(window, text="Les chapitres")
chapitre.pack()
chapitre.place(x=0, y=0)
    #Frame chapitre
etiquette = tk.Label(window, text='Votre histoire :')
etiquette.pack(padx=5, pady=5,)
etiquette.place(x=270, y=00)


texte_histoire = tk.scrolledtext.ScrolledText(window, font=("Arial", 10), width=50)
texte_histoire.place(relx=0.1, rely=0.5)


texte_histoire.place(x=500,height=50, width=50)
texte_histoire.pack(padx=0, pady=20)


#Les boutons
    #Boutons onglet 1
boutton_enregistrer = tk.Button(window, text="Enregistrer")
boutton_enregistrer.place()
boutton_enregistrer.pack()
tk.Button(window, text='Quitter', command=window.destroy).pack()


#Frame sur la gauche permettant de relier les chapitres entre eux
zone_reliant_les_chapitres_entre_eux = tk.Frame(window, borderwidth=1,)
zone_reliant_les_chapitres_entre_eux.place(x=700, y=80)

#Frame qui configure vers quel chapitre ca va
menu_chapitre_suivant = tk.Menubutton(zone_reliant_les_chapitres_entre_eux, text='Relier au chapitre...', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief=tk.RAISED)
menu_chapitre_suivant.pack()
menu_deroulant_chapitre_suivant = tk.Menu(menu_chapitre_suivant)
menu_deroulant_chapitre_suivant.add_command(label="n°1")
menu_chapitre_suivant.configure(menu=menu_deroulant_chapitre_suivant)

#Bouton pour ajouter un chapitre

"""o3 = tk.Frame(window)
o3.pack(side = "left")

creationdechapitre = tk.Button(o3,width = 30)
creationdechapitre.pack()
"""

bottomframe = tk.Frame(window)
bottomframe.pack( side = tk.BOTTOM )
blackbutton = tk.Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = tk.BOTTOM)



window.mainloop()