"""
* Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos necesarios para resolver las tareas, listadas a continuación:
*   a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora; (HECHO en la carga)
*   b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red Hat, Debian, Arch; (HECHO)
*   c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro, Red Hat, Fedora hasta la impresora; (HECHO)
*   d. encontrar el árbol de expansión mínima; (HECHO)
*   e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”; (HECHO)
*   f. indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”; (HECHO)
*   g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b; (HECHO)
*   h. debe utilizar un grafo no dirigido. (HECHO)
"""
from graph import Graph
from math import inf

def obtener_camino(pila_dijkstra, destino_buscado):
    """Reconstruye el camino más corto desde la pila de resultados de Dijkstra."""
    camino = []
    costo_total = None
    destino_actual = destino_buscado
    
    while pila_dijkstra.size() > 0:
        valor = pila_dijkstra.pop()
        if valor[0] == destino_actual:
            if costo_total is None:
                costo_total = valor[1]
            camino.append(valor[0])
            destino_actual = valor[2]
    
    camino.reverse()
    return camino, costo_total

def PuntoA():
    g = Graph(is_directed=False)

    # a. Almacenar nombre y tipo de equipo
    g.insert_vertex("Switch 1", other_values={"type": "switch"})
    g.insert_vertex("Ubuntu", other_values={"type": "pc"})
    g.insert_vertex("Debian", other_values={"type": "notebook"})
    g.insert_vertex("Impresora", other_values={"type": "impresora"})
    g.insert_vertex("Mint", other_values={"type": "pc"})
    g.insert_vertex("Router 1", other_values={"type": "router"})
    g.insert_vertex("Switch 2", other_values={"type": "switch"})
    g.insert_vertex("Manjaro", other_values={"type": "pc"})
    g.insert_vertex("Parrot", other_values={"type": "pc"})
    g.insert_vertex("Fedora", other_values={"type": "pc"})
    g.insert_vertex("Arch", other_values={"type": "notebook"})
    g.insert_vertex("MongoDB", other_values={"type": "servidor"})
    g.insert_vertex("Router 3", other_values={"type": "router"})
    g.insert_vertex("Router 2", other_values={"type": "router"})
    g.insert_vertex("Red Hat", other_values={"type": "notebook"})
    g.insert_vertex("Guaraní", other_values={"type": "servidor"})

    g.insert_edge("Switch 1", "Ubuntu", 18)
    g.insert_edge("Switch 1", "Debian", 17)
    g.insert_edge("Switch 1", "Impresora", 22)
    g.insert_edge("Switch 1", "Mint", 80)
    g.insert_edge("Switch 1", "Router 1", 29)
    g.insert_edge("Switch 2", "Manjaro", 40)
    g.insert_edge("Switch 2", "Parrot", 12)
    g.insert_edge("Switch 2", "Fedora", 3)
    g.insert_edge("Switch 2", "Arch", 56)
    g.insert_edge("Switch 2", "MongoDB", 5)
    g.insert_edge("Switch 2", "Router 3", 61)
    g.insert_edge("Router 2", "Red Hat", 25)
    g.insert_edge("Router 2", "Guaraní", 9)
    g.insert_edge("Router 1", "Router 2", 37)
    g.insert_edge("Router 1", "Router 3", 43)
    g.insert_edge("Router 2", "Router 3", 50)
    
    return g

def PuntoB(g):
    notebooks = ["Red Hat", "Debian", "Arch"]
    for pc in notebooks:
        print(f"\n>> Barridos desde: {pc}")
        print("  -> Barrido en Profundidad (DFS):")
        g.deep_sweep(pc)
        print("\n  -> Barrido en Amplitud (BFS):")
        g.amplitude_sweep(pc)

def PuntoC(g):
    pcs = ["Manjaro", "Red Hat", "Fedora"]
    for pc in pcs:
        pila_path = g.dijkstra(pc)
        camino, costo = obtener_camino(pila_path, "Impresora")
        if costo is not None:
            print(f"  -> Desde '{pc}': {' -> '.join(camino)} (Costo: {costo})")
        else:
            print(f"  -> No se encontró camino desde '{pc}' a la Impresora.")

def PuntoD(g):
    mst = g.kruskal("Router 1")
    if isinstance(mst, str):
        costo_total = 0
        print("  Aristas del Árbol de Expansión Mínima:")
        for arista in mst.split(';'):
            origen, destino, peso_str = arista.split('-')
            peso = int(peso_str)
            costo_total += peso
            print(f"    - {origen} <-> {destino} (Peso: {peso})")
        print(f"  Costo total del árbol: {costo_total}")
    else:
        print("  No se pudo generar el árbol de expansión mínima o el grafo no es conexo.")

def PuntoE(g):
    pcs = []
    for i in range(len(g)):
        nodo = g[i]
        if nodo.other_values["type"] == "pc":
            pcs.append(nodo.value)

    mejor_pc = None
    menor_costo = inf

    for pc in pcs:
        pila_path = g.dijkstra(pc)
        _, costo = obtener_camino(pila_path, "Guaraní")
        if costo is not None and costo < menor_costo:
            menor_costo = costo
            mejor_pc = pc
    
    if mejor_pc:
        print(f"  La PC con el camino más corto a 'Guaraní' es '{mejor_pc}' con un costo de {menor_costo}.")
    else:
        print("  No se pudo determinar el camino más corto desde ninguna PC.")

def PuntoF(g):
    pos_switch1 = g.search("Switch 1", "value")
    if pos_switch1 is None:
        print("  Error: No se encontró el 'Switch 1'.")
        return

    computadoras_conectadas = []
    for arista in g[pos_switch1].edges:
        pos_nodo = g.search(arista.value, "value")
        tipo_nodo = g[pos_nodo].other_values["type"]
        if tipo_nodo in ["pc", "notebook"]:
            computadoras_conectadas.append(arista.value)

    mejor_compu = None
    menor_costo = inf

    for compu in computadoras_conectadas:
        pila_path = g.dijkstra(compu)
        _, costo = obtener_camino(pila_path, "MongoDB")
        if costo is not None and costo < menor_costo:
            menor_costo = costo
            mejor_compu = compu

    if mejor_compu:
        print(f"  La computadora conectada a Switch 1 con el camino más corto a 'MongoDB' es '{mejor_compu}' (Costo: {menor_costo}).")
    else:
        print("  No se pudo determinar el camino más corto desde ninguna computadora en Switch 1.")

def PuntoG(g):
    g.delete_edge("Impresora", "Switch 1", "value")
    g.insert_edge("Impresora", "Router 2", 10)
    print("  Conexión de la Impresora movida de 'Switch 1' a 'Router 2'.")
    
    PuntoB(g)

if __name__ == "__main__":
    print("-" * 40)
    print("Punto A")
    grafo_red = PuntoA()
    print("Grafo de red cargado.")
    print("-" * 40)
    print("Punto B")
    PuntoB(grafo_red)
    print("-" * 40)
    print("Punto C")
    PuntoC(grafo_red)
    print("-" * 40)
    print("Punto D")
    PuntoD(grafo_red)
    print("-" * 40)
    print("Punto E")
    PuntoE(grafo_red)
    print("-" * 40)
    print("Punto F")
    PuntoF(grafo_red)
    print("-" * 40)
    
    grafo_para_g = PuntoA()
    print("Punto G")
    PuntoG(grafo_para_g)
    print("-" * 40)
