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

# --- DEFINICIÓN DE FUNCIONES PARA CADA PUNTO DEL EJERCICIO ---

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
    # 1. Se itera sobre la lista de dispositivos para insertarlos como vértices en el grafo.
    for name, type in devices:
        g.insert_vertex(name)
        # Se busca la posición del vértice recién insertado.
        vertex_pos = g.search(name, 'value')
        # Si se encuentra, se almacena su tipo ('pc', 'router', etc.) en el campo 'other_values'.
        if vertex_pos is not None:
            g[vertex_pos].other_values = {'type': type}

    # 2. Se define una lista de aristas (conexiones) con su origen, destino y peso (distancia).
    edges = [
        ('Switch 1', 'Debian', 17), ('Switch 1', 'Ubuntu', 18), ('Switch 1', 'Impresora', 22),
        ('Switch 1', 'Mint', 80), ('Switch 1', 'Router 1', 29),
        ('Switch 2', 'Manjaro', 40), ('Switch 2', 'Parrot', 12), ('Switch 2', 'Fedora', 3),
        ('Switch 2', 'Arch', 56), ('Switch 2', 'MongoDB', 5), ('Switch 2', 'Router 3', 61),
        ('Router 1', 'Router 2', 37), ('Router 1', 'Router 3', 43),
        ('Router 2', 'Red Hat', 25), ('Router 2', 'Guarani', 9), ('Router 2', 'Router 3', 50)
    ]
    # 3. Se itera sobre la lista de conexiones para insertarlas como aristas en el grafo.
    for origin, dest, weight in edges:
        g.insert_edge(origin, dest, weight)
    
    imprimir_mensaje("Grafo de red cargado exitosamente.", "exito")
    # 4. Se devuelve el grafo ya cargado.
    return g

def PuntoB(g, notebooks):
    """Punto b. Realiza barridos en profundidad y amplitud desde las notebooks."""
    # Se itera sobre la lista de notebooks especificadas.
    for notebook in notebooks:
        imprimir_mensaje(f"Barrido en Profundidad (DFS) desde: {notebook}", "info")
        g.deep_sweep(notebook)
        imprimir_mensaje(f"Barrido en Amplitud (BFS) desde: {notebook}", "info")
        g.amplitude_sweep(notebook)

def PuntoC(g, pcs, destination):
    """Punto c. Encuentra y muestra el camino más corto desde varias PCs a un destino."""
    # Se itera sobre la lista de PCs desde las que se quiere calcular el camino.
    for pc in pcs:
        # Se ejecuta el algoritmo de Dijkstra desde la PC actual.
        # Dijkstra devuelve una pila con la información de los caminos más cortos a todos los demás nodos.
        path_info = g.dijkstra(pc)
        
        # Para facilitar la búsqueda, convertimos la pila de resultados de Dijkstra a un diccionario.
        # La clave será el nombre del vértice y el valor será una tupla (costo, predecesor).
        path_dict = {}
        while path_info.size() > 0:
            data = path_info.pop()
            path_dict[data[0]] = (data[1], data[2]) # {vertice: (costo, predecesor)}

        cost = -1
        # Usamos una pila para reconstruir el camino desde el destino hasta el origen.
        path = Stack()
        # Si el destino está en nuestro diccionario de caminos...
        if destination in path_dict:
            # ...obtenemos el costo total.
            cost = path_dict[destination][0]
            current_vertex = destination
            # Y reconstruimos el camino hacia atrás usando los predecesores.
            while current_vertex is not None:
                path.push(current_vertex)
                current_vertex = path_dict[current_vertex][1]

        print(f"Desde '{pc}':")
        if cost != -1:
            print(f"  Costo total: {cost}")
            # Vaciamos la pila para mostrar el camino en el orden correcto (origen -> destino).
            path_str = ""
            while path.size() > 0:
                path_str += path.pop() + " -> "
            print(f"  Camino: {path_str.strip(' -> ')}")
        else:
            print(f"  No se encontró un camino a la {destination}.")

def PuntoD(g):
    """Punto d. Encuentra y muestra el Árbol de Expansión Mínima."""
    # Se ejecuta el algoritmo de Kruskal para obtener el Árbol de Expansión Mínima (MST).
    # Kruskal devuelve una cadena de texto con las aristas del MST.
    mst_str = g.kruskal('Switch 1')
    total_weight = 0
    print("Aristas del MST:")
    # Se procesa la cadena para calcular el peso total y mostrar las aristas.
    for edge in mst_str.split(';'):
        parts = edge.split('-')
        if len(parts) == 3:
            origin, dest, weight = parts
            total_weight += int(weight)
            print(f"  {origin} -- {dest} (Peso: {weight})")
    print(f"Peso total del Árbol de Expansión Mínima: {total_weight}")

