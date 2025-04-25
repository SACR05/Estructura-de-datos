
import tkinter as tk
from tkinter import messagebox

# Clase Vista que crea y muestra la interfaz gráfica al usuario
class Vista:
    def __init__(self, root, controlador):
        self.controlador = controlador
        root.title("Lista Doble de Clientes")
        root.geometry("400x400")

        # Entradas de datos
        self.label_cedula = tk.Label(root, text="Cédula:")
        self.label_cedula.pack()
        self.entry_cedula = tk.Entry(root)
        self.entry_cedula.pack()

        self.label_nombre = tk.Label(root, text="Nombre:")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack()

        # Botón insertar
        self.btn_insertar = tk.Button(root, text="Insertar Cliente", command=self.insertar)
        self.btn_insertar.pack()

        # Botones  listar
        self.btn_listar_d = tk.Button(root, text="Listar Derecha", command=self.listar_derecha)
        self.btn_listar_d.pack()

        self.btn_listar_i = tk.Button(root, text="Listar Izquierda", command=self.listar_izquierda)
        self.btn_listar_i.pack()

        # Área de resultados
        self.text_resultado = tk.Text(root, height=10, width=40)
        self.text_resultado.pack()

    def insertar(self):
        try:
            cedula = int(self.entry_cedula.get())
            nombre = self.entry_nombre.get()
            self.controlador.insertar_cliente(cedula, nombre)
            messagebox.showinfo("Éxito", "Cliente insertado correctamente")
            self.entry_cedula.delete(0, tk.END)
            self.entry_nombre.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "La cédula debe ser numérica")

    def listar_derecha(self):
        clientes = self.controlador.obtener_clientes_derecha()
        self.mostrar_resultados(clientes)

    def listar_izquierda(self):
        clientes = self.controlador.obtener_clientes_izquierda()
        self.mostrar_resultados(clientes)

    def mostrar_resultados(self, lista):
        self.text_resultado.delete("1.0", tk.END)
        for cliente in lista:
            self.text_resultado.insert(tk.END, cliente + "\n")
