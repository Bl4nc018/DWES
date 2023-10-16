## Ejercicio 6:

from tkinter import ttk
import tkinter as tk
from cell import Cell
from detail_window import detWindow

class MainWindow():

    def on_button_clicked(self, cell):
        # message = "Has hecho click en el juego: " + cell.title ## Mensaje que aparecerá una vez se haga clic.
        # messagebox.showinfo("Información", message)
        detWindow(cell) ## Llamamos a la funcion con la que haremos la segunda ventana.
        
    def __init__(self, root):
        root.title("Top 5 Juegos:") ## Título de la ventana.

        self.cells = [
            Cell("Divinity Original Sin II", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\300px-Divinity_Original_Sin_II_-_Definitive_Edition_cover.jpg",
                 "Divinity: Original Sin 2: Héroes con habilidades mágicas prohibidas buscan escapar de la isla de Fort Joy y desvelar un misterio divino en un mundo oscuro."),
            
            Cell("Baldur's Gate 3", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\Baldurs gate 3 game cover.jpg",
                 "Baldur's Gate 3: Lucha contra los azotamentes en un mundo de fantasía épica mientras buscas una cura para la infección alienígena."),
            
            Cell("Mass Effect: Legendary Edition", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\Mass Effect game cover.jpg",
                 "Mass Effect Legendary Edition: Épica saga espacial con decisiones cruciales y una galaxia llena de peligros."),
            
            Cell("Persona 5", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\Persona_5_cover_art.jpg",
                 "Persona 5: Juego de rol con adolescentes luchando contra la corrupción en mundos paralelos."),
            
            Cell("The Elder Scrolls V: Skyrim", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\The_Elder_Scrolls_V_Skyrim_cover.png",
                 "The Elder Scrolls V: Skyrim es un ARPG del tipo mundo abierto desarrollado por Bethesda Game Studios y publicado por Bethesda Softworks.")
        ]

        ## Celdas con el título que tendrán y, debajo, la imagen que mostrarán.

        for i, cell in enumerate(self.cells): ## Bucle para leer la lista.

            ## Lo que se mostrará en la ventana:
            label = ttk.Label(root, image=cell.imagen_redi, text=cell.title, compound= tk.BOTTOM) ## La imagen y el texto que se mostrarán son pasados por el constructor de nombre cell
            label.grid(row=i,column=0)
            label.bind("<Button-1>",lambda event, cell = cell: self.on_button_clicked(cell))