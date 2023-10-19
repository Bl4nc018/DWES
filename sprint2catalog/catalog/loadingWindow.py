import json
import threading
import tkinter as tk
import requests
from window import MainWindow


class LoadingWindow:
    def __init__(self, root):
        self.root = root ## Instancia ventana carga
        self.root.title("Cargando...") ## Titulo ventana carga
        self.root.geometry("250x200") ## Tamaño ventana carga
        self.root.resizable(False, False) ## Argumento empleado para evitar que varie el tamaño de la ventana de carga
        
        self.finished=False
        
        ## Etiqueta:
        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14))
        self.label.pack(side=tk.TOP, pady=10)
        
        label_bg_color = self.label.cget("bg") ## Color del fondo
        
        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color) ## Creación del lienzo con sus correspondientes características
        self.canvas.pack() 
        
        self.progress = 0
        
        self.draw_progress_circle(self.progress) ## a la función creada se le pasa el atributo propio de progreso, que instanciamos en 0
        
        
        
        self.thread = threading.Thread(target=self.fetch_json_data) ## Guardamos datos en el thread
        self.thread.start() ## Comenzamos el thread
        
        self.check_thread() ## Comprobamos estado del thread
        
        self.update_progress_circle()
        
        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()
        
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")
        
        
    def draw_progress_circle(self, progress):
        self.canvas.delete("progress")  ## Esta línea es necesaria para poder borrar cualquier dibujo anterior previo al inicio de la función
        angle = int(360 * (progress/100))
        
        self.canvas.create_arc(10, 10, 35, 35,
                               start=0, extent=angle, tags="progress", outline='red', width=4, style=tk.ARC) ## Creamos el arco de carga
        
    
    def update_progress_circle(self):  
        if self.progress < 100:
            self.progress += 9
        else:
            self.progress = 0       
        
        self.draw_progress_circle(self.progress)
        self.root.after(100, self.update_progress_circle)
        
    ## Ejercicio 3: Descargar json
    
    def fetch_json_data(self):
        response = requests.get("https://raw.githubusercontent.com/Bl4nc018/DWES/main/catalog.json")       
        if response.status_code == 200:
            self.json_data = response.json() ## Recoje en una variable la respuesta del .json
            self.finished=True
        # print(response.json()) ## Imprime el .json sin decodif. para confirmar que si se descarga.
        
    def check_thread(self):
        if self.finished:
            self.root.destroy()
            launch_main_window(self.json_data)
        else:
            self.root.after(100, self.check_thread)

        
        
## Ejercicio 4: Despliegue ventana detalle y renderizado del JSON.

def launch_main_window(json_data):
    root = tk.Tk()
    app = MainWindow(root, json_data)
    root.mainloop()

