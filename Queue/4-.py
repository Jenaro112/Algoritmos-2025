"""
Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos
"""

from queue_ import Queue
from random import randint

def Primo(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

def eliminar_no_primos(cola: Queue) -> None:
    size_inicial = cola.size()
    
    for _ in range(size_inicial):
        num = cola.attention()
        if Primo(num):
            cola.arrive(num)

cola = Queue()
for _ in range(10):
    cola.arrive(randint(1, 100))  # Cargar la cola con números aleatorios entre 1 y 100

print("-" * 50)
print("-Cola original:")
cola.show()

eliminar_no_primos(cola)

print("-" * 50)
print("-Cola después de eliminar no primos:")
cola.show()
print("-" * 50)