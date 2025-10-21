"""
------------------------------
|       Trabajo N° 6         |
------------------------------
Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición, casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar las siguientes actividades:
-   a. eliminar el nodo que contiene la información de Linterna Verde;
-   b. mostrar el año de aparición de Wolverine;
-   c. cambiar la casa de Dr. Strange a Marvel;
-   d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
-   e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
-   f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
-   g. mostrar toda la información de Flash y Star-Lord;
-   h. listar los superhéroes que comienzan con la letra B, M y S;
-   i. determinar cuántos superhéroes hay de cada casa de comic.
"""

from list_ import List
from super_heroes_data import superheroes

class Superhero:
    def __init__(self, nombre, anio_aparicion, casa_comic, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa_comic = casa_comic
        self.biografia = biografia

    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Año de aparición: {self.anio_aparicion}\n"
                f"Casa de cómic: {self.casa_comic}\n"
                f"Biografía: {self.biografia}")

# a. eliminar el nodo que contiene la información de Linterna Verde
def Punto_A(lista):
    print("PUNTO A")
    eliminado = lista.delete_value("Linterna Verde", "nombre")
    if eliminado:
        print(f"Se eliminó a: {eliminado.nombre}")
    else:
        print("Linterna Verde no se encontró en la lista.")

# b. mostrar el año de aparición de Wolverine
def Punto_B(lista):
    print("PUNTO B")
    index_wolverine = lista.search("Wolverine", "nombre")
    if index_wolverine is not None:
        print(f"Wolverine apareció en: {lista[index_wolverine].anio_aparicion}")
    else:
        print("Wolverine no se encontró en la lista.")

# c. cambiar la casa de Dr. Strange a Marvel
def Punto_C(lista):
    print("PUNTO C")
    index_strange = lista.search("Dr Strange", "nombre")
    if index_strange is not None:
        heroe = lista[index_strange]
        print(f"Casa original de Dr. Strange: {heroe.casa_comic}")
        heroe.casa_comic = "Marvel"
        print(f"Nueva casa de Dr. Strange: {heroe.casa_comic}")
    else:
        print("Dr. Strange no se encontró en la lista.")

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”
def Punto_D(lista):
    print("PUNTO D")
    for heroe in lista:
        if "suit" in heroe.biografia.lower() or "armor" in heroe.biografia.lower():
            print(heroe.nombre)

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963
def Punto_E(lista):
    print("PUNTO E")
    for heroe in lista:
        if heroe.anio_aparicion < 1963:
            print(f"{heroe.nombre} ({heroe.casa_comic})")

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla
def Punto_F(lista):
    print("PUNTO F")
    for nombre_heroe in ["Capitana Marvel", "Mujer Maravilla"]:
        index = lista.search(nombre_heroe, "nombre")
        if index is not None:
            print(f"{nombre_heroe} pertenece a: {lista[index].casa_comic}")
        else:
            print(f"{nombre_heroe} no se encontró.")

# g. mostrar toda la información de Flash y Star-Lord
def Punto_G(lista):
    print("PUNTO G")
    for nombre_heroe in ["Flash", "Star-Lord"]:
        index = lista.search(nombre_heroe, "nombre")
        if index is not None:
            print(lista[index])
            print()
        else:
            print(f"{nombre_heroe} no se encontró.")

# h. listar los superhéroes que comienzan con la letra B, M y S
def Punto_H(lista):
    print("PUNTO H")
    for heroe in lista:
        if heroe.nombre.startswith(('B', 'M', 'S')):
            print(heroe.nombre)

# i. determinar cuántos superhéroes hay de cada casa de comic
def Punto_I(lista):
    print("PUNTO I")
    conteo_casas = {}
    for heroe in lista:
        conteo_casas[heroe.casa_comic] = conteo_casas.get(heroe.casa_comic, 0) + 1
    
    for casa, cantidad in conteo_casas.items():
        print(f"{casa}: {cantidad} superhéroes")

if __name__ == "__main__":
    lista_superheroes = List()

    # Criterios de ordenación/búsqueda
    def by_name(hero):
        return hero.nombre

    lista_superheroes.add_criterion('nombre', by_name)

    # Cargar datos únicamente desde super_heroes_data.py
    for data in superheroes:
        # Asignamos casa de cómic. El archivo solo contiene Marvel.
        # Hacemos una excepción para Dr. Strange para que el punto C tenga sentido.
        casa = "Marvel"
        if data["name"] == "Dr Strange":
            casa = "DC"

        lista_superheroes.append(Superhero(
            nombre=data["name"],
            anio_aparicion=data["first_appearance"],
            casa_comic=casa,
            biografia=data["short_bio"]
        ))

    # Ejecutar cada punto del ejercicio
    print('-' * 30)
    Punto_A(lista_superheroes)
    print('-' * 30)
    Punto_B(lista_superheroes)
    print('-' * 30)
    Punto_C(lista_superheroes)
    print('-' * 30)
    Punto_D(lista_superheroes)
    print('-' * 30)
    Punto_E(lista_superheroes)
    print('-' * 30)
    Punto_F(lista_superheroes)
    print('-' * 30)
    Punto_G(lista_superheroes)
    print('-' * 30)
    Punto_H(lista_superheroes)
    print('-' * 30)
    Punto_I(lista_superheroes)
    print('-' * 30)
