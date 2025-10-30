#INSTITUTO TECNOLOGICO DE SAN JUAN DEL RIO 
#ESTRUCTURA DE DATOS 
#UNIDAD 3
#NOMBRE : ROCIO MOLINA MONROY 
#-----------------------------------------------------------
class Nodo:
    """Nodo individual dentro de una lista doblemente enlazada."""
    def __init__(self, dato):
        self.dato = dato
        self.prev = None
        self.next = None

class ListaDoble:
    """Lista doblemente enlazada con operaciones básicas."""
    def __init__(self):
        self.head = None
        self.tail = None

    # Insertar al final de la lista
    def push_back(self, x):
        n = Nodo(x)
        n.prev = self.tail
        if self.tail:
            self.tail.next = n
        else:
            self.head = n
        self.tail = n

    def remove_node(self, nodo):
        """
        Elimina un nodo específico de la lista en tiempo constante.
        Método tomado de ejercicios previos.
        """
        if not nodo:
            return
        if nodo.prev:
            nodo.prev.next = nodo.next
        else:
            self.head = nodo.next
        if nodo.next:
            nodo.next.prev = nodo.prev
        else:
            self.tail = nodo.prev
        nodo.prev = nodo.next = None

    def forward(self):
        cur, out = self.head, []
        while cur:
            out.append(cur.dato)
            cur = cur.next
        return out

    # ---------------------------------------------------------------
    # NUEVO MÉTODO: Eliminar elementos repetidos - Tiempo O(n)
    # ---------------------------------------------------------------
    def remove_dups(self):
        """
        Elimina duplicados manteniendo solo la primera vez que aparece cada valor.
        Utiliza un conjunto para registrar los datos ya encontrados.
        """
        vistos = set()  # Espacio proporcional al número de elementos únicos
        cur = self.head

        # Recorrido completo de la lista
        while cur:
            dato_actual = cur.dato

            if dato_actual in vistos:
                # Si ya lo vimos antes, lo eliminamos

                borrar = cur  # Guardamos el nodo a eliminar

                cur = cur.next  # Avanzamos antes de eliminar para no perder la referencia

                self.remove_node(borrar)  # Eliminación directa
            else:
                # Si es la primera vez que aparece, lo registramos
                vistos.add(dato_actual)

                cur = cur.next  # Continuamos con el siguiente nodo

        print(f"  [ÉXITO]: Se eliminaron los duplicados. Elementos únicos: {vistos}")

# Crear lista con elementos repetidos
ld = ListaDoble()
ld.push_back(10)
ld.push_back(20)
ld.push_back(10)  # Repetido
ld.push_back(30)
ld.push_back(20)  # Repetido
ld.push_back(40)
ld.push_back(50)
ld.push_back(30)  # Repetido

print(f"Lista Inicial: {ld.forward()}")
print("-" * 40)

# Ejecutar eliminación de duplicados
ld.remove_dups()

# Mostrar lista final
print(f"Lista Final (sin duplicados): {ld.forward()}")

# Probar con una lista sin elementos repetidos
print("\n--- Prueba con lista sin duplicados ---")
ld2 = ListaDoble()
ld2.push_back(1)
ld2.push_back(2)
ld2.push_back(3)

print(f"Lista Inicial: {ld2.forward()}")
ld2.remove_dups()
print(f"Lista Final: {ld2.forward()}")

print("-" * 40)