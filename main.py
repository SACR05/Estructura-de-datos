class Eje:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.siguiente = None

# Clase que define la lista simple
class ListaSimple:
    def __init__(self):
        self.inicio = None

    def insertar_ordenado(self, cedula, nombre):
        nuevo = Eje(cedula, nombre)
        if self.inicio is None or cedula < self.inicio.cedula:
            nuevo.siguiente = self.inicio
            self.inicio = nuevo
        else:
            actual = self.inicio
            while actual.siguiente and actual.siguiente.cedula < cedula:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo

        print(f"Cliente {nombre} insertado con éxito.")

    def listar_derecha(self):
        if not self.inicio:
            print("No hay nada en la lista")
            return
        actual = self.inicio
        print("Clientes:")
        while actual:
            print(f"Cédula: {actual.cedula}, Nombre: {actual.nombre}")
            actual = actual.siguiente

def menu():
    lista = ListaSimple()
    while True:
        print("Menu")
        print("1. Nuevo cliente")
        print("2. Listar clientes")
        print("3. Salir")
        opcion = input("Seleccione una de las 3 opciones: ")

        if opcion == "1":
            try:
                cedula = int(input("Ingrese la cédula del usuario: "))
                nombre = input("Ingrese el nombre del cliente: ")
                lista.insertar_ordenado(cedula, nombre)
            except ValueError:
                print("Cédula inválida, ingrésela correctamente.")
        elif opcion == "2":
            lista.listar_derecha()
        elif opcion == "3":
            print("Hasta luego, nos veremos en una próxima ocasión.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()