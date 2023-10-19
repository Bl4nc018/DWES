import tkinter as tk
from tkinter import ttk


def detWindow(cell):
    root = tk.Toplevel() ## self.window, es una variable que forma parte de la instancia de la clase y la empleamos para acceder, mediante Toplevel,
                         ## a una nueva ventana secundaria creada por este. Es decir, mientras que con root = Tk(); creamos la ventana principal,
                         ## con window = Toplevel(root) (ejemplo) creamos la ventana secundaria. Entre parentesis ponemos root para asociarla a esa ventana principal.
                         
    root.title("Información extra acerca del juego.") ## Título de la ventana.
    
    label1 = ttk.Label(root, text=cell.name) ## Esta es la que contendrá el título del videojuego
    label1.pack()
    label = ttk.Label(root, image=cell.imagen, compound=tk.BOTTOM) ## Esta línea es para llamar a la foto almacenada en Cell()
    label.pack()
    label2 = ttk.Label(root, text=cell.descripcion) ## Esta contendrá la descripción.
    label2.pack()
    
    root.mainloop()
        