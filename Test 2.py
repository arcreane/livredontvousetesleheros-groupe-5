import tkinter as tk

fenetre = tk.Tk()

variable_a_modifier = tk.StringVar()  # String
# variable_a_modifier = tk.IntVar() # Integer
# variable_a_modifier = tk.DoubleVar() # Float

label = tk.Label(fenetre, textvariable=variable_a_modifier)
label.pack()


## Pour modifier le résultat de la variable tkinter
## On utilise .set()
def modifier_texte():
    variable_a_modifier.set('Salut, ça va bien?')


btn_modifier = tk.Button(fenetre, text="Modifier",
                         command=modifier_texte)
btn_modifier.pack()


## Pour afficher le résultat de la variable tkinter
## On utilise .get()
def print_texte():
    print(variable_a_modifier.get())


btn_print = tk.Button(fenetre, text="Printer",
                      command=print_texte)
btn_print.pack()

fenetre.mainloop()