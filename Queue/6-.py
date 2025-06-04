"""
Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ninguna estructura auxiliar.
"""

import queue_


def ocurrencias(cola: queue_.Queue, elemento: int) -> int:
    contador = 0
    tamaño = cola.size()
    for _ in range(tamaño):
        current = cola.attention()
        if current == elemento:
            contador += 1
        cola.arrive(current)
    
    return contador


cola = queue_.Queue()
for item in [1, 2, 3, 4, 5, 1, 2, 1, 6, 7]:
    cola.arrive(item)

ocurrencias_1 = ocurrencias(cola, 1)
ocurrencias_2 = ocurrencias(cola, 2)

print("-" * 50)
print("ocurrencias de elementos en la cola:")
print(f"La cantidad de ocurrencias del elemento 1 en la cola es: {ocurrencias_1}")
print(f"La cantidad de ocurrencias del elemento 2 en la cola es: {ocurrencias_2}")
print("-" * 50)