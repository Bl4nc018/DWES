from tkinter import Canvas, Frame, Label, Scrollbar, messagebox, ttk
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
    img = ImageTk.PhotoImage((img_data).resize((250, 250), Image.Resampling.LANCZOS)) ## Hacemos resize a la imagen 
    return img

  def on_button_clicked(self, cell):
    detWindow(cell) ## Llamamos a la funcion con la que haremos la segunda ventana.
    
    
  ## Ejercicio 6:  
    
  def on_button_clicked2(self):
    mensajito = "La desarrolladora de esta página la ha programado con Python."
    messagebox.showinfo("Acerca del desarrollador", mensajito)
  
    
  def __init__(self, root, json_data):
    
    root.title("Top 5 Juegos:")

    ## Ejercicio 7: Creada barra lateral para desplazarse

    self.canvas = Canvas(root) ## Definimos el canvas, que emplearemos para dibujar en la ventana principal.
    self.scrollbar = Scrollbar(root, orient="vertical", command=self.canvas.yview) ## Se crea un objeto Scrollbar que se adjunta a root también. 
                  ## Mediante orient definimos su orientación, en este caso, vertical y se asocia al lienzo (el canvas) para controlar el desplazamiento vertical.
    self.scrollable_frame = Frame(self.canvas)  ## Aquí colocamos el canvas gracias al frame.
    
    self.scrollable_frame.bind("<Configure>",  ## Con estas líneas (44 - 47) hacemos que el lienzo se ajuste a la ventana si esta se reconfigura.
                               lambda e: self.canvas.configure(
                                 scrollregion=self.canvas.bbox("all")
                               ))
    
    self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw") ## Creamos la ventana en la posición 0, 0. La ancla es para que haya un ajuste del marco.
    self.canvas.configure(yscrollcommand=self.scrollbar.set) ## Configura el lienzo para emplearlo.


    self.cell_list = []  ## Inicializamos una variable propia de nombre cell_list. Osease una lista para almacenar todo el contenido que vayamos pasando a cada celda.

    for item in json_data: ## Cambiamos gran parte del código anterior para, en lugar de leer todos los datos del catalog en una linea, se haga en varias y no debamos de emplear dos for.
        name = item["name"] ## Le pasamos a una variable el nombre del item en el catalog (json_data)
        descripcion = item["descripcion"]
        url = item["image_url"]
        imagen = self.load_image_from_url(url) ## Nuevamente pasamos a una variable de nombre imagen el contenido que cargamos del .json

        cell = Cell(name, descripcion, url, imagen) ## Todo este contenido que se fue leyendo anteriormente es introducido dentro de la clase Cell() que es instanciada en una variable de nombre cell.
        self.cell_list.append(cell) ## Esta línea de código es empleada para añadir todo el contenido de la variable anterior (que pasamos a la clase Cell) ir siendo añadido a la lista instanciada
                                    ## anteriormente como self.cell_list.

        self.canvas.grid(row=0, column=0, sticky="nsew") ## Para colocar el lienzo:
        self.scrollbar.grid(row=0, column=1, sticky="ns") ## Para colocar la barra:
        
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        
        frame = Frame(self.scrollable_frame) ## Marco que contendrá lo que se vaya a mostrar
        frame.pack(pady=10)
        
        label = Label(frame, image=cell.imagen, text=name, compound=tk.BOTTOM) ## Etiqueta para mostrar la imagen
        label.grid(row=0, column=0)
        
        label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))    
    
    
    ## Ejercicio 5: Centrado de la ventana.    
        
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2  ## A diferencia de loading window, aqui no se emplea self.root porque no esta definido en mainwindow
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry(f"+{int(x)}+{int(y)}")
    
    ## Ejercicio 6: Añadida a la barra de la ventana el elemento "Ayuda"
    
    barra_menus = tk.Menu() ## Instanciamos la barra
    menu_archivo = tk.Menu(barra_menus, tearoff=False) ## 
    
    menu_archivo.add_command(label="Acerca de", command=self.on_button_clicked2) ##
    barra_menus.add_cascade(menu=menu_archivo, label="Ayuda")
    root.config(menu=barra_menus)
    
    
    