from typing import Any, Optional

class Queue:


    def __init__(self):
        """
        Inicializa una nueva instancia de la cola.
        El atributo '__elements' es una lista privada que almacena los elementos de la cola.
        """
        self.__elements = []

    def arrive(self, value: Any) -> None:
        """
        Agrega un elemento al final de la cola.
        
        Args:
            value (Any): El elemento a agregar a la cola.
        """
        self.__elements.append(value)

    def attention(self) -> Optional[Any]:
        """
        Elimina y devuelve el primer elemento de la cola (el elemento "en atención").
        Si la cola está vacía, devuelve None.
        
        Returns:
            Optional[Any]: El primer elemento de la cola o None si está vacía.
        """
        return (
            self.__elements.pop(0)
            if self.__elements
            else None
        )

    def size(self) -> int:
        """
        Devuelve el número actual de elementos en la cola.
        
        Returns:
            int: El número de elementos en la cola.
        """
        return len(self.__elements)
    
    def on_front(self) -> Optional[Any]:
        """
        Devuelve el primer elemento de la cola sin eliminarlo.
        Si la cola está vacía, devuelve None.
        
        Returns:
            Optional[Any]: El primer elemento de la cola o None si está vacía.
        """
        return (
            self.__elements[0]
            if self.__elements
            else None
        )

    def move_to_end(self) -> Optional[Any]:
        """
        Mueve el primer elemento de la cola al final de la misma.
        Esto simula que un elemento ha sido "atendido" y luego "vuelve a la fila".
        Si la cola está vacía, no hace nada y devuelve None.
        
        Returns:
            Optional[Any]: El elemento que fue movido al final, o None si la cola estaba vacía.
        """
        if self.__elements:
            value = self.attention()  # Quita el primer elemento
            self.arrive(value)        # Lo agrega al final
            return value
        return None
    
    def show(self):
        """
        Muestra todos los elementos de la cola en el orden actual,
        moviendo cada elemento al final de la cola después de imprimirlo.
        Esto significa que la cola original se altera y los elementos se rotan.
        """
        for i in range(len(self.__elements)):
            print(self.move_to_end())