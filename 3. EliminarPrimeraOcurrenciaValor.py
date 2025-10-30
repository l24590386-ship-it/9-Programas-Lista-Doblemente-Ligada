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
    """Estructura de lista doblemente enlazada con operaciones básicas."""
    def __init__(self):
        self.head = None
        self.tail = None

    # Añadir al inicio de la lista
    # Tiempo constante: O(1)
    def push_front(self, x):
        n = Nodo(x)
        n.next = self.head

        if self.head:
            self.head.prev = n
        else:
            # Si no había elementos, este nodo será también el final
            self.tail = n

        self.head = n

    # Añadir al final de la lista
    # Tiempo constante: O(1)
    def push_back(self, x):
        n = Nodo(x)
        n.prev = self.tail

        if self.tail:
            self.tail.next = n
        else:
            # Si la lista estaba vacía, este nodo será también el inicio
            self.head = n

        self.tail = n

    # Buscar un nodo con cierto valor
    def find(self, v):
        cur = self.head
        while cur:
            if cur.dato == v: return cur
            cur = cur.next
        return None

    # -----------------------------------------------
    # MÉTODO NUEVO 1: Quitar un nodo directamente - O(1)
    # -----------------------------------------------
    def remove_node(self, nodo):
        """
        Elimina un nodo específico de la lista, considerando si es el primero o el último.
        """
        # Si el nodo no existe, no se hace nada
        if not nodo:
            return

        # Actualiza el enlace del nodo anterior
        if nodo.prev:
            # Si no es el primero, el anterior apunta al siguiente
            nodo.prev.next = nodo.next
        else:
            # Si es el primero, se actualiza la cabeza
            self.head = nodo.next

        # Actualiza el enlace del nodo siguiente
        if nodo.next:
            # Si no es el último, el siguiente apunta al anterior
            nodo.next.prev = nodo.prev
        else:
            # Si es el último, se actualiza la cola
            self.tail = nodo.prev

        # Limpieza opcional de referencias
        nodo.prev = nodo.next = None

        # Solo se modifican punteros, por eso es O(1)

    # ------------------------------------------------------
    # MÉTODO NUEVO 2: Eliminar por contenido - O(n) total
    # ------------------------------------------------------
    def remove_value(self, v):
        """
        Localiza y elimina la primera aparición del valor dado.
        """
        # Paso 1: Buscar el nodo (O(n))
        nodo_a_eliminar = self.find(v)

        # Paso 2: Eliminar el nodo si fue encontrado (O(1))
        self.remove_node(nodo_a_eliminar)

        if nodo_a_eliminar:
            print(f"  [ÉXITO]: Se eliminó el valor {v}.")
        else:
            print(f"  [AVISO]: No se encontró el valor {v} en la lista.")

    # Método para recorrer la lista hacia adelante
    def forward(self):
        cur, out = self.head, []
        while cur:
            out.append(cur.dato)
            cur = cur.next
        return out

    # Verifica si la lista está vacía
    def is_empty(self):
        return self.head is None and self.tail is None

# Crear y llenar la lista
ld = ListaDoble()
ld.push_front(5)   # Lista: [5]
ld.push_back(10)   # Lista: [5, 10]
ld.push_back(15)   # Lista: [5, 10, 15]
ld.push_back(20)   # Lista: [5, 10, 15, 20]
ld.push_back(30)   # Lista: [5, 10, 15, 20, 30]

print(f"Lista Inicial: {ld.forward()}")
print("-" * 40)

# PRUEBA 1: Eliminar un valor intermedio (15)
ld.remove_value(15)
print(f"Lista después de eliminar (15): {ld.forward()}")

# PRUEBA 2: Eliminar el primer nodo (5)
ld.remove_value(5)
print(f"Lista después de eliminar la HEAD (5): {ld.forward()}")

# PRUEBA 3: Eliminar el último nodo (30)
ld.remove_value(30)
print(f"Lista después de eliminar la TAIL (30): {ld.forward()}")

# PRUEBA 4: Intentar eliminar un valor que no está (100)
ld.remove_value(100)
print(f"Lista después de eliminar (100): {ld.forward()}")

# PRUEBA 5: Vaciar la lista eliminando los restantes
print("-" * 40)
ld.remove_value(20) # Lista: [10]
ld.remove_value(10) # Lista: []

print(f"Lista después de vaciarla: {ld.forward()} (¿Vacía? {'Sí' if ld.is_empty() else 'No'})")
print("-" * 40)