## Onglets

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import tkinter.filedialog
import os

# Toutes les def
def afficheZoneSaisie():
    global entree
    zoneSaisie = entree.get()
    print('Votre mot de passe secret est : '+zoneSaisie)
    # return inutile : modification d'une variable globale
def clean_exit():
    root.destroy()


def alternate_window(is_in_root, is_in_window, window):
    def alternate_processing():
        if is_in_root and not is_in_window:
            root.withdraw()
            window.deiconify()
        else:
            window.withdraw()
            root.deiconify()

    return alternate_processing


def create_window(window, text_label):
    label = tk.Label(window, text=text_label)
    button = tk.Button(window, text="Revenir vers root", command=alternate_window(False, True, window))
    label.grid(column=0, row=0)
    button.grid(column=0, row=1)
    window.protocol("WM_DELETE_WINDOW", clean_exit)


# Création de la fenêtre
window = tk.Tk()
window.winfo_screenwidth()
window.winfo_screenheight()
window.geometry("900x600")




    #Onglet 1
o1 = tk.Frame()  # Ajout de l'onglet 1
o1.pack()



    #Onglet 2
o2 = tk.Frame()  # Ajout de l'onglet 2
o2.pack()





#Les Frames
    #Frame o1
etiquette = tk.Label(o1, text='Votre histoire :')
etiquette.pack(padx=5, pady=5,)
etiquette.place(x=5, y=00)

scrollbar = tk.Scrollbar(o1)
texte_histoire = tk.Text(o1, font=("Arial", 10), width=50, yscrollcommand=scrollbar.set)
scrollbar.config(command=texte_histoire.yview)

texte_histoire.place(x=0, y=0, height=50, width=50)
texte_histoire.pack(padx=5, pady=20)
scrollbar.pack()


#Les boutons
    #Boutons onglet 1
tk.Button(o1, text="Enregistrer").pack()
tk.Button(o1, text='Quitter', command=window.destroy).pack()
    #Boutons onglet 2
tk.Button(o2, text='En attente', command=None).pack()

#Frame sur la gauche permettant de relier les chapitres entre eux
zone_reliant_les_chapitres_entre_eux = tk.Frame(o1, borderwidth=1,)
zone_reliant_les_chapitres_entre_eux.pack(padx=10,pady=10)
#Frame qui configure vers quel chapitre ca va
menu_chapitre_suivant = tk.Menubutton(zone_reliant_les_chapitres_entre_eux, text='Relier aux chapitre...', width='20', borderwidth=2, bg='gray', activebackground='darkorange',)
menu_chapitre_suivant.pack()
menu_deroulant_chapitre_suivant = tk.Menu(menu_chapitre_suivant)
menu_deroulant_chapitre_suivant.add_command(label="n°1")
menu_chapitre_suivant.configure(menu=menu_deroulant_chapitre_suivant)
#Boutons que le joueur pourra cocher
value = tk.StringVar()
choix1 = tk.Radiobutton(zone_reliant_les_chapitres_entre_eux, text="Avoir des dents en bois", variable=value, value=1)
choix2 = tk.Radiobutton(zone_reliant_les_chapitres_entre_eux, text="Avoir des jambes en mousse", variable=value, value=2)







window.mainloop()