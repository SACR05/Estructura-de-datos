import os # Ayuda a limpiar la pantalla

class NodoCliente:
    
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.siguiente = None  # Apuntador al siguiente nodo
        self.anterior = None   # Apuntador al nodo anterior

class ListaDobleClientes:
    
    def __init__(self):
        self.primero = None  # Apuntador al primer nodo de la lista
        self.ultimo = None   # Apuntador al último nodo de la lista
        self.tamanio = 0     # Contador de elementos en la lista

    def esta_vacia(self):
        """Verifica si la lista está vacía."""
        return self.primero is None

    def insertar_cliente_ordenado(self, cedula, nombre):
        
        #Inserta un nuevo cliente en la lista de forma ordenada por cédula.
    
        temp = self.primero
        while temp:
            if temp.cedula == cedula:
                print(f"Error: La cédula '{cedula}' ya existe. No se insertó el cliente.")
                return 
            temp = temp.siguiente

        nuevo_nodo = NodoCliente(cedula, nombre)
        self.tamanio += 1

        # 1: Lista vacía
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            print(f"Cliente '{nombre}' (Cédula: {cedula}) insertado correctamente (lista estaba vacía).")
            return

        # 2: Insertar al principio la cedula escrita por el usuario en el input
        if nuevo_nodo.cedula < self.primero.cedula:
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo
            print(f"Cliente '{nombre}' (Cédula: {cedula}) insertado correctamente (al inicio).")
            return

        if nuevo_nodo.cedula > self.ultimo.cedula:
             nuevo_nodo.anterior = self.ultimo
             self.ultimo.siguiente = nuevo_nodo
             self.ultimo = nuevo_nodo
             print(f"Cliente '{nombre}' (Cédula: {cedula}) insertado correctamente (al final).")
             return

        
        actual = self.primero
        # Avanzamos hasta encontrar el nodo ANTERIOR a donde debemos insertar
      
        while actual.siguiente is not None and actual.siguiente.cedula < nuevo_nodo.cedula:
            actual = actual.siguiente


        nuevo_nodo.siguiente = actual.siguiente
        nuevo_nodo.anterior = actual
        if actual.siguiente is not None:
             actual.siguiente.anterior = nuevo_nodo
        actual.siguiente = nuevo_nodo

     
        print(f"Cliente '{nombre}' (Cédula: {cedula}) insertado correctamente (en medio).")


    def listar_clientes_derecha(self):
        # Imprime los clientes desde el primer nodo hasta el último.
        if self.esta_vacia():
            print("\n--- Lista de Clientes (Izquierda a Derecha) ---")
            print("La lista está vacía.")
            print("------------------------------------------------")
            return

        print("\n--- Lista de Clientes (Izquierda a Derecha) ---")
        actual = self.primero
        contador = 1
        while actual:
            print(f"{contador}. Cédula: {actual.cedula}, Nombre: {actual.nombre}")
            actual = actual.siguiente
            contador += 1
        print(f"Total de clientes: {self.tamanio}")
        print("------------------------------------------------")

    def listar_clientes_izquierda(self):
        # Imprime los clientes desde el último nodo hasta el primero.
        if self.esta_vacia():
            print("\n--- Lista de Clientes (Derecha a Izquierda) ---")
            print("La lista está vacía.")
            print("------------------------------------------------")
            return

        print("\n--- Lista de Clientes (Derecha a Izquierda) ---")
        actual = self.ultimo
        contador = self.tamanio # Empezar a contar desde el total
        while actual:
            print(f"{contador}. Cédula: {actual.cedula}, Nombre: {actual.nombre}")
            actual = actual.anterior
            contador -= 1
        print(f"Total de clientes: {self.tamanio}")
        print("------------------------------------------------")

def mostrar_menu():
    #Muestra el menú de opciones al usuario.
    print("\n========= MENÚ DE CLIENTES =========")
    print("1. Insertar Cliente (Ordenado por cédula)")
    print("2. Listar Clientes (Hacia la derecha ->)")
    print("3. Listar Clientes (Hacia la izquierda <-)")
    print("4. Salir")
    print("====================================")

def limpiar_pantalla():
   
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Programa Principal ---
if __name__ == "__main__":
    lista_clientes = ListaDobleClientes()
    opcion = ""

    while opcion != "4":
   
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Insertar Cliente ---")
            while True:
                try:
                    # Intentamos convertir a entero para asegurar orden numérico

                    cedula = int(input("Ingrese la cédula del cliente: "))
                    break # Salir del bucle si la conversión es exitosa
                except ValueError:
                    print("Error: La cédula debe ser un valor numérico.")

            nombre = input("Ingrese el nombre del cliente: ")
            if nombre.strip(): # Validar que el nombre no esté vacío
                lista_clientes.insertar_cliente_ordenado(cedula, nombre)
            else:
                print("Error: El nombre no puede estar vacío.")
            input("\nPresione Enter para continuar...") # Siempre que sale este comentario o input se pausa para que el usuario vea el resultado

        elif opcion == "2":
            lista_clientes.listar_clientes_derecha()
            input("\nPresione Enter para continuar...") 

        elif opcion == "3":
            lista_clientes.listar_clientes_izquierda()
            input("\nPresione Enter para continuar...") 

        elif opcion == "4":
            print("\nSaliendo de la aplicación...")

        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")
            input("\nPresione Enter para continuar...") 

    print("¡Hasta luego!")
