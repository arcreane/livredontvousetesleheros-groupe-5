import json
import tkinter.ttk as ttk
import tkinter.filedialog
import os
import glob
import tkinter as tk
window=tk.Tk()
window.minsize(650,260)
window.title('LDVELH')
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

frame=tk.Frame(window)
frame.grid(row=0, column=0, sticky="NESW")
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
        listelocate =[]
        listelocate = glob.glob((text_files[i].replace("content.json", "")+"*.json"), recursive = True)
        if text_files[i]in listelocate and text_files[i].replace("content.json", "")+"specs.json".replace("/","\\")in listelocate and text_files[i].replace("content.json", "")+"persos.json".replace("/","\\") in listelocate :
            retour.append((text_files[i].replace("content.json", "")))
    return(retour)

def accueil():
    tk.Label(text= "Bienvenue dans Le Jeu Dont Vous Êtes Le Héros : \n"
                   "Sélectionenez votre histoire dans la liste ou selectionner autre pour choisir un autre emplacement sur votre disque \n\n\n\n")\
        .grid(column = 0, row = 0, sticky = "EW")

    listeCombo.current(0)
    listeCombo.grid(row=1, column=0 , sticky = "N")
    tk.Label(text= "\n \n\n\n\n").grid(column = 0, row = 2, sticky = "EW")
    listeCombo.bind("<<ComboboxSelected>>", action)



printlist = []
ndlist = []



#t = Table(window,ndlist)
#Initialisation des variables tkinter
listeFichiers = listlivres()
listeFichiers.append("autre")
listeCombo = ttk.Combobox(window, values=listeFichiers)

def action(event):
    select = listeCombo.get()
    if select == "autre":
        text_files = tk.filedialog.askdirectory(title = "Selectionnez un dossier", mustexist = True, initialdir = os.path.expanduser('~/Documents'))
        if ishistoire(text_files):
            play(text_files)
    else :
        play(select)



#Jeu

def play(chemin):
    frame.destroy()
    with open(chemin+"/persos.json") as f:
      persos = json.load(f)
    with open(chemin+"/specs.json") as f:
      specs = json.load(f)
    with open(chemin+"/content.json") as f:
      content = json.load(f)
    print("blabla")
    for widget in window.winfo_children():
        widget.destroy
accueil()
import tkinter as tk

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        window.minsize(650, 260)
        window.title('LDVELH')
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1)

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        tk.Label(text="Bienvenue dans Le Jeu Dont Vous Êtes Le Héros : \n"
                      "Sélectionenez votre histoire dans la liste ou selectionner autre pour choisir un autre emplacement sur votre disque \n\n\n\n") \
            .grid(column=0, row=0, sticky="EW")

        listeCombo.current(0)
        listeCombo.grid(row=1, column=0, sticky="N")
        tk.Label(text="\n \n\n\n\n").grid(column=0, row=2, sticky="EW")
        listeCombo.bind("<<ComboboxSelected>>", action)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


window = SeaofBTCapp()
window.mainloop()
#window.mainloop()

