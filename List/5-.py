"""  
Dada una lista de números enteros eliminar de estas los números primos.
"""

from list_ import List

lista_numeros = List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def es_primo(numero: int) -> bool:

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def eliminar(lista: List) -> List:
    for numero in lista.copy():
        if es_primo(numero):
            lista.delete_value(numero)
    return lista

es_primos = eliminar(lista_numeros)
print(f"Números no primos: {es_primos}")
