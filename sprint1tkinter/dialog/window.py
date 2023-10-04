## Ejercicio #2:

from tkinter import ttk, Button

class MainWindow():

    def onButtonClicked(self):
        pass

    def __init__(self, root):
        self.root = root

        #Etiqueta
        self.label = ttk.Label(text = "Este mensaje es poco importante")
        self.label.pack()
        
        #Botón
        self.button = ttk.Button(text = "Realizar la acción", command = self.onButtonClicked)
        self.button.pack()

