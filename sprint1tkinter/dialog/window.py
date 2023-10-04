## Ejercicio 2:

from tkinter import ttk
from yes_window import show_yes_window
from no_window import show_no_window

class MainWindow():

    def __init__(self, root) -> None:
        self.root = root
<<<<<<< HEAD
=======

        #Etiqueta
        self.label = ttk.Label(text = "Este mensaje es poco importante")
        self.label.pack()
        
        #Botón
        self.button = ttk.Button(text = "Realizar la acción", command = self.onButtonClicked)
        self.button.pack()
>>>>>>> 8e0128757d52d273e008b884751ac09473d84315

        #Frame
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        #Etiqueta
        self.label = ttk.Label(text = "¿Aprobaste el examen?")
        self.label.pack()

        ## Ejercicio 3:

        #BotónSi
        self.button1 = ttk.Button(root, text = "Sí", command = show_yes_window)
        self.button1.pack(side="left")

        #BotónNo
        self.button2 = ttk.Button(root, text = "No", command = show_no_window)
        self.button2.pack(side="right")


# En esta clase para esta nueva ventana definimos el _init_ (funcion con la que definimos e inicializamos la configuración inicial.)
# Self.root se trata de la raíz de la clase, a partir de la que será empleada los métodos de esa clase en concreto.
# command llama a las otras ventanas y no hace falta emplear self. ya que son funciones.