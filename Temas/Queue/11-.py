"""  
Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
-   a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
-   b. indicar el plantea natal de Luke Skywalker y Han Solo
-   c. insertar un nuevo personaje antes del maestro Yoda
-   d. eliminar el personaje ubicado después de Jar Jar Binks
"""

import queue_

cola = queue_.Queue()

cola.arrive({"nombre": "Luke Skywalker", "planeta": "Tatooine"})
cola.arrive({"nombre": "Han Solo", "planeta": "Corellia"})
cola.arrive({"nombre": "Leia Organa", "planeta": "Alderaan"})
cola.arrive({"nombre": "Yoda", "planeta": "Dagobah"})
cola.arrive({"nombre": "Jar Jar Binks", "planeta": "Naboo"})
cola.arrive({"nombre": "Obi-Wan Kenobi", "planeta": "Stewjon"})

def Planetas(cola: queue_.Queue):
    print("Personajes de los planetas Alderaan, Endor y Tatooine:")
    for i in range(cola.size()):
        personaje = cola.attention()
        if personaje["planeta"] in ["Alderaan", "Endor", "Tatooine"]:
            print(f"  - {personaje['nombre']} ({personaje['planeta']})")
        cola.arrive(personaje)

def Luke_Han(cola: queue_.Queue):
    print("Planeta natal de Luke Skywalker y Han Solo:")
    for i in range(cola.size()):
        personaje = cola.attention()
        if personaje["nombre"] == "Luke Skywalker":
            print(f"  - {personaje['nombre']} es de {personaje['planeta']}")
        elif personaje["nombre"] == "Han Solo":
            print(f"  - {personaje['nombre']} es de {personaje['planeta']}")
        cola.arrive(personaje)

def Yoda(cola: queue_.Queue, new_pj: dict):
    print("Insertando un nuevo personaje antes del maestro Yoda:")
    for i in range(cola.size()):
        personaje = cola.attention()
        if personaje["nombre"] == "Yoda":
            cola.arrive(new_pj)
        cola.arrive(personaje)

def Jar_Jar(cola: queue_.Queue):
    print("Eliminando el personaje ubicado después de Jar Jar Binks:")
    for i in range(cola.size()):
        personaje = cola.attention()
        if personaje["nombre"] == "Jar Jar Binks":
            sig_pj = cola.attention()  # Eliminar el siguiente personaje
            print(f"  - Se eliminó a {sig_pj['nombre']} que estaba después de Jar Jar Binks.")
        else:
            cola.arrive(personaje)

print("-" * 50)
Planetas(cola)
print("-" * 50)
Luke_Han(cola)
print("-" * 50)
Yoda(cola, {"nombre": "Rey", "planeta": "Jakku"})
print("-" * 50)
Jar_Jar(cola)
print("-" * 50)
