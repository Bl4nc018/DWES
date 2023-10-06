## Ejercicio 6:

from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell
from PIL import Image, ImageTk

class MainWindow():

    def on_button_clicked(self, cell):
        message = "Has hecho click en el juego: " + cell.title ## Mensaje que aparecerá una vez se haga clic.
        messagebox.showinfo("Información", message)

    def __init__(self, root):
        root.title("Top 5 Juegos:") ## Título de la ventana.

        self.cells = [
            Cell("Divinity Original Sin II", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\300px-Divinity_Original_Sin_II_-_Definitive_Edition_cover.jpg"),
            Cell("Baldur's Gate 3", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\Baldurs gate 3 game cover.jpg"),
            Cell("Mass Effect: Legendary Edition", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\Mass Effect game cover.jpg"),
            Cell("Persona 5", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\Persona_5_cover_art.jpg"),
            Cell("The Elder Scrolls V: Skyrim", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\The_Elder_Scrolls_V_Skyrim_cover.png")
        ]

        ## Celdas con el título que tendrán y, debajo, la imagen que mostrarán.

        for i, cell in enumerate(self.cells): ## Bucle para leer la lista.
            
            ## La siguiente línea se trata de una variable en la que se abre la ruta de la clase cell, para obtener la imagen. Mediante el uso de Image.open procede
            ## a abrirla y, todo esto ejecuta .resize, lo que quiere decir que cambia la imagen que estaba sin editar a un 100x100.
            juego = (Image.open(cell.path)).resize((100, 100), Image.Resampling.LANCZOS)
            cell.image_tk = ImageTk.PhotoImage(juego)

            ## Lo que se mostrará en la ventana:
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound= tk.BOTTOM)
            label.grid(row=0,column=i)
            label.bind("<Button-1>",lambda event, celda = cell: self.on_button_clicked(cell))