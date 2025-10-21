"""
Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.
"""

from list_ import List

def nodos(lista: List) -> int:

    return f"La cantidad de nodos son: {len(lista)}"

Marvel = List()
for i in range(10):
    Marvel.append(i)

print(nodos(Marvel))  # Debería imprimir 10, ya que hemos añadido 10 nodos a la lista.

