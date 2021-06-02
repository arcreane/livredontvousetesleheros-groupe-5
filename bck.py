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
        MsgBox = tk.messagebox.askquestion('Conflit de fichiers', 'Êtes vous sur de vouloir écraser un livre déjà exisant ?',
                                           icon='warning', font=("Bahnschrift", 10))
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
                   "Sélectionenez votre histoire déjà existante dans la liste ou sélectionnez Créer un nouveau livre pour choisir un autre emplacement sur votre disque pour en créer une nouvelle\n\n\n\n",wraplength = 600, font=("Bahnschrift", 12))
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
        editor3000(select)
        frame1.destroy()

def ajouterchapitre():
    global chaplist
    content[str(len(content))] = [[f"Titre du chapitre {str(len(content)+1)}","Texte du chapitre"],0,0,[[],"H", "False"]]
    chaplist.delete(0, tk.END)
    for line in range(len(content)):
        chaplist.insert(tk.END, content[str(line)][0][0])
def editerchapitre(chemin,chapitreactuel, chapitreaemmener):
    global chaplist,frameleft, framecenter,frameright,leftcolumn,rightcolumn,frametopcenter,framebottomcenter
    save(chapitreactuel)
    for line in content:
        if chapitreaemmener == content[str(line)][0][0] :
            valuechap = line
    destroyframes()
    print(valuechap)
    editor3000(chemin, int(valuechap)-1)


#Éditeur
def newbook(chemin):
    with open(chemin + "/content.json", "w") as f:
        json.dump({"0": [["Titre du 1", "Blabla premiere diapo"], 0, 0, [["1", "Sortir"], ["2", "Chercher la telecommande"], ["3", "prout"]], "H", "False"]}, f)
    f = open(chemin + "/persos.json", "w")
    f = open(chemin + "/content.json", "w")
    editor3000(chemin)

def save(i):
    global titreduchapitre, texte_histoire,v,  redirchap1text, redirchap2text, redirchap3text,redirchap1,redirchap2,redirchap3
    content[str(i)]=[[titreduchapitre.get(),texte_histoire.get(1.0, tk.END+"-1c")],0,0,[[redirchap1.get(), redirchap1text.get()],[redirchap2.get(), redirchap2text.get()],[redirchap3.get(), redirchap3text.get()]],v.get(), "False"]


def writefiles(chemin, chapencours):
    save(chapencours)
    with open( chemin + "/content.json", 'w') as outfile:
        json.dump(content, outfile)
    with open( chemin + "/persos.json", 'w') as outfile:
        json.dump(persos, outfile)
    with open( chemin + "/specs.json", 'w') as outfile:
        json.dump(specs, outfile)

def editentry(a):

    global mylist1
    print(a)
    select = mylist1.get(1)
    nouvellefenetre = tk.Toplevel(window)
    nouvellefenetre.title("Modifier entrée")
    inputobj = tk.Entry(nouvellefenetre)
    inputobj.insert(1,str(select))
    inputobj.pack()
    inputobjsave = tk.Button(nouvellefenetre, text= "Enregistrer", command = lambda :updatelist(select, inputobj))
    inputobjsave.pack(fill= tk.Y)
def updatelist(select,inputobj):
    global specs
    #for i
    specs["objets"][inputobj] = specs["objets"][select]
    specs["objets"].pop(select)
    print(mylist1)

def destroyframes():
    global frameleft, framecenter,frameright,leftcolumn,rightcolumn,frametopcenter,framebottomcenter
    framelist = [frameleft, framecenter,frameright,leftcolumn,rightcolumn,frametopcenter,framebottomcenter]
    for i in range(0,len(framelist)):
        try:
            framelist[i].destroy()
        except:
            print("nop")

