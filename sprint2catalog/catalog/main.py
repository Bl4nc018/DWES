import threading
from tkinter import Tk 
from loadingWindow import LoadingWindow

if __name__ == "__main__":
    root = Tk()
    app = LoadingWindow(root)
    root.mainloop()
    