from PIL import Image, ImageTk

## En esta clase constructora definiremos todos los componentes que necesitaremos llamar mediante las otras clases.

class Cell():
    
    def __init__(self, name, descripcion, image_url, imagen):
        self.name = name
        self.descripcion = descripcion
        self.image_url = image_url
        self.imagen = imagen      
        