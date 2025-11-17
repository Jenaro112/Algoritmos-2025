from typing import Any, Optional

class Stack:
    """
    Esta clase implementa una estructura de datos de pila (LIFO - Last In, First Out).
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de la pila.
        El atributo '__elements' es una lista privada que almacena los elementos de la pila.
        """
        self.__elements = []

    def push(self, value: Any) -> None:
        """
        Agrega un elemento a la parte superior (final) de la pila.
        
        Args:
            value (Any): El elemento a agregar a la pila.
        """
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:
        """
        Elimina y devuelve el elemento superior (el último en ser agregado) de la pila.
        Si la pila está vacía, devuelve None.
        
        Returns:
            Optional[Any]: El elemento superior de la pila o None si está vacía.
        """
        return (
            self.__elements.pop()
            if self.__elements
            else None
        )

    def size(self) -> int:
        """
        Devuelve el número actual de elementos en la pila.
        
        Returns:
            int: El número de elementos en la pila.
        """
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:
        """
        Devuelve el elemento superior de la pila sin eliminarlo.
        Si la pila está vacía, devuelve None.
        
        Returns:
            Optional[Any]: El elemento superior de la pila o None si está vacía.
        """
        return (
            self.__elements[-1]
            if self.__elements
            else None
        )

    def show(self):
        """
        Muestra todos los elementos de la pila desde la parte superior hasta la base,
        y luego restaura la pila a su estado original.
        Utiliza una pila auxiliar para preservar el orden.
        """
        aux_stack = Stack()  # Crea una pila auxiliar para almacenar temporalmente los elementos
        
        # Saca todos los elementos de la pila original, los imprime y los guarda en la pila auxiliar
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value)
        
        # Devuelve los elementos de la pila auxiliar a la pila original para restaurarla
        while aux_stack.size() > 0:
            self.push(aux_stack.pop())