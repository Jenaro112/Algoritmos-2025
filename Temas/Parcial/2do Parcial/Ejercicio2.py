"""
* Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:
* cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
*-  a.  hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
*-  b.  determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;
*-  c.  cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;
*-  d.  calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
*-  e.  indicar qué personajes aparecieron en los nueve episodios de la saga
"""

from graph import Graph
from stack import Stack
from typing import Any

print("╔" + "═"*50 + "╗")
print("║" + "2DO PARCIAL DE ALGORITMOS Y ESTRUCTURAS DE DATOS".center(50) + "║")
print("║" + "JENARO GALDINI".center(50) + "║")
print("╚" + "═"*50 + "╝")

def cargar_grafo_star_wars():
    g = Graph()
    
    # Personajes y el número de episodios en los que aparecen
    personajes = [
        ("Luke Skywalker", 6), ("Darth Vader", 6), ("Yoda", 6), ("Boba Fett", 4),
        ("C-3PO", 9), ("Leia", 7), ("Rey", 3), ("Kylo Ren", 3),
        ("Chewbacca", 8), ("Han Solo", 5), ("R2-D2", 9), ("BB-8", 3)
    ]
    for nombre, episodios in personajes:
        g.insert_vertex(nombre)
        pos = g.search(nombre, 'value')
        if pos is not None:
            g[pos].other_values = {'episodes': episodios}

    # Aristas: (personaje1, personaje2, episodios_juntos)
    relaciones = [
        ("Luke Skywalker", "Darth Vader", 4), ("Luke Skywalker", "Leia", 4),
        ("Luke Skywalker", "Han Solo", 3), ("Luke Skywalker", "C-3PO", 5),
        ("Luke Skywalker", "R2-D2", 5), ("Darth Vader", "Leia", 3),
        ("Yoda", "Luke Skywalker", 3), ("Yoda", "C-3PO", 2),
        ("Han Solo", "Leia", 4), ("Han Solo", "Chewbacca", 4),
        ("C-3PO", "R2-D2", 9), ("C-3PO", "Leia", 6),
        ("Chewbacca", "Leia", 4), ("Boba Fett", "Darth Vader", 2),
        ("Rey", "Kylo Ren", 3), ("Rey", "BB-8", 3), ("Kylo Ren", "Darth Vader", 1) # Conexión simbólica
    ]
    for p1, p2, peso in relaciones:
        g.insert_edge(p1, p2, peso)
        
    print("Grafo de Star Wars cargado.")
    return g

def punto_a(g):
    print("\n" + "╔" + "═"*50 + "╗")
    print("║" + " a. Árbol de Expansión Mínimo".ljust(50) + "║")
    print("╚" + "═"*50 + "╝")
    personajes_mst = ["C-3PO", "Yoda", "Leia"]
    for personaje in personajes_mst:
        mst_str = g.kruskal(personaje)
        total_episodios = 0
        print(f"\n  ● MST para '{personaje}':")
        for edge in mst_str.split(';'):
            parts = edge.split('-')
            if len(parts) == 3:
                p1, p2, peso = parts
                total_episodios += int(peso)
                print(f"    › {p1} ↔ {p2} ({peso} episodios)")
        print(f"\n    Costo total del MST: {total_episodios} episodios")

def punto_b(g):
    print("\n" + "╔" + "═"*50 + "╗")
    print("║" + " b. Máximo de episodios compartidos".ljust(50) + "║")
    print("╚" + "═"*50 + "╝")
    max_episodios = 0
    pares = []
    for i in range(len(g)):
        personaje = g[i]
        for arista in personaje.edges:
            if arista.weight > max_episodios:
                max_episodios = arista.weight
                pares = [(personaje.value, arista.value)]
            elif arista.weight == max_episodios:
                # Evitar duplicados (ej. A-B y B-A)
                if (arista.value, personaje.value) not in pares:
                    pares.append((personaje.value, arista.value))
    
    print(f"\n  ● El número máximo de episodios compartidos es: {max_episodios}")
    print("  ● Pares de personajes que coinciden:")
    for p1, p2 in pares:
        print(f"    › {p1} y {p2}")

def punto_d(g):
    print("\n" + "╔" + "═"*50 + "╗")
    print("║" + " d. Caminos más cortos".ljust(50) + "║")
    print("╚" + "═"*50 + "╝")
    caminos = [("C-3PO", "R2-D2"), ("Yoda", "Darth Vader")]
    for origen, destino in caminos:
        path_info = g.dijkstra(origen)
        path, cost = g.reconstruct_path(path_info, destino)
        print(f"\n  ● Camino más corto de '{origen}' a '{destino}':")
        if cost != -1:
            path_str = ""
            while path.size() > 0:
                path_str += path.pop() + " -> "
            print(f"  Camino: {path_str.strip(' -> ')}")
            print(f"  Episodios (costo): {cost}")

def punto_e(g):
    print("\n" + "╔" + "═"*50 + "╗")
    print("║" + " e. Personajes en los 9 episodios de la saga".ljust(50) + "║")
    print("╚" + "═"*50 + "╝")
    for i in range(len(g)):
        personaje = g[i]
        if personaje.other_values and personaje.other_values.get('episodes') == 9:
            print(f"  › {personaje.value}")

def main():
    grafo_sw = cargar_grafo_star_wars()
    punto_a(grafo_sw)
    punto_b(grafo_sw)
    punto_d(grafo_sw)
    punto_e(grafo_sw)

if __name__ == "__main__":
    main()