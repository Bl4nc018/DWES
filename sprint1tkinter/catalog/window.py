## Ejercicio 6:

from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell
from PIL import Image


class MainWindow():

    def on_button_clicked(self, cell):
        message = "Has hecho click en el  juego: " + cell.title
        messagebox.showinfo("Información", message)

    def __init__(self, root):
        root.title("Top 5 Juegos:")

        self.cells = [
            Cell("Divinity Original Sin II", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\edited\\300px-Divinity_Original_Sin_II_-_Definitive_Edition_cover (100x100).jpg"),
            Cell("Baldur's Gate 3", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\edited\\Baldurs gate 3 game cover (100x100).jpg"),
            Cell("Mass Effect: Legendary Edition", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\edited\\Mass Effect game cover (100x100).jpg"),
            Cell("Persona 5", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\edited\\Persona_5_cover_art (100x100).jpg"),
            Cell("The Elder Scrolls V: Skyrim", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\edited\\The_Elder_Scrolls_V_Skyrim_cover (100x100).jpg")
        ]

        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image = cell.image_tk, text = cell.title, compound = tk.BOTTOM)
            label.grid(row = i, column = 0)
            label.bind("<Button-1>", lambda event, cell = cell: self.on_button_clicked(cell))