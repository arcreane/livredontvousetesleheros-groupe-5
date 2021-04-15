import json
from tabulate import tabulate
with open('livre/persos.json') as f:
  persos = json.load(f)
with open('livre/specs.json') as f:
  specs = json.load(f)
with open('livre/content.json') as f:
  content = json.load(f)

#print(specs, persos, content)

print("Choisissez un personnage")

#print(list(persos.keys()))
printlist = []
ndlist = []

for i in range(0, len(list(persos.keys()))):
  ndlist += [[list(persos.keys())[i]]+persos[list(persos.keys())[i]][0]]

print(tabulate(ndlist, headers=["Nom"]+specs["cappas"]))
name = list(persos.keys())[0]
print(list(persos.keys())[0])
print(name in list(persos.keys()))
while name in list(persos.keys()):
  name = input("Entrez le nom de votre personnage :")