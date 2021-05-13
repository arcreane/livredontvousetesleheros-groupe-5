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
"""while name in list(persos.keys()):
  name = input("Entrez le nom de votre personnage :")"""

import tkinter as tk
window=tk.Tk()
# add widgets here

window.title('LDVELH')
#window.geometry(f"{str(window.winfo_screenwidth())}x{str(window.winfo_screenheight())}")
window.geometry("300x200")
tuplle = (["Nom"]+specs["cappas"])
ndlist.insert(0,tuplle)

class Table:

  def __init__(self, root,contenu):
    total_rows = len(contenu)
    total_columns = len(contenu[0])

    # code for creating table
    for i in range(total_rows):
      for j in range(total_columns):
        self.e = tk.Entry(root, width=20, fg='blue',
                       font=('Arial', 16, 'bold'))

        self.e.grid(row=i, column=j)
        self.e.insert(tk.END, contenu[i][j])


# take the data
lst = [(1, 'Raj', 'Mumbai', 19),
       (2, 'Aaryan', 'Pune', 18),
       (3, 'Vaishnavi', 'Mumbai', 20),
       (4, 'Rachna', 'Mumbai', 21),
       (5, 'Shubham', 'Delhi', 21)]

# find total number of rows and
# columns in list

"""def changeText():
  text.set(tabulate(ndlist, headers=["Nom"]+specs["cappas"]))"""


text = tk.StringVar()
text.set("Hello World!")
label = tk.Label(window, textvariable=text)
#label.pack(pady=20)
"""button = tk.Button(window, text="Changer le text", command=changeText)"""
"""button.pack()"""

t = Table(window,ndlist)
window.mainloop()
