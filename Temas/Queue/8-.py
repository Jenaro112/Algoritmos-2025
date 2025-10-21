"""
Realizar un algoritmo que mantenga ordenado los elementos agregados a una cola, utilizando solo una cola como estructura auxiliar.
"""

from queue_ import Queue

def burbuja(queue: Queue) -> Queue:
    n = queue.size()
    for j in range(n):
        previo = queue.attention()
        for j in range(queue.size()):
            actual = queue.attention()
            if previo > actual:
                queue.arrive(actual)
            else:
                queue.arrive(previo)
                previo = actual
        queue.arrive(previo)
    return queue

cola = Queue()
for i in [5, 3, 8, 6, 2]:
    cola.arrive(i)

print("Cola sin ordenar:")
cola.show()

cola_ordenada = burbuja(cola)
print("Cola ordenada:")
cola_ordenada.show()