def editor3000(chemin,chapitre = 0):
    global frame2, frame3, perso, chaplist, titreduchapitre, texte_histoire,v,  redirchap1text, redirchap2text, redirchap3text,redirchap1,redirchap2,redirchap3,frameleft, framecenter,frameright,leftcolumn,rightcolumn,frametopcenter,framebottomcenter, mylist1
    frame2.destroy()
    frame3.destroy()
    load(chemin)
    frameleft = tk.Frame(window)
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
    mylist1.bind('<Double-Button>', editentry)
    myscroll2.config(command=mylist1.yview)
    for line in range(1,len(specs["objets"])+1):
        mylist1.insert(tk.END, specs["objets"][str(line)][0])
    mylist1.pack(side=tk.TOP, fill=tk.BOTH)
    rightcolumn.pack(side = tk.TOP, fill = tk.Y)
    v = tk.StringVar(None, "C")
    combat = ttk.Radiobutton(
        frameright,
        text='Combat',
        variable=v,
        value='C')
    histoire = ttk.Radiobutton(
        frameright,
        text='Histoire',
        variable=v,
        value='H')
    combat.pack(side=tk.TOP, ipady=5, fill = tk.Y)
    histoire.pack(side=tk.TOP, ipady=5, fill = tk.Y)
    v.set("H")
    frameright.pack(side = tk.RIGHT, fill = tk.Y)
    mylabel = tk.Label(leftcolumn, text='Liste des chapitres', font=("Bahnschrift", 15))
    mylabel.pack()
    myscroll = tk.Scrollbar(leftcolumn)
    myscroll.pack(side=tk.RIGHT, fill=tk.Y)
    chaplist = tk.Listbox(leftcolumn, yscrollcommand=myscroll.set)
    for line in range(len(content)):
        chaplist.insert(tk.END, content[str(line)][0][0])
        chaplist.configure( selectmode = tk.SINGLE)
    chaplist.pack(side=tk.TOP, fill=tk.Y)
    addchapitre = tk.Button(leftcolumn, text= "Ajouter un chapitre", command= ajouterchapitre, font=("Bahnschrift", 10))
    addchapitre.pack(fill=tk.X)
    editchapitre = tk.Button(leftcolumn, text= "Editer le chapitre",font=("Bahnschrift", 10), command= lambda : editerchapitre(chemin,chapitre, chaplist.get(chaplist.curselection())))
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
    soustitresredirs = tk.Label(framebottomcenter, text= "Choisissez les cartes vers lequel rediriger avec les choix")
    subframe1 = tk.Frame(framebottomcenter)
    subframe2 = tk.Frame(framebottomcenter)
    subframe3 = tk.Frame(framebottomcenter)
    redirchap1 = tk.Entry(subframe1,width = 3)
    redirchap2 = tk.Entry(subframe2,width = 3)
    redirchap3 = tk.Entry(subframe3,width = 3)
    print(chapitre)
    print(content)
    redirchap1.insert(1,f"{content[str(chapitre)][3][0][0]}" )
    redirchap2.insert(1,f"{content[str(chapitre)][3][1][0]}" )
    redirchap3.insert(1,f"{content[str(chapitre)][3][2][0]}" )
    redirchap1text = tk.Entry(subframe1,width = 60)
    redirchap2text = tk.Entry(subframe2,width = 60)
    redirchap3text = tk.Entry(subframe3,width = 60)
    redirchap1text.insert(1,f"{content[str(chapitre)][3][0][1]}" )
    redirchap2text.insert(1,f"{content[str(chapitre)][3][1][1]}" )
    redirchap3text.insert(1,f"{content[str(chapitre)][3][2][1]}" )
    redirchap1text.pack(side = tk.RIGHT)
    redirchap2text.pack(side = tk.RIGHT)
    redirchap3text.pack(side = tk.RIGHT)
    redirchap1.pack(side = tk.LEFT)
    redirchap2.pack(side = tk.LEFT)
    redirchap3.pack(side = tk.LEFT)
    subframe1.pack()
    subframe2.pack()
    subframe3.pack()
    enregistrer = tk.Button(framebottomcenter, text= "Enregistrer chapitre", command= lambda : save(chapitre))
    enregistrer.pack(side = tk.BOTTOM, fill=tk.X)
    ecrirefichier =tk.Button(framebottomcenter, text= "Ecrire le livre", command= lambda : writefiles(chemin, chapitre))
    ecrirefichier.pack(side = tk.BOTTOM, fill=tk.X)
    framebottomcenter.pack(fill=tk.X)
    framecenter.pack()

accueil()
#editor3000("C:/Users/maxim/Documents/GitHub/livredontvousetesleheros-groupe-5/livres/livre 1")
window.mainloop()