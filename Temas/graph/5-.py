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
from MiLibreria import imprimir_titulo, imprimir_subtitulo, imprimir_mensaje

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
    
    imprimir_mensaje("Grafo de red cargado exitosamente.", "exito")
    return g

def PuntoB(g, notebooks):
    """Punto b. Realiza barridos en profundidad y amplitud desde las notebooks."""
    for notebook in notebooks:
        imprimir_mensaje(f"Barrido en Profundidad (DFS) desde: {notebook}", "info")
        g.deep_sweep(notebook)
        imprimir_mensaje(f"Barrido en Amplitud (BFS) desde: {notebook}", "info")
        g.amplitude_sweep(notebook)

def PuntoC(g, pcs, destination):
    """Punto c. Encuentra y muestra el camino más corto desde varias PCs a un destino."""
    for pc in pcs:
        path_info = g.dijkstra(pc)
        
        # Convertir la pila de resultados de Dijkstra a un diccionario para fácil acceso
        path_dict = {}
        while path_info.size() > 0:
            data = path_info.pop()
            path_dict[data[0]] = (data[1], data[2]) # {vertice: (costo, predecesor)}

        cost = -1
        path = Stack()
        if destination in path_dict:
            cost = path_dict[destination][0]
            current_vertex = destination
            while current_vertex is not None:
                path.push(current_vertex)
                current_vertex = path_dict[current_vertex][1]

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
    shortest_path_pc = {'pc': None, 'cost': float('inf')}
    for i in range(len(g)):
        vertex = g[i]
        if vertex.other_values and vertex.other_values.get('type') == 'pc':
            path_info = g.dijkstra(vertex.value)
            
            # Convertir la pila de resultados a un diccionario
            path_dict = {}
            while path_info.size() > 0:
                data = path_info.pop()
                path_dict[data[0]] = (data[1], data[2])

            cost = -1
            if 'Guarani' in path_dict:
                cost = path_dict['Guarani'][0]

            if cost != -1 and cost < shortest_path_pc['cost']:
                shortest_path_pc['pc'] = vertex.value
                shortest_path_pc['cost'] = cost

    if shortest_path_pc['pc']:
        print(f"La PC con el camino más corto a 'Guarani' es '{shortest_path_pc['pc']}' con un costo de {shortest_path_pc['cost']}.")
    else:
        print("No se pudo encontrar un camino desde ninguna PC a 'Guarani'.")

def PuntoF(g):
    """Punto f. Indica qué computadora del Switch 1 tiene el camino más corto a 'MongoDB'."""
    computers_on_switch1 = ['Debian', 'Ubuntu', 'Mint']
    shortest_path_sw1 = {'device': None, 'cost': float('inf')}
    for device in computers_on_switch1:
        path_info = g.dijkstra(device)

        # Convertir la pila de resultados a un diccionario
        path_dict = {}
        while path_info.size() > 0:
            data = path_info.pop()
            path_dict[data[0]] = (data[1], data[2])

        cost = -1
        if 'MongoDB' in path_dict:
            cost = path_dict['MongoDB'][0]

        if cost != -1 and cost < shortest_path_sw1['cost']:
            shortest_path_sw1['device'] = device
            shortest_path_sw1['cost'] = cost

    if shortest_path_sw1['device']:
        print(f"El dispositivo en Switch 1 con el camino más corto a 'MongoDB' es '{shortest_path_sw1['device']}' con un costo de {shortest_path_sw1['cost']}.")

def PuntoG(g, pcs_to_print):
    """Punto g. Cambia la conexión de la impresora y recalcula los caminos más cortos."""
    g.delete_edge('Switch 1', 'Impresora', 'value')
    g.insert_edge('Router 2', 'Impresora', 20)
    imprimir_mensaje("Conexión de la impresora cambiada a Router 2.", "alerta")
    PuntoC(g, pcs_to_print, 'Impresora')

def main():
    """Función principal que orquesta la resolución del problema."""
    imprimir_titulo("Ejercicio 5")

    # a.
    imprimir_subtitulo("Punto A: Carga del Grafo de Red")
    network_graph = PuntoA()

    # b.
    imprimir_subtitulo("Punto B: Barridos de Red (DFS y BFS)")
    notebooks_to_scan = ['Red Hat', 'Debian', 'Arch']
    PuntoB(network_graph, notebooks_to_scan)

    # c.
    imprimir_subtitulo("Punto C: Camino más corto a la Impresora")
    pcs_to_print = ['Manjaro', 'Red Hat', 'Fedora']
    PuntoC(network_graph, pcs_to_print, 'Impresora')

    # d.
    imprimir_subtitulo("Punto D: Árbol de Expansión Mínima")
    PuntoD(network_graph)

    # e.
    imprimir_subtitulo("Punto E: PC con camino más corto a 'Guaraní'")
    PuntoE(network_graph)

    # f.
    imprimir_subtitulo("Punto F: Dispositivo en Switch 1 con camino más corto a 'MongoDB'")
    PuntoF(network_graph)

    # g.
    imprimir_subtitulo("Punto G: Recalcular camino a la impresora tras cambio")
    PuntoG(network_graph, pcs_to_print)

if __name__ == "__main__":
    main()
