
from modelo import ListaDoble

# Controlador: conecta la vista con el modelo
class Controlador:
    def __init__(self):
        self.lista = ListaDoble()

    def insertar_cliente(self, cedula, nombre):
        self.lista.insertar_ordenado(cedula, nombre)

    def obtener_clientes_derecha(self):
        return self.lista.listar_derecha()

    def obtener_clientes_izquierda(self):
        return self.lista.listar_izquierda()
