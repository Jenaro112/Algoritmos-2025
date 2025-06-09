"""
Jenaro Galdini | 2do año de Licenciatura en Sistemas
--- PRIMER PARCIAL ---
Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
-   funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
-   funcion recursiva para listar los superheroes de la lista
"""

from list_ import List

def Cap_America(lista, nombre, indice=0):
    if indice >= len(lista):
        return False
    if lista[indice]['name'] == nombre:
        return True
    return Cap_America(lista, nombre, indice + 1)

def listar_superheroes(lista, indice=0):
    if indice >= len(lista):
        return
    print(f"{lista[indice]['name']} - {lista[indice]['alias']}")
    listar_superheroes(lista, indice + 1)

MCU = [
    {'name': 'Capitan America', 'alias': 'Steve Rogers'},
    {'name': 'Iron Man', 'alias': 'Tony Stark'},
    {'name': 'Thor', 'alias': 'Thor Odinson'},
    {'name': 'Hulk', 'alias': 'Bruce Banner'},
    {'name': 'Black Widow', 'alias': 'Natasha Romanoff'},
    {'name': 'Hawkeye', 'alias': 'Clint Barton'},
    {'name': 'Spider-Man', 'alias': 'Peter Parker'},
    {'name': 'Black Panther', 'alias': "T'Challa"},
    {'name': 'Doctor Strange', 'alias': 'Stephen Strange'},
    {'name': 'Scarlet Witch', 'alias': 'Wanda Maximoff'},
    {'name': 'Vision', 'alias': 'Vision'},
    {'name': 'Ant-Man', 'alias': 'Scott Lang'},
    {'name': 'Wasp', 'alias': 'Hope van Dyne'},
    {'name': 'Falcon', 'alias': 'Sam Wilson'},
    {'name': 'Winter Soldier', 'alias': 'Bucky Barnes'}
]

print("-" * 50)
print("EXAMEN DE JENARO GALDINI")
print("Primer Parcial - Ejercicio 1")
print("-" * 50)
if Cap_America(MCU, 'Capitan America'):
    print("El Capitan America esta en la lista")
else:
    print("El Capitan America NO esta en la lista")
print("-" * 50)
listar_superheroes(MCU)
print("-" * 50)
