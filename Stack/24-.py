"""
Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y la cantidad de películas de la saga en la que participó,implementar las funciones necesarias para resolver las siguientes actividades:

a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
"""

from stack import Stack

personajes_mcu = [
    {"nombre": "Iron Man", "peliculas": 10},
    {"nombre": "Captain America", "peliculas": 9},
    {"nombre": "Black Widow", "peliculas": 7},
    {"nombre": "Hulk", "peliculas": 6},
    {"nombre": "Thor", "peliculas": 8},
    {"nombre": "Hawkeye", "peliculas": 6},
    {"nombre": "Rocket Raccoon", "peliculas": 4},
    {"nombre": "Groot", "peliculas": 5},
    {"nombre": "Doctor Strange", "peliculas": 4},
    {"nombre": "Captain Marvel", "peliculas": 3},
    {"nombre": "Gamora", "peliculas": 4},
    {"nombre": "Star-Lord", "peliculas": 4},
    {"nombre": "Drax", "peliculas": 4},
    {"nombre": "Vision", "peliculas": 3},
]

pila_personajes = Stack()
for personaje in personajes_mcu:
    pila_personajes.push(personaje)

# (a) Posición de Rocket Raccoon y Groot
def posicion_personajes(pila: Stack, nombres: list):
    aux = Stack()
    posiciones = {}
    pos = 1
    while not pila.is_empty():
        personaje = pila.pop()
        if personaje["nombre"] in nombres:
            posiciones[personaje["nombre"]] = pos
        aux.push(personaje)
        pos += 1
    while not aux.is_empty():
        pila.push(aux.pop())
    for nombre in nombres:
        if nombre in posiciones:
            print(f"{nombre} está en la posición {posiciones[nombre]}.")
        else:
            print(f"{nombre} no se encontró en la pila.")

# (b) Personajes con más de 5 películas
def personajes_mas_de_cinco(pila: Stack):
    aux = Stack()
    print("Personajes con más de 5 películas:")
    while not pila.is_empty():
        personaje = pila.pop()
        if personaje["peliculas"] > 5:
            print(f"  - {personaje['nombre']}: {personaje['peliculas']} películas")
        aux.push(personaje)
    while not aux.is_empty():
        pila.push(aux.pop())

# (c) Películas de Black Widow
def peliculas_black_widow(pila: Stack):
    aux = Stack()
    cantidad = None
    while not pila.is_empty():
        personaje = pila.pop()
        if personaje["nombre"] == "Black Widow":
            cantidad = personaje["peliculas"]
        aux.push(personaje)
    while not aux.is_empty():
        pila.push(aux.pop())
    if cantidad is not None:
        print(f"Black Widow participó en {cantidad} películas.")
    else:
        print("Black Widow no se encontró en la pila.")

# (d) Personajes que empiezan con C, D o G
def personajes_letras_especificas(pila: Stack):
    aux = Stack()
    letras = ('C', 'D', 'G')
    print("Personajes que comienzan con C, D o G:")
    while not pila.is_empty():
        personaje = pila.pop()
        if personaje["nombre"].startswith(letras):
            print(f"  - {personaje['nombre']}")
        aux.push(personaje)
    while not aux.is_empty():
        pila.push(aux.pop())

# Ejecutar todas las funciones
posicion_personajes(pila_personajes, ["Rocket Raccoon", "Groot"])
personajes_mas_de_cinco(pila_personajes)
peliculas_black_widow(pila_personajes)
personajes_letras_especificas(pila_personajes)
