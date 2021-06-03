import json
import tkinter.ttk as ttk
import tkinter.filedialog
import tkinter.font as tkFont
import os

import glob
import tkinter as tk


#initialisation de tkinter
window=tk.Tk()

window.minsize(650,260)
window.title('LDVELH')

content= ""
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

#
window.geometry("1300x720")
#charge les json dans des dicts
def load(chemin):
    global persos, specs,content
    with open(chemin + "/persos.json") as f:
        persos = json.load(f)
    with open(chemin + "/specs.json") as f:
        specs = json.load(f)
    with open(chemin + "/content.json") as f:
        content = json.load(f)
#choix des parties de l"histoire
def boutondechoix(content, i,chemin):
    boutons = []
    for o in range(len(content[str(i)][3])):
        boutons.append(tk.Button(frame3, text=content[str(i)][3][o][1], command=lambda x=content[str(i)][3][o][0]: choixdelacarte(x,chemin)))
    return(boutons)

#lance le chemin choisi (retrospéctivement : pourrait etre fait avec une focntion lambda)
def choixdelacarte(x,chemin):

    play(chemin,x)
#selctionne le personnage a (retrospéctivement : pourrait etre fait avec une focntion lambda)
def choixduperso(x):
    global perso
    perso = x
#vérifie que le chemin donné est bien un histoire( ne vérfie pas le contenu des fichiers, juste si ils existent)
def ishistoire(path):
    listelocate = []
    listelocate = glob.glob(path + "/*.json")

    if path + "\\specs.json" in listelocate and path + "\\persos.json" in listelocate and listelocate and path + "\\content.json" in listelocate:
        return(True)
    else :
        return(False)
#liste les livres dans le chemin par défaut ici ./livres/
def listlivres():
    path = "./livres/"
    retour = []
    listefichiers = []
    text_files = glob.glob(path + "/**/content.json", recursive = True)
    for i in range(0, len(text_files)):
        listelocate = glob.glob((text_files[i].replace("content.json", "")+"*.json"), recursive = True)
        if text_files[i]in listelocate and text_files[i].replace("content.json", "")+"specs.json".replace("/","\\")in listelocate and text_files[i].replace("content.json", "")+"persos.json".replace("/","\\") in listelocate :
            retour.append((text_files[i].replace("content.json", "")))
    return(retour)
#Selection du livre
def accueil():
    title_label = tk.Label(frame1, text= "Bienvenue dans Le Jeu Dont Vous Êtes Le Héros : \n"
                   "Sélectionenez votre histoire dans la liste ou selectionner autre pour choisir un autre emplacement sur votre disque \n\n\n\n")
        #.grid(column = 1, row = 0, sticky = 'E'+'W')

    title_label.config(anchor="center")
    title_label.pack(fill="y")

    listeCombo.current(0)
    listeCombo.pack(fill="y")

    #tk.Label(frame1, text= "\n \n\n\n\n").grid(column = 0, row = 2, sticky = "EW")
    listeCombo.bind("<<ComboboxSelected>>", action)
    frame1.pack(expand = "True")





#Initialisation des variables tkinter#2
listeFichiers = listlivres()
listeFichiers.append("autre")
listeCombo = ttk.Combobox(frame1, values=listeFichiers)

#action du combobox de accueil
def action(event):
    select = listeCombo.get()
    if select == "autre":
        text_files = tk.filedialog.askdirectory(title = "Selectionnez un dossier", mustexist = True, initialdir = os.path.expanduser('~/Documents'))
        if ishistoire(text_files):
            frame1.pack_forget()
            play(text_files)
    else :
        frame1.pack_forget()
        play(select)


#Jeu

def play(chemin,i=0):
    global frame2, frame3, perso
    frame2.destroy()
    frame3.destroy()
    frame2 = tk.Frame(window)
    frame3 = tk.Frame(window)

    if i == 0 :
        load(chemin)
    if content[str(i)][4] == "H" :
        policeTitre = tkFont.Font(family="Lucida Grande", size=20)
        boutonsduchp = boutondechoix(content, i,chemin)
        titre_label = tk.Label(frame2, text = content[str(i)][0][0],font=policeTitre)
        titre_label.pack(side="top")
        title_label = tk.Label(frame2, text = content[str(i)][0][1])
        title_label.pack(side="left")
        for choix in range(len(boutonsduchp)):
            boutonsduchp[choix].pack(fill="x")
            frame3.pack(side= "bottom",padx=20, pady=20,expand= "yes")
        frame2.pack(padx=20, pady=20,expand= "yes")
    elif content[str(i)][4] == "P" :
        boutons = []
        policeTitre = tkFont.Font(family="Lucida Grande", size=20)
        titre_label = tk.Label(frame2, text = content[str(i)][0][0],font=policeTitre)
        titre_label.pack(side="top")
        title_label = tk.Label(frame2, text = content[str(i)][0][1])
        title_label.pack()

        for o in range(0,len(persos)):
            boutons = []
            boutons.append(tk.Button(frame3, text=list(persos.keys())[o],
                                     command=lambda x=content[str(i)][3][o][0]: choixdelacarte(x, chemin)))
            frame3.pack(side="bottom", padx=20, pady=20, expand="yes")
        for choix in range(len(boutons)):
            boutons[choix].pack(fill="x")
            frame3.pack(side= "bottom",padx=20, pady=20,expand= "yes")
        frame2.pack(padx=20, pady=20,expand= "yes")



accueil()
#permet de lancer le jeu sans passer par laccueil
#play("C:/Users/maxim/Documents/GitHub/livredontvousetesleheros-groupe-5/livres/livre 1")
window.mainloop()