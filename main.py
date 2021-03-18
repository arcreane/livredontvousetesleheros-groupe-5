import os
#Stocker le livre dans un dico

#IMPORT DES FICHIERS
#CHECk FOR BCK

#livre = {"numero de carte":["texte a afficher", ["liste de tupples de cartes a coninuer avec leur numéro"], "choses a rajouter au sac a dos"], cartedefin ?}
livreimport = []
nouv_liste= []
listedescartes_sale = []
listedescartes = []
with open("livre/livre1.txt", "r") as fichier:
    livreimport = "".join(fichier)
    listeimport = livreimport.split("###@@@###@@@")
    print(listeimport)
for i in range(0,len(listeimport)):
    if "#" not in listeimport[i]:
        nouv_liste.append(listeimport[i])
for i in range(0,len(nouv_liste)):
    cartes = nouv_liste[i].split("\n")
    listedescartes_sale.append(cartes)

for i in range(0,len( listedescartes_sale)):
    for y in range(0, len(listedescartes_sale)):
        if "" !=  listedescartes_sale[i][y]:
            listedescartes.append(listedescartes_sale[i][y])
print(listedescartes)
#initiialisation de la partie
carte  = 0
end = False
texte_carte = "Vous etes a la carte :"
backpack = []
"""
while end != True:
    print(texte_carte, carte, "\n" , livre.get(carte)[0])
    for i in range(0, len(livre.get(carte)[1])):
        print(livre.get(carte)[1][i])
    if livre.get(carte)[2] != "":
        backpack.append(livre.get(carte)[2])
    choix = input("entrez le numéro de la carte ou vous souhaitez vous rendre")
    while choix not in livre.get(carte)[1] :
        for i in range(0, len(livre.get(carte)[1])):
            print(livre.get(carte)[1][i])
        choix = input("Ce numéro n'est pas dans les choix, veuillez en entrer un qui soit dans la liste")"""
