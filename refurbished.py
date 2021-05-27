import tkinter as tk
class Table:

  def __init__(self, root,contenu):
    total_rows = len(contenu)
    total_columns = len(contenu[0])

    # code for creating table
    for i in range(total_rows):
      for j in range(total_columns):
        self.e = tk.Entry(root, width=15, fg='black',
                       font=('Arial', 12, 'bold'))

        self.e.grid(row=i, column=j)
        self.e.insert(tk.END, contenu[i][j])

"""def changeText():
  text.set(tabulate(ndlist, headers=["Nom"]+specs["cappas"]))"""
"""tuplle = (["Nom"]+specs["cappas"])
ndlist.insert(0,tuplle)"""

"""for i in range(0, len(list(persos.keys()))):
  ndlist += [[list(persos.keys())[i]]+persos[list(persos.keys())[i]][0]]"""

"""print(tabulate(ndlist, headers=["Nom"]+specs["cappas"]))
name = list(persos.keys())[0]
print(list(persos.keys())[0])
print(name in list(persos.keys()))
"""