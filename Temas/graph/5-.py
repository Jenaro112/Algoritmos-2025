"""
* Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos necesarios para resolver las tareas, listadas a continuación:
*   a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora.
*   b. realizar un barrido en profundidad y amplitud partiendo desde las tres notebooks: Red Hat, Debian, Arch.
*   c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro, Red Hat, Fedora hasta la impresora.
*   d. encontrar el árbol de expansión mínima para toda la red.
*   e. determinar desde qué pc (no notebook) es el camino más corto hasta el servidor “Guaraní”.
*   f. indicar desde qué computadora conectada al switch 01 es el camino más corto al servidor “MongoDB”.
*   g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto c.
*   h. debe utilizar un grafo no dirigido.
"""

from graph import Graph
from stack import Stack

def get_path(path_info_original: Stack, destination: str):
    """
    Reconstruye el camino y calcula el costo desde la pila devuelta por Dijkstra.
    """
    path_stack = Stack()
    # Clonar la pila original para no destruirla
    aux_stack = Stack()
    while path_info_original.size() > 0:
        item = path_info_original.pop()
        aux_stack.push(item)
    while aux_stack.size() > 0:
        item = aux_stack.pop()
        path_info_original.push(item)
        path_stack.push(item)

    path = Stack()
    cost = -1
    
    # Buscar el destino en la pila de resultados
    current_data = None
    while path_stack.size() > 0:
        data = path_stack.pop()
        if data[0] == destination:
            current_data = data
            break
    
    if current_data:
        cost = current_data[1]
        # Reconstruir el camino hacia atrás usando los predecesores
        while current_data is not None:
            path.push(current_data[0])
            predecessor_name = current_data[2]
            if predecessor_name is None:
                break
            
            # Buscar el nodo predecesor en la pila original para continuar
            found_predecessor = None
            temp_stack = Stack()
            while path_info_original.size() > 0:
                search_data = path_info_original.pop()
                temp_stack.push(search_data)
                if search_data[0] == predecessor_name:
                    found_predecessor = search_data
            
            # Restaurar la pila original
            while temp_stack.size() > 0:
                path_info_original.push(temp_stack.pop())
            
            current_data = found_predecessor

    return path, cost

def PuntoA():
    """Punto a. Crea y carga el grafo de la red con todos los dispositivos y conexiones."""
    g = Graph()
    devices = [
        ('Switch 1', 'switch'), ('Debian', 'notebook'), ('Ubuntu', 'pc'), 
        ('Impresora', 'impresora'), ('Mint', 'pc'), ('Router 1', 'router'),
        ('Switch 2', 'switch'), ('Manjaro', 'pc'), ('Parrot', 'pc'), 
        ('Fedora', 'pc'), ('Arch', 'notebook'), ('MongoDB', 'servidor'), 
        ('Router 3', 'router'), ('Router 2', 'router'), ('Red Hat', 'notebook'), 
        ('Guarani', 'servidor')
    ]
    for name, type in devices:
        g.insert_vertex(name)
        vertex_pos = g.search(name, 'value')
        if vertex_pos is not None:
            g[vertex_pos].other_values = {'type': type}

    edges = [
        ('Switch 1', 'Debian', 17), ('Switch 1', 'Ubuntu', 18), ('Switch 1', 'Impresora', 22),
        ('Switch 1', 'Mint', 80), ('Switch 1', 'Router 1', 29),
        ('Switch 2', 'Manjaro', 40), ('Switch 2', 'Parrot', 12), ('Switch 2', 'Fedora', 3),
        ('Switch 2', 'Arch', 56), ('Switch 2', 'MongoDB', 5), ('Switch 2', 'Router 3', 61),
        ('Router 1', 'Router 2', 37), ('Router 1', 'Router 3', 43),
        ('Router 2', 'Red Hat', 25), ('Router 2', 'Guarani', 9), ('Router 2', 'Router 3', 50)
    ]
    for origin, dest, weight in edges:
        g.insert_edge(origin, dest, weight)
    
    print("Grafo de red cargado.")
    return g

def PuntoB(g, notebooks):
    """Punto b. Realiza barridos en profundidad y amplitud desde las notebooks."""
    print("-" * 30)
    for notebook in notebooks:
        print(f"\n--- Barrido en Profundidad (DFS) desde: {notebook} ---")
        g.deep_sweep(notebook)
        print(f"\n--- Barrido en Amplitud (BFS) desde: {notebook} ---")
        g.amplitude_sweep(notebook)

