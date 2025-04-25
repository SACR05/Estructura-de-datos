# main.py
import tkinter as tk
from controlador import Controlador
from vista import Vista

# Punto de entrada de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = Vista(root, Controlador())
    root.mainloop()

