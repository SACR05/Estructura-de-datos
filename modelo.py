
class Nodo:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.anterior = None
        self.siguiente = None

# TDA ListaDoble: maneja inserción y recorrido de clientes
class ListaDoble:
    def __init__(self):
        self.primero = None

    def insertar_ordenado(self, cedula, nombre):
        nuevo = Nodo(cedula, nombre)
        if self.primero is None:
            self.primero = nuevo
            return

        actual = self.primero
        anterior = None
        while actual and cedula > actual.cedula:
            anterior = actual
            actual = actual.siguiente

        if anterior is None:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo
        else:
            nuevo.siguiente = actual
            nuevo.anterior = anterior
            anterior.siguiente = nuevo
            if actual:
                actual.anterior = nuevo

    def listar_derecha(self):
        resultados = []
        actual = self.primero
        while actual:
            resultados.append(f"{actual.cedula} - {actual.nombre}")
            actual = actual.siguiente
        return resultados

    def listar_izquierda(self):
        resultados = []
        actual = self.primero
        if actual is None:
            return resultados
        while actual.siguiente:
            actual = actual.siguiente
        while actual:
            resultados.append(f"{actual.cedula} - {actual.nombre}")
            actual = actual.anterior
        return resultados
