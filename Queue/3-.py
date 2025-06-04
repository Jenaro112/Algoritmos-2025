"""
Dada una secuencia de caracteres, utilizar operaciones de cola y pila para determinar
si es un palíndromo, sin alterar la cola original.
"""

from queue_ import Queue
from stack_ import Stack

def palindromo(cola: Queue) -> bool:
    pila = Stack()
    size = cola.size()
    
    # Mover todos los elementos de la cola a la pila
    for _ in range(size):
        char = cola.attention()
        pila.push(char)
        cola.arrive(char)  # Restaurar la cola

    # Comparar los elementos de la pila con los de la cola
    for _ in range(size):
        if pila.pop() != cola.attention():
            return False
    return True

cola = Queue()

palabra = input("Ingrese una palabra: ")
for c in palabra:
    cola.arrive(c)

print("-" * 50)
print("Cola:")
cola.show()
print("-" * 50)

if palindromo(cola):
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")
print("-" * 50)
