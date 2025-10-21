"""
Utilizando operaciones de cola y pila, invertir el contenido de una pila.
"""
from queue_ import Queue
from stack_ import Stack

def invertido(pila: Stack) -> None:
    cola = Queue()
    
    # Mover todos los elementos de la pila a la cola
    while pila.size() > 0:
        cola.arrive(pila.pop())
    
    # Mover todos los elementos de la cola de vuelta a la pila
    while cola.size() > 0:
        pila.push(cola.attention())

pila1 = Stack()
for i in range(1, 11):
    pila1.push(i)

print("-" * 50)
print("Pila original:")
pila1.show()

invertido(pila1)
print("-" * 50)
print("Pila invertida:")
pila1.show()

