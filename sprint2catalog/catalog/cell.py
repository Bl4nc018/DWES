## Ejercicio 5:

from PIL import Image, ImageTk

## En esta clase constructora definiremos todos los componentes que necesitaremos llamar mediante las otras clases.

class Cell():
    
    def __init__(self, title, path, descripcion):
        self.title = title
        self.path = path
        self.descripcion = descripcion
        
        ## La siguiente línea se trata de una variable en la que se abre la ruta de la clase cell, para obtener la imagen. Mediante el uso de Image.open procede
        ## a abrirla y, todo esto ejecuta .resize, lo que quiere decir que cambia la imagen que estaba sin editar a un 100x100.

        self.imagen_redi = ImageTk.PhotoImage((Image.open(self.path)).resize((100, 100), Image.Resampling.LANCZOS)) 
        
        