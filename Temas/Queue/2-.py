""" 
Utilizando operaciones de cola y pila, invertir el contenido de una cola.
"""

import queue_
import stack_


cola1 = [1,2,3,4,5,6,7,8,9,10]

def invertido(cola: queue_.Queue) -> None:
    pila = stack_.Stack()
    
    # Mover todos los elementos de la cola a la pila
    while cola.size() > 0:
        pila.push(cola.attention())
    
    # Mover todos los elementos de la pila de vuelta a la cola
    while pila.size() > 0:
        cola.arrive(pila.pop())

cola1 = queue_.Queue()

for i in range(1, 11):
    cola1.arrive(i) 

invertido(cola1)
print("Cola invertida:")
cola1.show() 