## Ejercicio #2:

from tkinter import ttk, Button

class MainWindow():

    def onButtonClicked(self):
        pass

    def __init__(self, root):
        self.root = root
        
        #Botón
        self.button = ttk.Button(text = "Realizar la acción", command = self.onButtonClicked)
        self.button.pack()

