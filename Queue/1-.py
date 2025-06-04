""" 
Eliminar de una cola de caracteres todas las vocales que aparecen.
"""

from queue_ import Queue

def eliminar_vocales(cola: Queue) -> None:
    vocales = {'a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'}
    size_inicial = cola.size()
    
    for _ in range(size_inicial):
        char = cola.attention()
        if char not in vocales:
            cola.arrive(char)


cola = Queue()

palabra = input("Ingrese una palabra: ")
for c in palabra:
    cola.arrive(c)

print("-" * 50)
print("Antes de eliminar vocales:")
cola.show()

eliminar_vocales(cola)

print("-" * 50)
print("Después de eliminar vocales:")
cola.show()