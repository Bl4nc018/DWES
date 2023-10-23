from tkinter import messagebox, ttk
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
    
  def on_button_clicked2(self):
    mensajito = "La desarrolladora de esta página la ha programado con Python."
    messagebox.showinfo("Acerca del desarrollador", mensajito)
    
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
        label.grid(row=0, column=len(self.cell_list) - 1)  ## Como borramos el anterior for que empleabamos para recorrer todo el contenido dentro de la lista e ir leyendolo para mostrarlo en la ventana.
                                                           ## Aqui usaremos la linea con la longitud de la lista -1 para que se muestren todas las imagenes en una sola fila.
                                                           ## Si empleamos la longitud en las filas, nos quedará, aunque en el centro, saldrá cortado por un cuarto de la pantalla.
        label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))
        
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2  ## A diferencia de loading window, aqui no se emplea self.root porque no esta definido en mainwindow
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry(f"+{int(x)}+{int(y)}")
    
    ## Ejercicio 6:
    
    barra_menus = tk.Menu()
    menu_archivo = tk.Menu(barra_menus, tearoff=False)


    menu_archivo.add_command(label="Acerca de", command=self.on_button_clicked2)
    barra_menus.add_cascade(menu=menu_archivo, label="Ayuda")
    root.config(menu=barra_menus)
  
  def archivo_nuevo_presionado(root):
    print("¡Has presionado para crear un nuevo archivo!")