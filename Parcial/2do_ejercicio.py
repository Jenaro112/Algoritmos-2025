"""
Jenaro Galdini | 2do año de Licenciatura en Sistemas
--- PRIMER PARCIAL ---
Ejercicio 2: Dada una lista de personajes de marvel (la desarrollada en clases) debe tener 100 o mas, resolver:
-   a.Listado ordenado de manera ascendente por nombre de los personajes.
-   b.Determinar en que posicion esta The Thing y Rocket Raccoon.
-   c.Listar todos los villanos de la lista.
-   d.Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
-   e.Listar los superheores que comienzan con  Bl, G, My, y W.
-   f.Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
-   g.Listado de superheroes ordenados por fecha de aparación.
-   h.Modificar el nombre real de Ant Man a Scott Lang.
-   i.Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
-   j.Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.
"""

from list_ import List
from super_heroes_data import superheroes
from queue_ import Queue



class Superheroes:
    
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        return f"{self.name}, {self.real_name}"



def order_by_name(item):
    return item.name

def order_by_year(item):
    return item.year

def order_by_real_name(item):
    return item.real_name or ""

def order_by_first_appearance(item):
    return item.first_appearance

list_superhero = List()
list_superhero.add_criterion('name', order_by_name)
list_superhero.add_criterion('real_name', order_by_real_name)
list_superhero.add_criterion('first_appearance', order_by_first_appearance)

for superhero in superheroes:
    hero = Superheroes(
        name=superhero["name"],
        alias=superhero["alias"],
        real_name=superhero["real_name"],
        short_bio=superhero["short_bio"],
        first_appearance=superhero["first_appearance"],
        is_villain=superhero["is_villain"],
    )
    list_superhero.append(hero)

#Punto A
def Punto_A():
    print("---PUNTO A---")
    print("Listado ordenado de manera ascendente por nombre de los personajes:")
    
    list_superhero.sort_by_criterion('name')
    for hero in list_superhero:
        print(hero)

#Punto B
def Punto_B():
    print("---PUNTO B---")
    print("Posición de The Thing y Rocket Raccoon:")
    Posicion_The_Thing = list_superhero.search('The Thing', 'name')
    Posicion_Rocket_Raccoon = list_superhero.search('Rocket Raccoon', 'name')
    if Posicion_The_Thing is not None:
        print(f"The Thing está en la posición: {Posicion_The_Thing}")
    else:
        print("The Thing no está en la lista.")
    if Posicion_Rocket_Raccoon is not None:
        print(f"Rocket Raccoon está en la posición: {Posicion_Rocket_Raccoon}")

#Punto C
def Punto_C():
    print("---PUNTO C---")
    print("Listado de villanos:")
    for hero in list_superhero:
        if hero.is_villain:
            print(hero)

#Punto D
def Punto_D():
    print("---PUNTO D---")
    cola_villanos = Queue()
    for hero in list_superhero:
        if hero.is_villain:
            cola_villanos.arrive(hero)

    print("Villanos antes de 1980:")
    while cola_villanos.size() > 0:
        villano = cola_villanos.attention()
        if villano.first_appearance < 1980:
            print(f"{villano.name} - {villano.first_appearance}")


#Punto E
def Punto_E():
    print("---PUNTO E---")
    print("Superhéroes que comienzan con Bl, G, My, y W:")
    for hero in list_superhero:
        if hero.name.startswith(('Bl', 'G', 'My', 'W')):
            print(hero)

#Punto F
def Punto_F():
    print("---PUNTO F---")
    print("Listado de personajes ordenado por nombre real:")
    list_superhero.sort_by_criterion('real_name')
    for hero in list_superhero:
        print(f"{hero.real_name} - {hero.name}")


#Punto G
def Punto_G():
    print("---PUNTO G---")
    print("Listado de superhéroes ordenados por fecha de aparición:")
    list_superhero.sort_by_criterion('first_appearance')
    for hero in list_superhero:
        print(f"{hero.name} - {hero.first_appearance}")

#Punto H
def Punto_H():
    print("---PUNTO H---")
    print("Modificando el nombre real de Ant Man: de Hank Pym a Scott Lang:")
    pos = list_superhero.search('Ant Man', 'name')
    if pos is not None:
        list_superhero[pos].real_name = 'Scott Lang'
        print(f"Nombre real de Ant Man modificado a: {list_superhero[pos].real_name}")

#Punto I
def Punto_I():
    print("---PUNTO I---")
    print("Personajes con 'time-traveling' o 'suit' en su biografía:")
    for hero in list_superhero:
        if 'time-traveling' in hero.short_bio or 'suit' in hero.short_bio:
            print(hero)

#Punto J
def Punto_J():
    print("---PUNTO J---")
    print("Eliminando a Electro y Baron Zemo:")
    for name in ['Electro', 'Baron Zemo']:
        heroe_eliminado = list_superhero.delete_value(name, 'name')
        if heroe_eliminado is not None:
            print(f"Eliminado: {heroe_eliminado}")
        else:
            print(f"{name} no estaba en la lista.")

print("-" * 50)
print("EXAMEN DE JENARO GALDINI")
print("Primer Parcial - Ejercicio 2")
print("-" * 50)
Punto_A()
print("-" * 50)
Punto_B()
print("-" * 50)
Punto_C()
print("-" * 50)
Punto_D()
print("-" * 50)
Punto_E()
print("-" * 50)
Punto_F()
print("-" * 50)
Punto_G()
print("-" * 50)
Punto_H()
print("-" * 50)
Punto_I()
print("-" * 50)
Punto_J()
print("-" * 50)