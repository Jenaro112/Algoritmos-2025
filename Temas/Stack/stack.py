
from typing import Any, Optional


class Stack:
    """
    Representa una estructura de datos de tipo Pila (Stack).
    Funciona bajo el principio LIFO (Last In, First Out), donde el último
    elemento en entrar es el primero en salir.
    """

    def __init__(self):
        """
        Inicializa una nueva pila vacía.
        Utiliza una lista interna de Python para almacenar los elementos.
        """
        self.__elements = []


    def push(self, value: Any) -> None:
        """
        Agrega un elemento a la cima (top) de la pila.

        Args:
            value (Any): El elemento que se va a agregar a la pila.
        """
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:
        """
        Elimina y devuelve el elemento que se encuentra en la cima de la pila.

        Returns:
            Optional[Any]: El elemento de la cima, o None si la pila está vacía.
        """
        return (
            self.__elements.pop()
            if self.__elements
            else None
        )

    def size(self) -> int:
        """
        Devuelve el número de elementos que contiene la pila.

        Returns:
            int: La cantidad de elementos en la pila.
        """
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:
        """
        Devuelve el elemento de la cima de la pila sin eliminarlo.

        Returns:
            Optional[Any]: El elemento de la cima, o None si la pila está vacía.
        """
        return (
            self.__elements[-1]
            if self.__elements
            else None
        )

    def show(self):
        """
        Muestra todos los elementos de la pila, desde la cima hasta la base,
        sin alterar el contenido original de la misma.
        """
        aux_stack = Stack()
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value)
        
        while aux_stack.size() > 0:
            self.push(aux_stack.pop())
