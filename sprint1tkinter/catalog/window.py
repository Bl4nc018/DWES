## Ejercicio 6:

from tkinter import ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox

class MainWindow():

    def on_button_clicked(self, cell):
        message = "Has hecho click en la celda" + cell.title
        messagebox.showinfo("Información", message)

    def __init__(self, root):
        root.title("MainWindow")

        self.cells = [
            Cell("Juego 1", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\edited\\300px-Divinity_Original_Sin_II_-_Definitive_Edition_cover (100x100).jpg"),
            Cell("Juego 2", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\edited\\Baldurs gate 3 game cover (100x100).jpg"),
            Cell("Juego 3", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\edited\\Mass Effect game cover (100x100).jpg"),
            Cell("Juego 4", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\edited\\Persona_5_cover_art (100x100).jpg"),
            Cell("Juego 5", "C:\\msys64\\home\\joker\\DWES\\sprint1tkinter\\catalog\\data\\edited\\The_Elder_Scrolls_V_Skyrim_cover (100x100).jpg")
        ]

        for i, cell in enumerate(self.cells):

            label = ttk.Label(root, image = cell.image_tk, text = cell.title, compound = tk.BOTTOM)
            label.grid(row = i, column = 0)
            label.bind("<Button-1>", lambda event, cell = cell: self.on_button_clicked(cell))