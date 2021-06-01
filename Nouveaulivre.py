import json
import tkinter.ttk as ttk
import tkinter.filedialog
import tkinter.messagebox
import os

import glob
import tkinter as tk



window=tk.Tk()

window.minsize(650,260)
window.title('LDVELH')

content= ""
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

#frame1.grid(row=3, column=0, sticky="NESW")
window.geometry("1300x720")
def alertwindow():
    MsgBox = tk.messagebox.askquestion('Conflit de fichiers', 'Êtes vous sur de vouloir écraser un livre déjà exisatnt ?',
                                       icon='warning')
    if MsgBox == 'yes':
        print("allesgut")
    else:
        tk.messagebox.showinfo('Return', 'You will now return to the application screen')
def load(chemin):
    global persos, specs,content
    with open(chemin + "/persos.json") as f:
        persos = json.load(f)
    with open(chemin + "/specs.json") as f:
        specs = json.load(f)
    with open(chemin + "/content.json") as f:
        content = json.load(f)
def boutondechoix(content, i,chemin):
    boutons = []
    for o in range(len(content[str(i)][3])):
        boutons.append(tk.Button(frame3, text=content[str(i)][3][o][1], command=lambda x=content[str(i)][3][o][0]: choixdelacarte(x,chemin)))
    return(boutons)
def choixdelacarte(x,chemin):

    play(chemin,x)

def choixduperso(x):
    global perso
    perso = x

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
    title_label = tk.Label(frame1, text= "Bienvenue dans l'édieur du Jeu Dont Vous Êtes Le Héros : \n"
                   "Sélectionenez votre histoire déjà existante dans la liste ou sélectionnez Créer un nouveau livre pour choisir un autre emplacement sur votre disque pour en créer une nouvelle\n\n\n\n",wraplength = 600)
        #.grid(column = 1, row = 0, sticky = 'E'+'W')

    title_label.config(anchor="center")
    title_label.pack(fill="y")

    listeCombo.current(0)
    listeCombo.pack(fill="y")

    #tk.Label(frame1, text= "\n \n\n\n\n").grid(column = 0, row = 2, sticky = "EW")
    listeCombo.bind("<<ComboboxSelected>>", action)
    frame1.pack(expand = "True")





#Initialisation des variables tkinter
listeFichiers = listlivres()
listeFichiers.append("Créer un nouveau livre")
listeCombo = ttk.Combobox(frame1, values=listeFichiers)


def action(event):
    select = listeCombo.get()
    if select == "Créer un nouveau livre":
        text_files = tk.filedialog.askdirectory(title = "Selectionnez un dossier", mustexist = True, initialdir = os.path.expanduser('~/Documents'))
        if not(ishistoire(text_files)):
            frame1.pack_forget()
            print("proutf")
            newbook(text_files)
        else :
            alertwindow()
    else :
        print("prout2")
        frame1.pack_forget()

def ajouterchapitre():
    content[str(len(content))] = [[f"Titre du chapitre {str(len(content))}","Texte du chapitre"],0,0,[[],"P", "False"]]

#Éditeur
def newbook(chemin):
    f = open(chemin + "/specs.json", "w")
    f = open(chemin + "/persos.json", "w")
    f = open(chemin + "/content.json", "w")
    editor3000(chemin)

def editor3000(chemin):
    global frame2, frame3, perso
    frame2.destroy()
    frame3.destroy()
    load(chemin)
    frame = tk.Frame(window)
    frameleft = tk.Frame(window)
    frametright = tk.Frame(window)
    framecenter= tk.Frame(frame)
    framebright= tk.Frame(window)
    leftcolumn = tk.Frame(frameleft)
    frame.grid(column = 3, row = 5, sticky ="nsew")
    mylabel = tk.Label(frame, text='Liste des chapitres', font="30")
    mylabel.grid(column = 0, row = 0)

    myscroll = tk.Scrollbar(frame)


    mylist = tk.Listbox(frame, yscrollcommand=myscroll.set)
    for line in range(len(content)):
        mylist.insert(tk.END, content[str(line)][0][0])
    mylist.grid(column = 0, row = 1, rowspan= 4, sticky ="ew")
    myscroll.grid(column = 0, row = 1, sticky='nsew')
    addchapitre = tk.Button(frame, text= "Ajouter un chapitre", command= ajouterchapitre)
    addchapitre.grid( sticky ="ew")



    scrollbar = tk.Scrollbar(framecenter)
    texte_histoire = tk.Text(framecenter, font=("Arial", 10), width=50, yscrollcommand=scrollbar.set)
    scrollbar.config(command=texte_histoire.yview)

    texte_histoire.place(x=0, y=0, height=50, width=50)
    texte_histoire.grid(row=0,column = 0, sticky ="ew")
    scrollbar.grid(row=0, column = 1, sticky='ns')
    framecenter.grid(column = 1, row = 0, rowspan=3, sticky = "nsew")


    def get_entry_text():
        print(texte_histoire.get())
        tk.Label.configure(text=texte_histoire.get())

    button = tk.Button(frame, text='get entry', command=get_entry_text)
    button.grid(column = 1, row = 3, sticky ="ew")

    myscroll.config(command=mylist.yview)
    frameleft.grid(column = 0, row = 1, sticky='ew')










#accueil()
editor3000("C:/Users/maxim/Documents/GitHub/livredontvousetesleheros-groupe-5/livres/livre 1")
window.mainloop()