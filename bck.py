import json
import tkinter.ttk as ttk
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk
import os

import glob
import tkinter as tk



window=tk.Tk()

window.minsize(650,400)
window.title('LDVELH')

content= ""
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

#frame1.grid(row=3, column=0, sticky="NESW")
window.geometry("1300x720")
def alertwindow(motif):
    if motif == "conflifichiers" :
        MsgBox = tk.messagebox.askquestion('Conflit de fichiers', 'Êtes vous sur de vouloir écraser un livre déjà exisatnt ?',
                                           icon='warning')
        if MsgBox == 'yes':
            print("allesgut")
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
            alertwindow("conflifichiers")
    else :
        print("prout2")
        frame1.pack_forget()

def ajouterchapitre():
    global chaplist
    content[str(len(content))] = [[f"Titre du chapitre {str(len(content)+1)}","Texte du chapitre"],0,0,[[],"C", "False"]]
    chaplist.delete(0, tk.END)
    for line in range(len(content)):
        chaplist.insert(tk.END, content[str(line)][0][0])
def editerchapitre():
    global chaplist
    try :
        select = chaplist.get(chaplist.curselection())
        print(select)
    except:
        print("No selected values")
#Éditeur
def newbook(chemin):
    f = open(chemin + "/specs.json", "w")
    f = open(chemin + "/persos.json", "w")
    f = open(chemin + "/content.json", "w")
    editor3000(chemin)

def destroyframes(framelist):
    for i in range(0,len(framelist)):
        try:
            framelist[i].destroy()
        except:
            print("nop")

def editor3000(chemin,chapitre = 0):
    global frame2, frame3, perso, chaplist
    frame2.destroy()
    frame3.destroy()
    load(chemin)
    frameleft = tk.Frame(window)
    frameright = tk.Frame(window)
    framecenter= tk.Frame(window)
    frameright= tk.Frame(window)
    leftcolumn = tk.Frame(frameleft)
    rightcolumn= tk.Frame(frameright)
    frametopcenter = tk.Frame(framecenter)
    framebottomcenter = tk.Frame(framecenter)



    frameleft.pack(side="left", fill =tk.Y)

    myscroll2 = tk.Scrollbar(rightcolumn)
    myscroll2.pack(side=tk.RIGHT, fill=tk.Y)

    mylist1 = tk.Listbox(rightcolumn, yscrollcommand=myscroll2.set)
    myscroll2.config(command=mylist1.yview)
    for line in range(1,len(specs["objets"])+1):
        mylist1.insert(tk.END, specs["objets"][str(line)][0])
    mylist1.pack(side=tk.TOP, fill=tk.BOTH)
    rightcolumn.pack(side = tk.TOP, fill = tk.Y)




    v = tk.StringVar(rightcolumn, "1")


    values = {"Histoire": "H",
              "Combat": "C"}

    for (text, value) in values.items():
        boutons = tk.Radiobutton(rightcolumn, text=text, variable=v,
                    value=value,tristatevalue=0)
        boutons.select()
        boutons.pack(side=tk.TOP, ipady=5, fill = tk.Y)

    frameright.pack(side = tk.RIGHT, fill = tk.Y)

    mylabel = tk.Label(leftcolumn, text='Liste des chapitres', font="30")
    mylabel.pack()

    myscroll = tk.Scrollbar(leftcolumn)
    myscroll.pack(side=tk.RIGHT, fill=tk.Y)

    chaplist = tk.Listbox(leftcolumn, yscrollcommand=myscroll.set)
    for line in range(len(content)):
        chaplist.insert(tk.END, content[str(line)][0][0])
        chaplist.configure( selectmode = tk.SINGLE)
    chaplist.pack(side=tk.TOP, fill=tk.Y)

    addchapitre = tk.Button(leftcolumn, text= "Ajouter un chapitre", command= ajouterchapitre)
    addchapitre.pack(fill=tk.X)
    editchapitre = tk.Button(leftcolumn, text= "Editer le chapitre", command= editerchapitre)
    editchapitre.pack(fill=tk.X)

    leftcolumn.pack(side = tk.TOP, fill=tk.Y)
    frameleft.pack(side =tk.LEFT, fill=tk.Y)
    framecenter.pack( fill = tk.BOTH)

    titreduchapitre = tk.Entry(frametopcenter)
    titreduchapitre.insert(1,content[str(chapitre)][0][0])
    titreduchapitre.pack(fill = tk.X, padx = 10)

    scrollbar3 = tk.Scrollbar(frametopcenter)
    texte_histoire = tk.Text(frametopcenter, font=("Arial", 10), width=50, yscrollcommand=scrollbar3.set)

    scrollbar3.config(command=texte_histoire.yview)

    texte_histoire.place(height=50, width=50)
    scrollbar3.pack(side = tk.RIGHT, fill=tk.Y)
    texte_histoire.insert(1.0,content[str(chapitre)][0][1])
    texte_histoire.pack(side=tk.TOP, fill=tk.BOTH, padx = 10)

    frametopcenter.pack(fill = tk.BOTH)

    def get_entry_text():
        print(texte_histoire.get(1.0,"end-1c"))


    button = tk.Button(framecenter, text='get entry', command=get_entry_text)
    button.pack(pady=10)




    redirchap1 = tk.Entry(framebottomcenter)
    redirchap2 = tk.Entry(framebottomcenter)
    redirchap3 = tk.Entry(framebottomcenter)
    redirchap1.insert(1,f"{content[str(chapitre)][3][0][0]}" )
    redirchap2.insert(1,f"{content[str(chapitre)][3][1][0]}" )
    redirchap3.insert(1,f"{content[str(chapitre)][3][2][0]}" )
    redirchap1.pack()
    redirchap2.pack()
    redirchap3.pack()
    framebottomcenter.pack()
    framecenter.pack()










#accueil()
editor3000("C:/Users/maxim/Documents/GitHub/livredontvousetesleheros-groupe-5/livres/livre 1")
window.mainloop()

