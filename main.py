import os
import tkinter as tk

#Stocker le livre dans un dico

#IMPORT DES FICHIERS
#CHECk FOR BCK
"""def Persos():
    def __init__(self,nom, capa, sacados):
        self.nom = nom
        self.c = capa
        self.bp = sacados
"""
livre={}
personnages={}
#livre = {"numero de carte":["texte a afficher", ["liste de tupples de cartes a coninuer avec leur numéro"], "choses a rajouter au sac a dos"], cartedefin ?}
livreimport = []
nouv_liste= []
listedescartes_sale = []
listedescartes = []
with open("livre/livre1.lvdvelh", "r") as fichier:
    livreimport = "".join(fichier)
    listeimport = livreimport.split("###@@@###@@@")
    print(listeimport)
for i in range(0, len(listeimport)):
    listeimport[i]= listeimport[i].split("\n")
    for y in range(0, len(listeimport[i])):
        listeimport[i][y] = listeimport[i][y][:str(listeimport[i][y]).find("@@")]
print(listeimport)
totalcartes = listeimport[0][0]
listecapa= str(listeimport[0][1]).split(", ")
print(listecapa)


for i in range(0,listeimport[0][3]):
    listepersos = listeimport[0][3+i].split("|")

    personnages[]


"""for i in range(0,len(listeimport)):
    if "#" not in listeimport[i]:
        nouv_liste.append(listeimport[i])
for i in range(0,len(nouv_liste)):
    cartes = nouv_liste[i].split("\n")
    listedescartes_sale.append(cartes)"""


"""print(nouv_liste)
for i in range(0,len( listedescartes_sale)):
    print(listedescartes_sale[i])
    for y in range(0, len(listedescartes_sale[i])):
        #print(listedescartes_sale[i][y])
        if '' !=  listedescartes_sale[i][y]:
            listedescartes.append(listedescartes_sale[i][y])"""
#print(listedescartes)=
#initiialisation de la partie
"""carte  = 0
end = False
texte_carte = "Vous etes a la carte :"
backpack = []
print(round(len(listedescartes)/6))
for i in range(0,round(len(listedescartes)/6)) :
    #livre[listedescartes[i*5+1]] = {[listedescartes[i*6+2][8:], listedescartes[i*6+3][11:], listedescartes[i*6+4][12:],listedescartes[i*6+5][12:]],listedescartes[i*6+6][6:]}
    print([listedescartes[i*6+2][8:], listedescartes[i*6+3][12:], listedescartes[i*6+4][20:],listedescartes[i*6+5][12:]],listedescartes[i*6+6][6:])"""

"""
while end != True:
    print(texte_carte, carte, "\n" , livre.get(carte)[0])
    for i in range(0, len(livre.get(carte)[1])):
        print(livre.get(carte)[1][i])
    if livre.get(carte)[2] != "":
        backpack.append(livre.get(carte)[2])
    choix = input("entrez le numéro de la carte où vous souhaitez vous rendre")
    while choix not in livre.get(carte)[1] :
        for i in range(0, len(livre.get(carte)[1])):
            print(livre.get(carte)[1][i])
        choix = input("Ce numéro n'est pas dans les choix, veuillez en entrer un qui soit dans la liste")"""
