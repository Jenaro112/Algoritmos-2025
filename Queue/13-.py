"""  
Dada una cola de 50000 caracteres generados aleatoriamente realizar las siguientes actividades:
-   a. separarla en dos colas una con dígitos y otra con el resto de los caracteres.
-   b. determinar cuántas letras hay en la segunda cola.
-   c. determinar además si existen los caracteres “?” y “#”.
"""

from queue_ import Queue
from random import choice, randint

#! NO PONER 50000 :/
cola = Queue()
for i in range(50):
    cola.arrive(choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!#"))

def separar(cola: Queue) -> tuple[Queue, Queue]:
    cola_digitos = Queue()
    cola_letras = Queue()
    
    for i in range(cola.size()):
        caracter = cola.attention()
        if caracter.isdigit():
            cola_digitos.arrive(caracter)
        else:
            cola_letras.arrive(caracter)
        cola.arrive(caracter)  # Volvemos a agregar el elemento a la cola original
    
    return cola_digitos, cola_letras

def contar_letras(cola: Queue) -> int:
    contador = 0
    
    for i in range(cola.size()):
        caracter = cola.attention()
        if caracter.isalpha():
            contador += 1
        cola.arrive(caracter)  # Volvemos a agregar el elemento a la cola
    
    return contador

def caracter(cola: Queue, caracter: str) -> bool:
    for i in range(cola.size()):
        c = cola.attention()
        if c == caracter:
            cola.arrive(c)  # Volvemos a agregar el elemento a la cola
            return True
        cola.arrive(c)  # Volvemos a agregar el elemento a la cola
    return False

cola_digitos, cola_letras = separar(cola)
print("-" * 50)
cola_digitos.show()
print("-" * 50)
cola_letras.show()
print("-" * 50)
contar_letras = contar_letras(cola_letras)
print(f"Número de letras en la cola de letras: {contar_letras}")
print("-" * 50)
caracter_existe = caracter(cola_letras, "?")
print(f"¿Existe el caracter '?': {caracter_existe}")
caracter_existe = caracter(cola_letras, "#")
print(f"¿Existe el caracter '#': {caracter_existe}")
print("-" * 50)