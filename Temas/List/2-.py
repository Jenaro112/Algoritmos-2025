"""  
Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.
"""

from list_ import List


lista_caracteres = List(['a', 'b', 'c', 'e', 'i', 'o', 'u', 'x'])   

def vocales():
    """
    Elimina todas las vocales de la lista de caracteres.
    """
    vocales = ['a', 'e', 'i', 'o', 'u']
    for caracter in vocales:
        lista_caracteres.delete_value(caracter)
    
    return lista_caracteres

vocales()
print(lista_caracteres)