""" 
Dada una cola de valores enteros calcular su rango y contar cuántos elementos negativos hay.
"""

from queue_ import Queue
from random import randint

def rango(cola: Queue) -> int:

    valor_min = float('inf')
    valor_max = float('-inf')
    
    for _ in range(cola.size()):
        valor = cola.attention()
        valor_min = min(valor_min, valor)
        valor_max = max(valor_max, valor)
        cola.arrive(valor)  # Volvemos a agregar el elemento a la cola
    
    return valor_max - valor_min

def negativos(cola: Queue) -> int:
    contador = 0
    
    for j in range(cola.size()):
        valor = cola.attention()
        if valor < 0:
            contador += 1
        cola.arrive(valor)  # Volvemos a agregar el elemento a la cola
    return contador

cola = Queue()
for _ in range(10):
    cola.arrive(randint(-10, 10))

print("-" * 50)
print("Cola de enteros:")
cola.show()

print("-" * 50)
print(f"Rango de la cola: {rango(cola)}")
print("-" * 50)
print(f"Número de elementos negativos en la cola: {negativos(cola)}")
print("-" * 50)
