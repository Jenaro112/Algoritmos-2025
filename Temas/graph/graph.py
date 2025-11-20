from typing import Any, Optional

# Importaciones de estructuras de datos auxiliares desde otros archivos del proyecto.
from heap import HeapMin
from list_ import List
from queue_ import Queue
from stack import Stack

# La clase Graph hereda de List, lo que significa que un grafo es, en esencia, una lista de vértices.
class Graph(List):
    """
    Representa una estructura de datos de tipo Grafo.
    Un grafo es una colección de vértices (nodos) y aristas (conexiones entre nodos).
    Esta implementación permite grafos dirigidos y no dirigidos.
    """

    class __nodeVertex:
        """
        Clase interna que representa un Vértice (o nodo) en el grafo.
        """

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            """
            Inicializa un nuevo vértice.
            """
            self.value = value
            # Cada vértice tiene su propia lista de aristas para representar las conexiones.
            self.edges = List()
            # Se definen criterios de ordenación para la lista de aristas.
            self.edges.add_criterion('value', Graph._order_by_value)
            self.edges.add_criterion('weight', Graph._order_by_weight)
            self.other_values = other_values
            # 'visited' es una bandera usada por los algoritmos de recorrido (BFS, DFS).
            self.visited = False
        
        def __str__(self):
            """Devuelve una representación en string del valor del vértice."""
            return str(self.value) #se agrego el str (string) para que muestre bien

    class __nodeEdge:
        """
        Clase interna que representa una Arista (o arco) en el grafo.
        Una arista conecta un vértice con otro y tiene un peso asociado.
        """

        def __init__(self, value: Any, weight: Any, other_values: Optional[Any] = None):
            """
            Inicializa una nueva arista.
            'value' aquí es el vértice de destino.
            """
            self.value = value
            self.weight = weight
            self.other_values = other_values
        
        def __str__(self):
            """Devuelve una representación en string de la arista."""
            return f'Destination: {self.value} with weight --> {self.weight}'
    
    def __init__(self, is_directed=False):
        """
        Inicializa un grafo.
        Args:
            is_directed (bool): Si es True, las aristas tienen una sola dirección.
                                Si es False, las aristas son bidireccionales.
        """
        # Se añade un criterio de ordenación para la lista de vértices (el propio grafo).
        self.add_criterion('value', self._order_by_value)
        self.is_directed = is_directed

    def _order_by_value(item):
        """Función de criterio para ordenar por el atributo 'value'."""
        return item.value

    def _order_by_weight(item):
        """Función de criterio para ordenar por el atributo 'weight'."""
        return item.weight
    
    def show(
        self
    ) -> None:
        """Muestra el grafo completo, listando cada vértice y sus conexiones."""
        for vertex in self:
            print(f"Vertex: {vertex}")
            vertex.edges.show() 

    def insert_vertex(
        self,
        value: Any,
        other_values: Optional[Any] = None) -> None: #añadido el other_values
        """
        Inserta un nuevo vértice en el grafo.
        """
        # Crea un nuevo nodo de vértice.
        node_vertex = Graph.__nodeVertex(value)
        # Lo agrega a la lista principal (el grafo).
        self.append(node_vertex)
        

    def insert_edge(self, origin_vertex: Any, destination_vertex: Any, weight: int) -> None:
        """
        Inserta una arista entre dos vértices con un peso determinado.
        """
        # Busca las posiciones de los vértices de origen y destino.
        origin = self.search(origin_vertex, 'value')
        destination = self.search(destination_vertex, 'value')
        
        # Si ambos vértices existen, crea la arista.
        if origin is not None and destination is not None:
            # Crea la arista hacia el destino.
            node_edge = Graph.__nodeEdge(destination_vertex, weight)
            # La agrega a la lista de aristas del vértice de origen.
            self[origin].edges.append(node_edge)
            
            # Si el grafo NO es dirigido, crea también la arista en sentido contrario.
            if not self.is_directed and origin != destination:
                node_edge = Graph.__nodeEdge(origin_vertex, weight)
                self[destination].edges.append(node_edge)
        else:
            print('no se puede insertar falta uno de los vertices')

    def delete_edge(
        self,
        origin,
        destination,
        key_value: str = None,
    ) -> Optional[Any]:
        """
        Elimina una arista entre un vértice de origen y uno de destino.
        """
        # Busca el vértice de origen.
        pos_origin = self.search(origin, key_value)
        if pos_origin is not None:
            # Elimina la arista de la lista de adyacencia del vértice de origen.
            edge = self[pos_origin].edges.delete_value(destination, key_value)
            
            # Si el grafo NO es dirigido, también elimina la arista en sentido contrario.
            if not self.is_directed and edge is not None:
                pos_destination = self.search(destination, key_value)
                if pos_destination is not None:
                    self[pos_destination].edges.delete_value(origin, key_value)
            return edge

    def delete_vertex(
        self,
        value,
        key_value_vertex: str = None,
        key_value_edges: str = 'value',
    ) -> Optional[Any]:
        """
        Elimina un vértice del grafo y todas las aristas conectadas a él.
        """
        # Primero, elimina el vértice de la lista principal del grafo.
        delete_value = self.delete_value(value, key_value_vertex)
        
        # Si se eliminó, ahora hay que limpiar las aristas que apuntaban a él.
        if delete_value is not None:
            for vertex in self:
                self.delete_edge(vertex.value, value, key_value_edges)
        return delete_value

    def mark_as_unvisited(self) -> None:
        """
        Pone la bandera 'visited' de todos los vértices en False.
        Es un paso necesario antes de iniciar un nuevo recorrido (DFS, BFS, etc.).
        """
        for vertex in self:
            vertex.visited = False

    def exist_path(self, origin, destination):
        """
        Determina si existe un camino entre un vértice de origen y uno de destino.

        Args:
            origin (Any): El valor del vértice de origen.
            destination (Any): El valor del vértice de destino.

        Returns:
            bool: True si existe un camino, False en caso contrario.
        """
        # Función interna recursiva que hace el trabajo sucio (DFS).
        def __exist_path(graph, origin, destination):
            result = False
            vertex_pos = graph.search(origin, 'value')
            if vertex_pos is not None:
                # Si no lo hemos visitado aún...
                if not graph[vertex_pos].visited:
                    # ...lo marcamos como visitado.
                    graph[vertex_pos].visited = True
                    # Si es el destino que buscamos, ¡éxito!
                    if graph[vertex_pos].value == destination:
                        return True
                    else:
                        # Si no, repetimos el proceso con todos sus vecinos.
                        for edge in graph[vertex_pos].edges:
                            destination_edge_pos = graph.search(edge.value, 'value')
                            if not graph[destination_edge_pos].visited:
                                result = __exist_path(graph, graph[destination_edge_pos].value, destination)
                                if result:
                                    break
            return result
        
        # Antes de empezar, nos aseguramos de que todos los nodos estén como "no visitados".
        self.mark_as_unvisited()
        result = __exist_path(self, origin, destination)
        return result
    
    def deep_sweep(self, value) -> None:
        """
        Realiza un recorrido en profundidad (DFS) desde un vértice de inicio.

        Args:
            value (Any): El valor del vértice desde el cual comenzar el recorrido.
        """
        # Función interna recursiva que implementa el DFS.
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

        # Preparamos el grafo para el recorrido.
        self.mark_as_unvisited()
        __deep_sweep(self, value)
        
    def amplitude_sweep(self, value)-> None:
        """
        Realiza un recorrido en amplitud (BFS) desde un vértice de inicio.

        Args:
            value (Any): El valor del vértice desde el cual comenzar el recorrido.
        """
        # Usamos una cola para llevar el orden de visita (primero en entrar, primero en salir).
        queue_vertex = Queue()
        self.mark_as_unvisited()
        vertex_pos = self.search(value, 'value')
        
        if vertex_pos is not None:
            if not self[vertex_pos].visited:
                self[vertex_pos].visited = True
                # Ponemos el primer vértice en la cola.
                queue_vertex.arrive(self[vertex_pos])
                
                # Mientras queden vértices por visitar en la cola...
                while queue_vertex.size() > 0:
                    # ...sacamos el primero de la cola.
                    vertex = queue_vertex.attention()
                    print(vertex.value)
                    # Y ponemos a todos sus vecinos no visitados en la cola.
                    for edge in vertex.edges:
                        destination_edge_pos = self.search(edge.value, 'value')
                        if destination_edge_pos is not None:
                            if not self[destination_edge_pos].visited:
                                self[destination_edge_pos].visited = True
                                queue_vertex.arrive(self[destination_edge_pos])

    def dijkstra(self, origin):
        """
        Implementa el algoritmo de Dijkstra para encontrar el camino más corto desde un origen a todos los demás vértices.

        Args:
            origin (Any): El valor del vértice de origen.

        Returns:
            Stack: Una pila con la información del camino (vértice, costo, predecesor).
        """
        from math import inf
        no_visited = HeapMin() # Usamos un Heap Mínimo como cola de prioridad.
        path = Stack() # Pila para almacenar el resultado final.

        # Inicializa todos los vértices con una distancia infinita, excepto el origen (distancia 0).
        for vertex in self:
            distance = 0 if vertex.value == origin else inf
            no_visited.arrive([vertex.value, vertex, None], distance)
        
        # Mientras queden vértices en la cola de prioridad...
        while no_visited.size() > 0:
            # ...sacamos el vértice con la menor distancia (el más cercano).
            value = no_visited.attention()
            costo_nodo_actual = value[0]
            path.push([value[1][0], costo_nodo_actual, value[1][2]])
            edges = value[1][1].edges

            # Ahora, revisamos todos sus vecinos.
            for edge in edges:
                pos = no_visited.search(edge.value)
                # Si el vecino aún no ha sido visitado permanentemente...
                if pos is not None:
                    # ...y encontramos un camino más corto hacia él...
                    if costo_nodo_actual + edge.weight < no_visited.elements[pos][0]:
                        no_visited.elements[pos][1][2] = value[1][0] # ...actualizamos su predecesor.
                        no_visited.change_priority(pos, costo_nodo_actual + edge.weight) # ...y actualizamos su distancia (prioridad en el heap).
        return path

    def kruskal(self, origin_vertex):
        """
        Implementa el algoritmo de Kruskal para encontrar el Árbol de Expansión Mínima (MST).

        Args:
            origin_vertex (Any): Un vértice de referencia para determinar a qué árbol del bosque pertenece el resultado.

        Returns:
            list or str: Una representación del árbol de expansión mínima.
        """
        # Función auxiliar para buscar a qué sub-árbol (conjunto) pertenece un vértice.
        def search_in_forest(forest, value):
            for index, tree in enumerate(forest):
                if value in tree:
                    return index
                
        forest = [] # El "bosque" donde cada vértice empieza siendo su propio árbol.
        edges = HeapMin() # Un Heap Mínimo para tener todas las aristas ordenadas por peso.
        
        # 1. Cada vértice se convierte en un árbol individual en el bosque.
        # 2. Todas las aristas del grafo se cargan en el heap.
        for vertex in self:
            forest.append(vertex.value)
            for edge in vertex.edges:
                edges.arrive([vertex.value, edge.value], edge.weight)
        
        # Mientras tengamos más de un árbol en el bosque...
        while len(forest) > 1 and edges.size() > 0:
            # ...sacamos la arista más barata (de menor peso).
            edge = edges.attention()
            # Verificamos a qué árbol pertenecen el origen y el destino de esa arista.
            origin = search_in_forest(forest, edge[1][0])
            destination = search_in_forest(forest, edge[1][1])

            if origin is not None and destination is not None:
                # Si están en árboles diferentes, significa que agregar esta arista no creará un ciclo.
                if origin != destination:
                    # Unimos los dos árboles en uno solo.
                    if origin > destination:
                        vertex_origin = forest.pop(origin)
                        vertex_destination = forest.pop(destination)
                    else:
                        vertex_destination = forest.pop(destination)
                        vertex_origin = forest.pop(origin)

                    # Se construye una cadena de texto para representar el árbol unido.
                    if '-' not in vertex_origin and '-' not in vertex_destination:
                        forest.append(f'{vertex_origin}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_destination:
                        forest.append(vertex_origin+';'+f'{edge[1][0]}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_origin:
                        forest.append(vertex_destination+';'+f'{vertex_origin}-{edge[1][1]}-{edge[0]}')
                    else:
                        forest.append(vertex_origin+';'+vertex_destination+';'+f'{edge[1][0]}-{edge[1][1]}-{edge[0]}')
        
        # Al final, devolvemos el árbol que contiene al vértice de origen que nos pasaron.
        from_vertex = search_in_forest(forest, origin_vertex)
        
        return forest[from_vertex] if from_vertex is not None else forest
