## Ejercicio 3:

import tkinter as tk

def show_no_window():

    no_root = tk.Tk()

    #Etiqueta
    label = tk.Label(no_root, text="No")
    label.pack()

    no_root.mainloop()



# En este caso, esto es una función, no una clase. Por lo tanto, para empaquetar una etiqueta creas una nueva variable, que esté en el root que generará la nueva ventana
# por ello se pone la nueva label despues del primer paréntesis '('. Y empaquetar se refiere a añadir la variable mediante un .pack().