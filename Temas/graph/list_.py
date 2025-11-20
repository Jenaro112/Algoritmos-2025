from typing import Any, Optional

class List(list):
    """
    Una clase de Lista extendida que hereda de la clase `list` de Python.
    Añade funcionalidades para gestionar criterios de ordenación y búsqueda,
    permitiendo que la lista maneje objetos complejos de manera más flexible.
    """

    # Un diccionario a nivel de clase para almacenar funciones que definen
    # cómo ordenar o buscar por diferentes atributos de los objetos en la lista.
    CRITERION_FUNCTIONS = {}

    def add_criterion(
        self,
        key_criterion: str,
        function,
    ):
        """
        Agrega una nueva función de criterio al diccionario de criterios.
        Estos criterios se usarán para ordenar y buscar en la lista.

        Args:
            key_criterion (str): El nombre (clave) para identificar el criterio.
            function: La función lambda o regular que extrae el valor del criterio de un objeto.
                        Ejemplo: lambda x: x.nombre
        """
        self.CRITERION_FUNCTIONS[key_criterion] = function

    def show(
        self
    ) -> None:
        """
        Imprime en la consola cada elemento de la lista en una nueva línea.
        """
        for element in self:
            print(element)

    def delete_value(
        self,
        value,
        key_value: str = None,
    ) -> Optional[Any]:
        """
        Busca un valor en la lista y, si lo encuentra, lo elimina.

        Args:
            value: El valor a buscar y eliminar.
            key_value (str, optional): El criterio de búsqueda a utilizar. Si es None,
                                        se busca el valor directamente. Defaults to None.

        Returns:
            Optional[Any]: El elemento eliminado, o None si no se encontró.
        """
        index = self.search(value, key_value)
        return self.pop(index) if index is not None else index

    def sort_by_criterion(
        self,
        criterion_key: str = None,
    ) -> None:
        """
        Ordena la lista basándose en un criterio previamente definido.

        Args:
            criterion_key (str, optional): El nombre del criterio por el cual ordenar.
                                            Si es None, intentará un ordenamiento por defecto.
        """
        # Obtiene la función de criterio del diccionario.
        criterion = self.CRITERION_FUNCTIONS.get(criterion_key)

        if criterion is not None:
            # Si se encuentra un criterio, ordena la lista usando esa función como clave.
            self.sort(key=criterion)
        elif self and  isinstance(self[0], (int, str, bool)):
            # Si no hay criterio pero la lista contiene tipos básicos, usa el sort por defecto.
            self.sort()
        else:
            # Si no se puede determinar cómo ordenar, se informa al usuario.
            print('criterio de orden no encontrado')

    def search(
        self,
        search_value,
        search_key: str = None,
    ) -> Optional[int]:
        """
        Realiza una búsqueda binaria en la lista para encontrar un valor.
        La lista DEBE estar ordenada por el criterio de búsqueda para que funcione correctamente.

        Args:
            search_value: El valor que se está buscando.
            search_key (str, optional): El criterio a usar para la búsqueda. Defaults to None.

        Returns:
            Optional[int]: El índice del elemento encontrado, o None si no se encuentra.
        """
        # Primero, ordena la lista por el criterio de búsqueda para asegurar que la búsqueda binaria funcione.
        self.sort_by_criterion(search_key)
        start = 0
        end = len(self) -1
        middle = (start + end) // 2

        while start <= end:
            criterion = self.CRITERION_FUNCTIONS.get(search_key)
            # Si no hay criterio y los elementos no son básicos, no se puede buscar.
            if criterion is None and self and not isinstance(self[0], (int, str, bool)):
                return None

            # Obtiene el valor del elemento en la posición media, usando el criterio si está disponible.
            value = criterion(self[middle]) if criterion else self[middle]
            
            if value == search_value:
                return middle
            # Ajusta los límites de la búsqueda (start, end) para la siguiente iteración.
            elif value  < search_value:
                start = middle +1
            else:
                end = middle -1
            middle = (start + end) // 2