def PuntoC(g, pcs, destination):
    """Punto c. Encuentra y muestra el camino más corto desde varias PCs a un destino."""
    print("-" * 30)
    print(f"\n--- c. Camino más corto a la {destination} ---")
    for pc in pcs:
        path_info = g.dijkstra(pc)
        path, cost = get_path(path_info, destination)
        print(f"Desde '{pc}':")
        if cost != -1:
            print(f"  Costo total: {cost}")
            path_str = ""
            while path.size() > 0:
                path_str += path.pop() + " -> "
            print(f"  Camino: {path_str.strip(' -> ')}")
        else:
            print(f"  No se encontró un camino a la {destination}.")

def PuntoD(g):
    """Punto d. Encuentra y muestra el Árbol de Expansión Mínima."""
    print("-" * 30)
    print("\n--- d. Árbol de Expansión Mínima (Kruskal) ---")
    mst_str = g.kruskal('Switch 1')
    total_weight = 0
    print("Aristas del MST:")
    for edge in mst_str.split(';'):
        parts = edge.split('-')
        if len(parts) == 3:
            origin, dest, weight = parts
            total_weight += int(weight)
            print(f"  {origin} -- {dest} (Peso: {weight})")
    print(f"Peso total del Árbol de Expansión Mínima: {total_weight}")

def PuntoE(g):
    """Punto e. Determina qué PC (no notebook) tiene el camino más corto al servidor 'Guaraní'."""
    print("-" * 30)
    print("\n--- e. PC con camino más corto a 'Guaraní' ---")
    shortest_path_pc = {'pc': None, 'cost': float('inf')}
    for i in range(len(g)):
        vertex = g[i]
        if vertex.other_values and vertex.other_values.get('type') == 'pc':
            path_info = g.dijkstra(vertex.value)
            _, cost = get_path(path_info, 'Guarani')
            if cost != -1 and cost < shortest_path_pc['cost']:
                shortest_path_pc['pc'] = vertex.value
                shortest_path_pc['cost'] = cost

    if shortest_path_pc['pc']:
        print(f"La PC con el camino más corto a 'Guarani' es '{shortest_path_pc['pc']}' con un costo de {shortest_path_pc['cost']}.")
    else:
        print("No se pudo encontrar un camino desde ninguna PC a 'Guarani'.")

def PuntoF(g):
    """Punto f. Indica qué computadora del Switch 1 tiene el camino más corto a 'MongoDB'."""
    print("-" * 30)
    print("\n--- f. Computadora en Switch 1 con camino más corto a 'MongoDB' ---")
    computers_on_switch1 = ['Debian', 'Ubuntu', 'Mint']
    shortest_path_sw1 = {'device': None, 'cost': float('inf')}
    for device in computers_on_switch1:
        path_info = g.dijkstra(device)
        _, cost = get_path(path_info, 'MongoDB')
        if cost != -1 and cost < shortest_path_sw1['cost']:
            shortest_path_sw1['device'] = device
            shortest_path_sw1['cost'] = cost

    if shortest_path_sw1['device']:
        print(f"El dispositivo en Switch 1 con el camino más corto a 'MongoDB' es '{shortest_path_sw1['device']}' con un costo de {shortest_path_sw1['cost']}.")

def PuntoG(g, pcs_to_print):
    """Punto g. Cambia la conexión de la impresora y recalcula los caminos más cortos."""
    print("-" * 30)
    print("\n--- g. Recalcular camino a la impresora tras cambio de conexión ---")
    g.delete_edge('Switch 1', 'Impresora', 'value')
    g.insert_edge('Router 2', 'Impresora', 20)
    print("Conexión de la impresora cambiada a Router 2.")
    PuntoC(g, pcs_to_print, 'Impresora')

def main():
    """Función principal que orquesta la resolución del problema."""
    # a.
    network_graph = PuntoA()

    # b.
    notebooks_to_scan = ['Red Hat', 'Debian', 'Arch']
    PuntoB(network_graph, notebooks_to_scan)

    # c.
    pcs_to_print = ['Manjaro', 'Red Hat', 'Fedora']
    PuntoC(network_graph, pcs_to_print, 'Impresora')

    # d.
    PuntoD(network_graph)

    # e.
    PuntoE(network_graph)

    # f.
    PuntoF(network_graph)

    # g.
    PuntoG(network_graph, pcs_to_print)
    
    print("-" * 30)

if __name__ == "__main__":
    main()
