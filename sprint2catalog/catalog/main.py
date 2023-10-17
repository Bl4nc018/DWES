from tkinter import Tk 
from window import MainWindow
from loadingWindow import LoadingWindow

if __name__ == "__main__":
    root = Tk()
    app = LoadingWindow(root)
    root.mainloop()