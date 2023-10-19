from tkinter import ttk
import tkinter as tk

import requests
from cell import Cell
from detail_window import detWindow

## Ejercicio 4:

from PIL import Image, ImageTk
from io import BytesIO

class MainWindow():

  def load_image_from_url(self, url):
    response = requests.get(url)
    img_data = Image.open(BytesIO(response.content))
    img = ImageTk.PhotoImage(img_data)
    return img

  def on_button_clicked(self, cell):
    detWindow(cell) ## Llamamos a la funcion con la que haremos la segunda ventana.
    
  def __init__(self, root, json_data):
    root.title("Top 5 Juegos:")

    self.cell_list = []  ## Inicializamos una variable propia de nombre cell_list. Osease una lista para almacenar todo el contenido que vayamos pasando a cada celda.

    for item in json_data: ## Cambiamos gran parte del código anterior para, en lugar de leer todos los datos del catalog en una linea, se haga en varias y no debamos de emplear dos for.
        name = item["name"] ## Le pasamos a una variable el nombre del item en el catalog (json_data)
        descripcion = item["descripcion"]
        url = item["image_url"]
        imagen = self.load_image_from_url(url) ## Nuevamente pasamos a una variable de nombre imagen el contenido que cargamos del .json

        cell = Cell(name, descripcion, url, imagen) ## Todo este contenido que se fue leyendo anteriormente es introducido dentro de la clase Cell() que es instanciada en una variable de nombre cell.
        self.cell_list.append(cell) ## Esta línea de código es empleada para añadir todo el contenido de la variable anterior (que pasamos a la clase Cell) ir siendo añadido a la lista instanciada
                                    ## anteriormente como self.cell_list.

        label = ttk.Label(root, image=cell.imagen, text=name, compound=tk.BOTTOM)
        label.grid(row=len(self.cell_list) - 1, column=0)  ## Como borramos el anterior for que empleabamos para recorrer todo el contenido dentro de la lista e ir leyendolo para mostrarlo en la ventana.
                                                           ## Aqui usaremos la longitud de la lista menos 1 para poder definir adecuadamente cuantas filas tendrá lo que se mostrará por pantalla.
        label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))