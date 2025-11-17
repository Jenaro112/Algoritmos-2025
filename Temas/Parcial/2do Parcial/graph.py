from typing import Any, Optional

# Importaciones de estructuras de datos auxiliares desde otros archivos del proyecto.
from heap import HeapMin
from list_ import List
from queue_ import Queue
from stack import Stack

# La clase Graph hereda de List, lo que significa que un grafo es, en esencia, una lista de vértices.
class Graph(List):

    class __nodeVertex:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.edges = List()
            # Se definen criterios de ordenación para la lista de aristas.
            self.edges.add_criterion('value', Graph._order_by_value)
            self.edges.add_criterion('weight', Graph._order_by_weight)
            self.other_values = other_values
            self.visited = False
        
        def __str__(self):
            return str(self.value) #se agrego el str (string) para que muestre bien

    class __nodeEdge:

        def __init__(self, value: Any, weight: Any, other_values: Optional[Any] = None):
            self.value = value
            self.weight = weight
            self.other_values = other_values
        
        def __str__(self):
            return f'Destination: {self.value} with weight --> {self.weight}'
    
    def __init__(self, is_directed=False):
        """
        Inicializa un grafo.

        Args:
            is_directed (bool): Indica si el grafo es dirigido o no.
        """
        # Se añade un criterio de ordenación para la lista de vértices (el propio grafo).
        self.add_criterion('value', self._order_by_value)
        self.is_directed = is_directed

    def _order_by_value(item):
        return item.value

    def _order_by_weight(item):
        return item.weight
    
    # Muestra el grafo completo, listando cada vértice y sus aristas adyacentes.
    def show(
        self
    ) -> None:
        """Muestra el grafo completo, listando cada vértice y sus aristas adyacentes."""
        for vertex in self:
            print(f"Vertex: {vertex}")
            vertex.edges.show() 

    # Inserta un nuevo vértice en el grafo.
    def insert_vertex(
        self,
        value: Any,
        other_values: Optional[Any] = None) -> None: #añadido el other_values
        """
        Inserta un nuevo vértice en el grafo.

        Args:
            value (Any): El valor del vértice a insertar.
            other_values (Optional[Any], optional): Otros valores asociados al vértice. Defaults to None.
        """
        node_vertex = Graph.__nodeVertex(value)
        self.append(node_vertex)
        

    def insert_edge(self, origin_vertex: Any, destination_vertex: Any, weight: int) -> None: # Inserta una arista entre dos vértices.
        """
        Inserta una arista entre dos vértices con un peso determinado.

        Args:
            origin_vertex (Any): El valor del vértice de origen.
            destination_vertex (Any): El valor del vértice de destino.
            weight (int): El peso de la arista.
        """
        origin = self.search(origin_vertex, 'value')
        destination = self.search(destination_vertex, 'value')
        if origin is not None and destination is not None:
            node_edge = Graph.__nodeEdge(destination_vertex, weight)
            self[origin].edges.append(node_edge)
            if not self.is_directed and origin != destination: #Se acomodo el problema de grafo dirigido o no dirigido (lo tomaba al reves)
                node_edge = Graph.__nodeEdge(origin_vertex, weight)
                self[destination].edges.append(node_edge)
        else:
            print('no se puede insertar falta uno de los vertices')

    # Elimina una arista entre un origen y un destino.
    def delete_edge(
        self,
        origin,
        destination,
        key_value: str = None,
    ) -> Optional[Any]:
        """
        Elimina una arista entre un vértice de origen y uno de destino.

        Args:
            origin (Any): El valor del vértice de origen.
            destination (Any): El valor del vértice de destino.
            key_value (str, optional): La clave para buscar los vértices. Defaults to None.

        Returns:
            Optional[Any]: La arista eliminada o None si no se encontró.
        """
        pos_origin = self.search(origin, key_value)
        if pos_origin is not None:
            # Elimina la arista de la lista de adyacencia del vértice de origen.
            edge = self[pos_origin].edges.delete_value(destination, key_value)
            if not self.is_directed and edge is not None: # Si el grafo NO es dirigido, elimina también la arista en sentido contrario.
                pos_destination = self.search(destination, key_value)
                if pos_destination is not None:
                    self[pos_destination].edges.delete_value(origin, key_value)
            return edge

    # Elimina un vértice del grafo y todas las aristas conectadas a él.
    def delete_vertex(
        self,
        value,
        key_value_vertex: str = None,
        key_value_edges: str = 'value',
    ) -> Optional[Any]:
        """
        Elimina un vértice del grafo y todas las aristas conectadas a él.

        Args:
            value (Any): El valor del vértice a eliminar.
            key_value_vertex (str, optional): La clave para buscar el vértice. Defaults to None.
            key_value_edges (str, optional): La clave para buscar las aristas a eliminar. Defaults to 'value'.

        Returns:
            Optional[Any]: El vértice eliminado o None si no se encontró.
        """
        delete_value = self.delete_value(value, key_value_vertex)
        # Si el vértice se eliminó correctamente, recorre todos los demás vértices para eliminar las aristas que apuntaban a él.
        if delete_value is not None:
            for vertex in self:
                self.delete_edge(vertex.value, value, key_value_edges)
        return delete_value

    # Marca todos los vértices del grafo como no visitados. Útil para reiniciar recorridos.
    def mark_as_unvisited(self) -> None:
        """Marca todos los vértices del grafo como no visitados."""
        for vertex in self:
            vertex.visited = False

    # Determina si existe un camino entre un vértice de origen y uno de destino usando un recorrido en profundidad.
    def exist_path(self, origin, destination):
        """
        Determina si existe un camino entre un vértice de origen y uno de destino.

        Args:
            origin (Any): El valor del vértice de origen.
            destination (Any): El valor del vértice de destino.

        Returns:
            bool: True si existe un camino, False en caso contrario.
        """
        def __exist_path(graph, origin, destination):
            result = False
            vertex_pos = graph.search(origin, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    if graph[vertex_pos].value == destination:
                        return True
                    else:
                        for edge in graph[vertex_pos].edges:
                            destination_edge_pos = graph.search(edge.value, 'value')
                            if not graph[destination_edge_pos].visited:
                                result = __exist_path(graph, graph[destination_edge_pos].value, destination)
                                if result:
                                    break
            return result
        
        self.mark_as_unvisited()
        result = __exist_path(self, origin, destination)
        return result
    
    # Realiza un recorrido en profundidad (DFS - Depth-First Search) desde un vértice de inicio.
    def deep_sweep(self, value) -> None:
        """
        Realiza un recorrido en profundidad (DFS) desde un vértice de inicio.

        Args:
            value (Any): El valor del vértice desde el cual comenzar el recorrido.
        """
        def __deep_sweep(graph, value):
            vertex_pos = graph.search(value, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    print(graph[vertex_pos])
                    for edge in graph[vertex_pos].edges:
                        destination_edge_pos = graph.search(edge.value, 'value')
                        if not graph[destination_edge_pos].visited:
                            __deep_sweep(graph, graph[destination_edge_pos].value)

        self.mark_as_unvisited()
        __deep_sweep(self, value)
        
    # Realiza un recorrido en amplitud (BFS - Breadth-First Search) desde un vértice de inicio.
    def amplitude_sweep(self, value)-> None:
        """
        Realiza un recorrido en amplitud (BFS) desde un vértice de inicio.

        Args:
            value (Any): El valor del vértice desde el cual comenzar el recorrido.
        """
        queue_vertex = Queue()
        self.mark_as_unvisited()
        vertex_pos = self.search(value, 'value')
        if vertex_pos is not None:
            if not self[vertex_pos].visited:
                self[vertex_pos].visited = True
                queue_vertex.arrive(self[vertex_pos])
                # Mientras la cola no esté vacía, procesa los vértices.
                while queue_vertex.size() > 0:
                    vertex = queue_vertex.attention()
                    print(vertex.value)
                    for edge in vertex.edges:
                        destination_edge_pos = self.search(edge.value, 'value')
                        if destination_edge_pos is not None:
                            if not self[destination_edge_pos].visited:
                                self[destination_edge_pos].visited = True
                                queue_vertex.arrive(self[destination_edge_pos])

    # Implementación del algoritmo de Dijkstra para encontrar el camino más corto desde un vértice de origen a todos los demás.
    def dijkstra(self, origin):
        """
        Implementa el algoritmo de Dijkstra para encontrar el camino más corto desde un origen a todos los demás vértices.

        Args:
            origin (Any): El valor del vértice de origen.

        Returns:
            Stack: Una pila con la información del camino (vértice, costo, predecesor).
        """
        from math import inf
        no_visited = HeapMin() # Cola de prioridad para almacenar los vértices no visitados.
        path = Stack() # Pila para reconstruir el camino.

        # Inicializa todos los vértices con una distancia infinita, excepto el origen (distancia 0).
        for vertex in self:
            distance = 0 if vertex.value == origin else inf
            no_visited.arrive([vertex.value, vertex, None], distance)
        
        # Mientras haya vértices no visitados.
        while no_visited.size() > 0:
            value = no_visited.attention() # Obtiene el vértice con la menor distancia.
            costo_nodo_actual = value[0]
            path.push([value[1][0], costo_nodo_actual, value[1][2]])
            edges = value[1][1].edges

            # Recorre las aristas del vértice actual.
            for edge in edges:
                pos = no_visited.search(edge.value)
                # Si el destino de la arista está en la cola de no visitados.
                if pos is not None:
                    # Si se encuentra un camino más corto, se actualiza la distancia.
                    if costo_nodo_actual + edge.weight < no_visited.elements[pos][0]:
                        no_visited.elements[pos][1][2] = value[1][0] # Actualiza el predecesor.
                        no_visited.change_priority(pos, costo_nodo_actual + edge.weight) # Actualiza la prioridad (distancia).
        return path

    # Implementación del algoritmo de Kruskal para encontrar el Árbol de Expansión Mínima (MST).
    def kruskal(self, origin_vertex):
        """
        Implementa el algoritmo de Kruskal para encontrar el Árbol de Expansión Mínima (MST).

        Args:
            origin_vertex (Any): Un vértice de referencia para determinar a qué árbol del bosque pertenece el resultado.

        Returns:
            list or str: Una representación del árbol de expansión mínima.
        """
        # Función auxiliar para encontrar a qué conjunto (árbol) pertenece un vértice en el bosque.
        def search_in_forest(forest, value):
            for index, tree in enumerate(forest):
                if value in tree:
                    return index
                
        forest = [] # Bosque de árboles, inicialmente cada vértice es un árbol.
        edges = HeapMin() # Cola de prioridad para almacenar todas las aristas ordenadas por peso.
        for vertex in self:
            forest.append(vertex.value)
            for edge in vertex.edges:
                edges.arrive([vertex.value, edge.value], edge.weight)
        
        while len(forest) > 1 and edges.size() > 0:
            edge = edges.attention()
            # Busca los árboles a los que pertenecen el origen y el destino de la arista.
            origin = search_in_forest(forest, edge[1][0])
            destination = search_in_forest(forest, edge[1][1])

            if origin is not None and destination is not None:
                # Si no pertenecen al mismo árbol, se unen para no formar un ciclo.
                if origin != destination:
                    if origin > destination:
                        vertex_origin = forest.pop(origin)
                        vertex_destination = forest.pop(destination)
                    else:
                        vertex_destination = forest.pop(destination)
                        vertex_origin = forest.pop(origin)

                    if '-' not in vertex_origin and '-' not in vertex_destination:
                        forest.append(f'{vertex_origin}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_destination:
                        forest.append(vertex_origin+';'+f'{edge[1][0]}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_origin:
                        forest.append(vertex_destination+';'+f'{vertex_origin}-{edge[1][1]}-{edge[0]}')
                    else:
                        forest.append(vertex_origin+';'+vertex_destination+';'+f'{edge[1][0]}-{edge[1][1]}-{edge[0]}')
        
        from_vertex = search_in_forest(forest, origin_vertex)
        
        return forest[from_vertex] if from_vertex is not None else forest

    def reconstruct_path(self, dijkstra_result: Stack, destination: str):
        """
        Reconstruye el camino más corto desde el resultado de Dijkstra a un destino específico.

        Args:
            dijkstra_result (Stack): La pila devuelta por el método dijkstra.
            destination (str): El nombre del vértice de destino.

        Returns:
            tuple[Stack, int]: Una tupla conteniendo una pila con el camino y el costo total.
        """
        path = Stack()
        cost = -1

        # 1. Convertir la pila de resultados a un diccionario para acceso rápido
        path_data = {}
        while dijkstra_result.size() > 0:
            item = dijkstra_result.pop()
            path_data[item[0]] = item  # Clave: nombre del vértice

        # 2. Reconstruir el camino hacia atrás desde el destino
        if destination in path_data:
            cost = path_data[destination][1]
            current_name = destination
            while current_name is not None:
                path.push(current_name)
                current_name = path_data[current_name][2] # Moverse al predecesor
        
        return path, cost
