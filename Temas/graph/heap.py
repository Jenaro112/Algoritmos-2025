from typing import Any

class HeapMax:
    """
    Implementación de un Max Heap (Montículo de Máximos).
    Es una estructura de datos de árbol donde el nodo padre siempre es
    mayor o igual que sus hijos. El elemento más grande está siempre en la raíz.
    """

    def __init__(self):
        """Inicializa un heap vacío usando una lista para almacenar los elementos."""
        self.elements = []
    
    def size(self) -> int:
        """Devuelve el número de elementos en el heap."""
        return len(self.elements)

    def add(self, value: Any) -> None:
        """Agrega un nuevo elemento al heap y lo reordena para mantener la propiedad de Max Heap."""
        # 1. Agrega el elemento al final de la lista.
        self.elements.append(value)
        # 2. Llama a `float` para que el nuevo elemento "flote" hacia arriba
        #    hasta encontrar su posición correcta.
        self.float(self.size()-1)
    
    def remove(self) -> Any:
        """Elimina y devuelve el elemento máximo (la raíz) del heap."""
        # 1. Intercambia la raíz (el máximo) con el último elemento.
        last = self.size() -1
        self.interchange(0, last)
        # 2. Elimina el último elemento (que ahora es el máximo original).
        value = self.elements.pop()
        # 3. Llama a `sink` para que la nueva raíz (que era el último elemento)
        #    "se hunda" hasta su posición correcta, restaurando la propiedad del heap.
        self.sink(0)
        return value

    def float(self, index: int) -> None:
        """
        Hace que un elemento en un índice dado "flote" hacia arriba en el heap
        mientras sea mayor que su padre.
        """
        # Calcula el índice del nodo padre.
        father = (index - 1) // 2
        # Mientras no hayamos llegado a la raíz y el elemento actual sea mayor que su padre...
        while index > 0 and self.elements[index] > self.elements[father]:
            # ...intercambiamos el elemento con su padre.
            self.interchange(index, father)
            # Actualizamos los índices para seguir subiendo.
            index = father
            father = (index - 1) // 2

    def sink(self, index: int) -> None:
        """
        Hace que un elemento en un índice dado "se hunda" hacia abajo en el heap
        mientras sea menor que alguno de sus hijos.
        """
        # Calcula el índice del hijo izquierdo.
        left_son = (2 * index) + 1
        control = True
        # Mientras el nodo tenga al menos un hijo izquierdo...
        while control and left_son < self.size():
            right_son = left_son + 1

            # Se determina cuál de los dos hijos es el mayor.
            mayor = left_son
            if right_son < self.size():
                if self.elements[right_son] > self.elements[mayor]:
                    mayor = right_son

            # Si el nodo actual es menor que su hijo mayor...
            if self.elements[index] < self.elements[mayor]:
                # ...los intercambiamos.
                self.interchange(index, mayor)
                # Actualizamos los índices para seguir hundiéndonos.
                index = mayor
                left_son = (2 * index) + 1
            else:
                # Si el nodo ya es mayor que sus hijos, está en su lugar y paramos.
                control = False


    def interchange(self, index_1: int, index_2: int) -> None:
        """Función auxiliar para intercambiar dos elementos en la lista."""
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def heapsort(self) -> list:
        """
        Ordena una lista utilizando el algoritmo Heapsort.
        Funciona extrayendo repetidamente el elemento máximo del heap.
        """
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result

    def arrive(self, value: Any, priority: int) -> None:
        """Método para usar el heap como una cola de prioridad (mayor prioridad primero)."""
        self.add([priority, value])
    
    def attention(self) -> Any:
        """Método para atender (extraer) el elemento con la mayor prioridad."""
        value = self.remove()
        return value


class HeapMin:
    """
    Implementación de un Min Heap (Montículo de Mínimos).
    Es una estructura de datos de árbol donde el nodo padre siempre es
    menor o igual que sus hijos. El elemento más pequeño está siempre en la raíz.
    Esencial para algoritmos como Dijkstra.
    """

    def __init__(self):
        """Inicializa un heap vacío."""
        self.elements = []
    
    def size(self) -> int:
        """Devuelve el número de elementos en el heap."""
        return len(self.elements)

    def add(self, value: Any) -> None:
        """Agrega un nuevo elemento al heap y lo reordena."""
        self.elements.append(value)
        self.float(self.size()-1)
    
    def search(self, value):
        """
        Busca un valor específico dentro de los elementos del heap.
        Nota: Esta es una búsqueda lineal (lenta), usada en algoritmos como Dijkstra
        para encontrar un nodo específico en la cola de prioridad.
        """
        for index, element in enumerate(self.elements):
            # Asume que el elemento es una tupla/lista y el valor a buscar está en element[1][0].
            if element[1][0] == value:
                return index

    def remove(self) -> Any:
        """Elimina y devuelve el elemento mínimo (la raíz) del heap."""
        last = self.size() -1
        self.interchange(0, last)
        value = self.elements.pop()
        self.sink(0)
        return value

    def float(self, index: int) -> None:
        """Hace que un elemento "flote" hacia arriba mientras sea menor que su padre."""
        father = (index - 1) // 2
        # La lógica es la misma que en HeapMax, pero la condición es a la inversa (<).
        while index > 0 and self.elements[index] < self.elements[father]:
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index: int) -> None:
        """Hace que un elemento "se hunda" mientras sea mayor que alguno de sus hijos."""
        left_son = (2 * index) + 1
        control = True
        while control and left_son < self.size():
            right_son = left_son + 1

            # Busca cuál de los dos hijos es el menor.
            minor = left_son
            if right_son < self.size():
                if self.elements[right_son] < self.elements[minor]:
                    minor = right_son

            # Si el nodo actual es mayor que su hijo menor, los intercambia.
            if self.elements[index] > self.elements[minor]:
                self.interchange(index, minor)
                index = minor
                left_son = (2 * index) + 1
            else:
                control = False


    def interchange(self, index_1: int, index_2: int) -> None:
        """Función auxiliar para intercambiar dos elementos."""
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def heapsort(self) -> list:
        """Ordena una lista extrayendo repetidamente el elemento mínimo. El resultado será descendente."""
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result

    def arrive(self, value: Any, priority: int) -> None:
        """Método para usar el heap como una cola de prioridad (menor prioridad/costo primero)."""
        self.add([priority, value])
    
    def attention(self) -> Any:
        """Método para atender (extraer) el elemento con la menor prioridad/costo."""
        value = self.remove()
        return value

    def change_priority(self, index, new_priority):
        """
        Cambia la prioridad (costo) de un elemento en el heap y lo reubica.
        Es una operación clave para el algoritmo de Dijkstra.
        """
        if index < len(self.elements):
            previous_priority = self.elements[index][0]
            self.elements[index][0] = new_priority
            # Si la nueva prioridad es mayor, el elemento debe hundirse.
            if new_priority > previous_priority:
                self.sink(index)
            # Si la nueva prioridad es menor, el elemento debe flotar.
            elif new_priority < previous_priority:
                self.float(index)
