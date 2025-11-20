"""
*Implementar  sobre  un  grafo  no  dirigido  los  algoritmos  necesario  para  dar  solución  a  las  siguientes tareas:
*-   a. cada  vértice  representar  un  ambiente  de  una  casa:  cocina,  comedor,  cochera,  quincho, baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
*-  b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
*-  c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes;
*-  d. determinar  cuál  es  el  camino  más  corto  desde  la  habitación  1  hasta  la  sala  de  estar  para  determinar  cuántos  metros  de  cable  de  red  se  necesitan  para  conectar  el  router  con  el Smart Tv.
"""

from graph import Graph
from stack import Stack
from MiLibreria import imprimir_titulo, imprimir_subtitulo, imprimir_mensaje


def PuntoA_B():
    """
    Puntos a y b: Crea el grafo no dirigido representando la casa,
    carga los ambientes como vértices y las distancias como aristas.
    """
    g = Graph(is_directed=False)
    imprimir_subtitulo("Puntos A y B: Carga del Grafo de la Casa")

    ambientes = [
        'cocina', 'comedor', 'cochera', 'quincho', 'baño 1', 'baño 2',
        'habitación 1', 'habitación 2', 'sala de estar', 'terraza', 'patio'
    ]
    for ambiente in ambientes:
        g.insert_vertex(ambiente)

    # La 'cocina' y la 'sala de estar' tendrán 5 aristas.
    conexiones = [
        ('cocina', 'comedor', 4), ('cocina', 'baño 1', 2), ('cocina', 'patio', 5),
        ('cocina', 'sala de estar', 6), ('cocina', 'habitación 2', 7),
        ('comedor', 'sala de estar', 5), ('comedor', 'habitación 1', 6),
        ('cochera', 'patio', 4), ('cochera', 'quincho', 7), ('cochera', 'sala de estar', 8),
        ('quincho', 'patio', 3), ('quincho', 'baño 2', 2), ('quincho', 'terraza', 4),
        ('baño 1', 'habitación 1', 3), ('baño 1', 'sala de estar', 4),
        ('baño 2', 'terraza', 2), ('baño 2', 'habitación 2', 3),
        ('habitación 1', 'sala de estar', 3), ('habitación 1', 'terraza', 5),
        ('habitación 2', 'sala de estar', 4), ('habitación 2', 'terraza', 3),
        ('sala de estar', 'terraza', 2), ('sala de estar', 'patio', 5)
    ]

    for origen, destino, distancia in conexiones:
        g.insert_edge(origen, destino, distancia)
    
    imprimir_mensaje("Grafo de la casa cargado con ambientes y distancias.", "exito")
    return g

def PuntoC(g: Graph):
    """
    Punto c: Obtiene el árbol de expansión mínima y calcula los metros
    totales de cable necesarios.
    """
    imprimir_subtitulo("Punto C: Árbol de Expansión Mínima (Kruskal)")
    mst_str = g.kruskal('cocina')
    total_metros = 0
    print("   Conexiones del cableado:")
    for arista in mst_str.split(';'):
        partes = arista.split('-')
        if len(partes) == 3:
            origen, destino, peso = partes
            total_metros += int(peso)
            print(f"     - {origen} <-> {destino} ({peso}m)")
    print(f"\n   Se necesitan {total_metros} metros de cable para conectar todos los ambientes.")

def PuntoD(g: Graph):
    """
    Punto d: Determina el camino más corto desde la habitación 1
    hasta la sala de estar.
    """
    imprimir_subtitulo("Punto D: Camino más corto para cable de red")
    destination = 'sala de estar'
    path_info = g.dijkstra('habitación 1')

    # Convertir la pila de resultados de Dijkstra a un diccionario para fácil acceso
    path_dict = {}
    while path_info.size() > 0:
        data = path_info.pop()
        path_dict[data[0]] = (data[1], data[2]) # {vertice: (costo, predecesor)}

    metros = -1
    path = Stack()
    if destination in path_dict:
        metros = path_dict[destination][0]
        current_vertex = destination
        while current_vertex is not None:
            path.push(current_vertex)
            current_vertex = path_dict[current_vertex][1]

    if metros != -1:
        path_str = ""
        while path.size() > 0:
            path_str += path.pop() + " -> "
        print(f"   Se necesitan {metros} metros de cable de red.")
        print(f"   Camino: {path_str.strip(' -> ')}")
    else:
        print("   No se encontró un camino entre la habitación 1 y la sala de estar.")

if __name__ == "__main__":
    imprimir_titulo("Ejercicio 14")
    casa_graph = PuntoA_B()
    PuntoC(casa_graph)
    PuntoD(casa_graph)
