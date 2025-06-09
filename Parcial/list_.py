from typing import Any, Optional

class List(list):

    CRITERION_FUNCTIONS = {}

    def add_criterion(
        self,
        key_criterion: str, # El nombre del criterio (ej. 'por_edad', 'por_nombre').
        function, # La función que extrae el valor comparable de un elemento.
    ):
        """
        Agrega una nueva función de criterio al diccionario CRITERION_FUNCTIONS.
        Esta función se utilizará más adelante para ordenar o buscar basándose en este criterio.
        """
        self.CRITERION_FUNCTIONS[key_criterion] = function

    def show(
        self
    ) -> None:
        """
        Itera a través de cada elemento en la lista y lo imprime en la consola.
        """
        for element in self:
            print(element)

    def delete_value(
        self,
        value, # El valor a buscar y eliminar.
        key_value: str = None, # Opcional: La clave del criterio a usar para buscar si los elementos son objetos.
    ) -> Optional[Any]:
        """
        Elimina la primera ocurrencia de un valor especificado de la lista.
        Utiliza el método 'search' para encontrar el índice del valor.
        Si se encuentra, elimina el elemento usando pop() y lo devuelve; de lo contrario, devuelve None.
        """
        index = self.search(value, key_value)
        # Si se encuentra un índice, se elimina y devuelve el elemento; de lo contrario, se devuelve None.
        return self.pop(index) if index is not None else index

    # def insert_value(
    #     self,
    #     value: Any,
    # ) -> None:
    #     # list_number.append(2)
    #     # list_number.insert(1, 11)
    #     pass

    def sort_by_criterion(
        self,
        criterion_key: str = None, # Opcional: La clave de la función de criterio a usar para ordenar.
    ) -> None:
        """
        Ordena la lista basándose en una función de criterio especificada.
        Si se proporciona una clave de criterio y se encuentra, utiliza esa función para ordenar.
        Si no se proporciona ninguna clave de criterio, o si la lista contiene tipos básicos (int, str, bool),
        intenta una ordenación estándar. De lo contrario, imprime un mensaje de error.
        """
        # Obtiene la función de criterio del diccionario usando la clave proporcionada.
        criterion = self.CRITERION_FUNCTIONS.get(criterion_key)

        if criterion is not None:
            # Si se encuentra una función de criterio, ordena la lista usando esa función como clave.
            self.sort(key=criterion)
        elif self and isinstance(self[0], (int, str, bool)):
            # Si la lista contiene tipos básicos y no se da un criterio específico, realiza una ordenación por defecto.
            self.sort()
        else:
            # Si no se encuentra un criterio válido y los elementos no son tipos básicos, informa al usuario.
            print('criterio de orden no encontrado')

    def search(self,search_value,search_key: str = None,) -> int:
        """
        Busca un valor específico en la lista usando un algoritmo de búsqueda binaria.
        Primero ordena la lista por el criterio especificado (o por defecto si no se proporciona).
        Devuelve el índice del valor encontrado; de lo contrario, devuelve None.
        Nota: Este método asume que la lista está ordenada según la search_key.
        """
        # Primero, ordena la lista por el criterio especificado para habilitar la búsqueda binaria.
        self.sort_by_criterion(search_key)

        start = 0
        end = len(self) - 1
        middle = (start + end) // 2

        # Realiza la búsqueda binaria.
        while start <= end:
            # Obtiene la función de criterio para la búsqueda.
            criterion = self.CRITERION_FUNCTIONS.get(search_key)

            # Si no se encuentra un criterio y los elementos no son tipos básicos, no podemos buscar.
            if criterion is None and self and not isinstance(self[0], (int, str, bool)):
                return None

            # Determina el valor a comparar: ya sea aplicando el criterio o usando el elemento directamente.
            value = criterion(self[middle]) if criterion else self[middle]

            if value == search_value:
                # Si se encuentra el valor, devuelve su índice.
                return middle
            elif value < search_value:
                # Si el valor de búsqueda es mayor, ajusta el puntero 'start'.
                start = middle + 1
            else:
                # Si el valor de búsqueda es menor, ajusta el puntero 'end'.
                end = middle - 1
            # Recalcula el índice medio.
            middle = (start + end) // 2