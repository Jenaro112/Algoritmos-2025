"""
Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos,
una que contenga los números pares y otra para los números impares.
"""

from list_ import List

lista_numeros = List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def pares_impares(lista: List) -> tuple[List, List]:

    pares = List()
    impares = List()
    
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    return pares, impares

pares, impares = pares_impares(lista_numeros)
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")