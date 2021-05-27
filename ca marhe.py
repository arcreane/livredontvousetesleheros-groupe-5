import json
import tkinter.ttk as ttk
import tkinter.filedialog
import os
import time
import glob
import tkinter as tk



window=tk.Tk()

window.minsize(650,260)
window.title('LDVELH')


frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

#frame1.grid(row=3, column=0, sticky="NESW")
window.geometry("1300x720")


def ishistoire(path):
    listelocate = []
    listelocate = glob.glob(path + "/*.json")

    if path + "\\specs.json" in listelocate and path + "\\persos.json" in listelocate and listelocate and path + "\\content.json" in listelocate:
        return(True)
    else :
        return(False)

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



printlist = []
ndlist = []



#t = Table(window,ndlist)
#Initialisation des variables tkinter
listeFichiers = listlivres()
listeFichiers.append("autre")
listeCombo = ttk.Combobox(frame1, values=listeFichiers)


def action(event):
    select = listeCombo.get()
    if select == "autre":
        text_files = tk.filedialog.askdirectory(title = "Selectionnez un dossier", mustexist = True, initialdir = os.path.expanduser('~/Documents'))
        if ishistoire(text_files):
            play(text_files)
            frame1.pack_forget()
    else :
        play(select)




#Jeu

def play(chemin):


    with open(chemin+"/persos.json") as f:
      persos = json.load(f)
    with open(chemin+"/specs.json") as f:
      specs = json.load(f)
    with open(chemin+"/content.json") as f:
      content = json.load(f)

    state= True
    i= 0
    listecontenu = []
    for key,val in content.items():
        listecontenu.append(val)

    title_label = tk.Label(frame2, text = listecontenu[i][0])
    # .grid(column = 1, row = 0, sticky = 'E'+'W')

    title_label.config(anchor="center")
    title_label.grid(row = 0, column = 1)
    frame2.grid(row = 3, column = 3)
    print("test")





#accueil()
play("C:/Users/maxim/Documents/GitHub/livredontvousetesleheros-groupe-5/livres/livre 1")
window.mainloop()