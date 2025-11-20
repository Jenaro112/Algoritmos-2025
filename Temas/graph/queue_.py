from typing import Any, Optional

class Queue:
    """
    Representa una estructura de datos de tipo Cola (Queue).
    Funciona bajo el principio FIFO (First In, First Out), donde el primer
    elemento en entrar es el primero en salir.
    """

    def __init__(self):
        """
        Inicializa una nueva cola vacía.
        Utiliza una lista interna de Python para almacenar los elementos.
        """
        self.__elements = []

    def arrive(self, value: Any) -> None:
        """
        Agrega un elemento al final (final de la cola).

        Args:
            value (Any): El elemento que se va a agregar a la cola.
        """
        self.__elements.append(value)

    def attention(self) -> Optional[Any]:
        """
        Elimina y devuelve el elemento que se encuentra al frente de la cola.

        Returns:
            Optional[Any]: El elemento del frente, o None si la cola está vacía.
        """
        return (
            self.__elements.pop(0)
            if self.__elements
            else None
        )

    def size(self) -> int:
        """
        Devuelve el número de elementos que contiene la cola.

        Returns:
            int: La cantidad de elementos en la cola.
        """
        return len(self.__elements)
    
    def on_front(self) -> Optional[Any]:
        """
        Devuelve el elemento del frente de la cola sin eliminarlo.

        Returns:
            Optional[Any]: El elemento del frente, o None si la cola está vacía.
        """
        return (
            self.__elements[0]
            if self.__elements
            else None
        )

    def move_to_end(self) -> Optional[Any]:
        """
        Toma el elemento del frente de la cola y lo mueve al final.
        Es útil para recorrer la cola sin perder sus elementos.

        Returns:
            Optional[Any]: El elemento que fue movido, o None si la cola está vacía.
        """
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return value
    
    def show(self):
        """
        Muestra todos los elementos de la cola de forma no destructiva.
        Lo hace moviendo cada elemento al final y mostrándolo,
        dejando la cola en su estado original al terminar.
        """
        for i in range(len(self.__elements)):
            print(self.move_to_end())
