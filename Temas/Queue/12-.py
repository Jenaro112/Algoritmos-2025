"""  
Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar, ni métodos de ordenamiento.
"""

from queue_ import Queue

cola1 = Queue()
cola2 = Queue()

for i in [1, 3, 5, 7, 9]:
    cola1.arrive(i)

for i in [2, 4, 6, 8, 10]:
    cola2.arrive(i)

def combinar(cola1: Queue, cola2: Queue) -> Queue:
    nueva_cola = Queue()
    
    if cola1.on_front() <= cola2.on_front(): # Comparamos los primeros elementos de ambas colas
        nueva_cola.arrive(cola1.attention())
    else:
        nueva_cola.arrive(cola2.attention())
    
    while cola1.size() > 0: # Mientras haya elementos en cola1
        nueva_cola.arrive(cola1.attention())
    
    while cola2.size() > 0: # Mientras haya elementos en cola2
        nueva_cola.arrive(cola2.attention())
    
    return nueva_cola

nueva_cola = combinar(cola1, cola2)

print("-" * 50)
nueva_cola.show()
print("-" * 50)

