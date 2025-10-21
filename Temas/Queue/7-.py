"""
Eliminar el i-ésimo elemento después del frente de la cola.
"""

from queue_ import Queue

def eliminar_iesimo(cola: Queue, i: int) -> None:
    # Mover los primeros i-1 elementos a una cola temporal
    temp_queue = Queue()

    for _ in range(i - 1):
        temp_queue.arrive(cola.attention())
    
    # Eliminar el i-ésimo elemento
    cola.attention()
    
    # Mover los elementos de la cola temporal de vuelta a la cola original
    while temp_queue.size() > 0:
        cola.arrive(temp_queue.attention())

cola = Queue()
for _ in range(1,10):
    cola.arrive(_)

print("-" * 50)
print("Cola original:")
cola.show()

i = 3

eliminar_iesimo(cola, i)

print("-" * 50)
print(f"Cola después de eliminar el {i}-ésimo elemento:")
cola.show()