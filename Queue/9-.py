""" 
Dada una cola de valores enteros calcular su rango y contar cuántos elementos negativos hay.
"""

from queue import Queue
from colorama import Fore, Style
from random import randint

Numeros = Queue()
for i in range(10):
    Numeros.put(randint(-10, 10))

def rango (cola:Queue):
    max = cola.queue[0]
    min = cola.queue[0]
    for i in range(cola.qsize()):
        num = cola.get()
        if num 

