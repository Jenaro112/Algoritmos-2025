from typing import Any, Optional

from Profesor import graph

""" 
* insertar_vértice(grafo, dato). Agrega el elemento como un vértice al grafo;
"""

grafo = graph.Graph()

grafo.insert_vertex('A')
grafo.insert_vertex('B')
grafo.insert_vertex('C') 

grafo.show()