"""
Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista.
"""

from list_ import List

lista = List([1, 2, 3, 4, 5])

def insertar_pos(lista: List, valor: int, posicion: int) -> List:
    
    lista.insert(posicion, valor)
    return lista

posicion = 2
valor = 10

lista_actualizada = insertar_pos(lista, valor, posicion)
print(f"Lista actualizada: {lista_actualizada}")