def PuntoE(g):
    """Punto e. Determina qué PC (no notebook) tiene el camino más corto al servidor 'Guaraní'."""
    # Se inicializa un diccionario para guardar la PC con el camino más corto encontrado hasta ahora.
    shortest_path_pc = {'pc': None, 'cost': float('inf')}
    # Se recorren todos los vértices del grafo.
    for i in range(len(g)):
        vertex = g[i]
        # Si el vértice es de tipo 'pc'...
        if vertex.other_values and vertex.other_values.get('type') == 'pc':
            # ...se calcula el camino más corto desde esa PC a todos los demás nodos.
            path_info = g.dijkstra(vertex.value)
            
            # Se convierte la pila de resultados a un diccionario para fácil acceso.
            path_dict = {}
            while path_info.size() > 0:
                data = path_info.pop()
                path_dict[data[0]] = (data[1], data[2])

            # Se obtiene el costo para llegar al servidor 'Guarani'.
            cost = -1
            if 'Guarani' in path_dict:
                cost = path_dict['Guarani'][0]

            # Si el costo encontrado es menor que el mínimo guardado, se actualiza.
            if cost != -1 and cost < shortest_path_pc['cost']:
                shortest_path_pc['pc'] = vertex.value
                shortest_path_pc['cost'] = cost

    if shortest_path_pc['pc']:
        print(f"La PC con el camino más corto a 'Guarani' es '{shortest_path_pc['pc']}' con un costo de {shortest_path_pc['cost']}.")
    else:
        print("No se pudo encontrar un camino desde ninguna PC a 'Guarani'.")

def PuntoF(g):
    """Punto f. Indica qué computadora del Switch 1 tiene el camino más corto a 'MongoDB'."""
    # Se define una lista de los dispositivos de interés conectados al Switch 1.
    computers_on_switch1 = ['Debian', 'Ubuntu', 'Mint']
    # Se inicializa un diccionario para guardar el dispositivo con el camino más corto.
    shortest_path_sw1 = {'device': None, 'cost': float('inf')}
    # Se itera sobre cada dispositivo.
    for device in computers_on_switch1:
        # Se calcula el camino más corto desde ese dispositivo a todos los demás.
        path_info = g.dijkstra(device)

        # Se convierte la pila de resultados a un diccionario.
        path_dict = {}
        while path_info.size() > 0:
            data = path_info.pop()
            path_dict[data[0]] = (data[1], data[2])

        # Se obtiene el costo para llegar a 'MongoDB'.
        cost = -1
        if 'MongoDB' in path_dict:
            cost = path_dict['MongoDB'][0]

        # Si el costo es menor que el mínimo actual, se actualiza.
        if cost != -1 and cost < shortest_path_sw1['cost']:
            shortest_path_sw1['device'] = device
            shortest_path_sw1['cost'] = cost

    if shortest_path_sw1['device']:
        print(f"El dispositivo en Switch 1 con el camino más corto a 'MongoDB' es '{shortest_path_sw1['device']}' con un costo de {shortest_path_sw1['cost']}.")

def PuntoG(g, pcs_to_print):
    """Punto g. Cambia la conexión de la impresora y recalcula los caminos más cortos."""
    # 1. Se elimina la arista original que conecta 'Switch 1' con 'Impresora'.
    g.delete_edge('Switch 1', 'Impresora', 'value')
    # 2. Se inserta una nueva arista que conecta 'Router 2' con 'Impresora'.
    g.insert_edge('Router 2', 'Impresora', 20)
    imprimir_mensaje("Conexión de la impresora cambiada a Router 2.", "alerta")
    # 3. Se vuelve a ejecutar la función del Punto C para recalcular los caminos con el grafo modificado.
    PuntoC(g, pcs_to_print, 'Impresora')

def main():
    """Función principal que orquesta la resolución del problema."""
    imprimir_titulo("Análisis de Red - Ejercicio 5")

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

# --- PUNTO DE ENTRADA DEL SCRIPT ---
# Este bloque de código se ejecuta solo si este archivo es el programa principal.
if __name__ == "__main__":
    main()
