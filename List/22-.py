""" 
Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
actividades enumeradas a continuación:
a. listado ordenado por nombre y por especie;
b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
d. mostrar los Jedi de especie humana y twi'lek;
e. listar todos los Jedi que comienzan con A;
f. mostrar los Jedi que usaron sable de luz de más de un color;
g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
"""

from list_ import List

class Jedi:
    def __init__(self, nombre, especie, maestros, colores_sable):
        self.nombre = nombre
        self.especie = especie
        self.maestros = maestros
        self.colores_sable = colores_sable

    def __str__(self):
        maestros_str = ", ".join(self.maestros) if self.maestros else "Ninguno"
        sables_str = ", ".join(self.colores_sable)
        return (f"Nombre: {self.nombre} | Especie: {self.especie} | "
                f"Maestros: {maestros_str} | Sables: {sables_str}")

# --- Datos de los Jedi ---
jedi_data = [
    {"nombre": "Luke Skywalker", "especie": "Humano", "maestros": ["Obi-Wan Kenobi", "Yoda"], "colores_sable": ["verde", "azul"]},
    {"nombre": "Yoda", "especie": "Desconocida", "maestros": [], "colores_sable": ["verde"]},
    {"nombre": "Ahsoka Tano", "especie": "Togruta", "maestros": ["Anakin Skywalker"], "colores_sable": ["verde", "blanco"]},
    {"nombre": "Kit Fisto", "especie": "Nautolan", "maestros": ["Yoda"], "colores_sable": ["verde"]},
    {"nombre": "Mace Windu", "especie": "Humano", "maestros": [], "colores_sable": ["violeta"]},
    {"nombre": "Obi-Wan Kenobi", "especie": "Humano", "maestros": ["Qui-Gon Jinn"], "colores_sable": ["azul"]},
    {"nombre": "Qui-Gon Jinn", "especie": "Humano", "maestros": ["Conde Dooku"], "colores_sable": ["verde"]},
    {"nombre": "Aayla Secura", "especie": "Twi'lek", "maestros": ["Quinlan Vos"], "colores_sable": ["azul"]},
    {"nombre": "Plo Koon", "especie": "Kel Dor", "maestros": [], "colores_sable": ["azul"]},
    {"nombre": "Rey", "especie": "Humano", "maestros": ["Luke Skywalker", "Leia Organa"], "colores_sable": ["amarillo", "azul"]},
    {"nombre": "Kanan Jarrus", "especie": "Humano", "maestros": ["Depa Billaba"], "colores_sable": ["azul"]},
    {"nombre": "Depa Billaba", "especie": "Chalactan", "maestros": ["Mace Windu"], "colores_sable": ["verde"]},
]

# --- Funciones de resolución ---

def Punto_A(lista):
    print("Punto A\n")
    print("Ordenado por Nombre:")
    lista.sort_by_criterion('nombre')
    for jedi in lista:
        print(jedi.nombre)
    
    print("\nOrdenado por Especie:")
    lista.sort_by_criterion('especie')
    for jedi in lista:
        print(f"{jedi.nombre} ({jedi.especie})")
    print("-" * 30)

def Punto_B(lista):
    print("Punto B\n")
    for nombre_jedi in ["Ahsoka Tano", "Kit Fisto"]:
        index = lista.search(nombre_jedi, 'nombre')
        if index is not None:
            print(lista[index])
        else:
            print(f"{nombre_jedi} no encontrado.")
    print("-" * 30)

def Punto_C(lista):
    print("Punto C\n")
    for jedi in lista:
        if "Yoda" in jedi.maestros or "Luke Skywalker" in jedi.maestros:
            print(f"- {jedi.nombre}")
    print("-" * 30)

def Punto_D(lista):
    print("Punto D\n")
    for jedi in lista:
        if jedi.especie in ["Humano", "Twi'lek"]:
            print(f"- {jedi.nombre} ({jedi.especie})")
    print("-" * 30)

def Punto_E(lista):
    print("Punto E\n")
    for jedi in lista:
        if jedi.nombre.startswith('A'):
            print(f"- {jedi.nombre}")
    print("-" * 30)

def Punto_F(lista):
    print("Punto F\n")
    for jedi in lista:
        if len(jedi.colores_sable) > 1:
            print(f"- {jedi.nombre} (Colores: {', '.join(jedi.colores_sable)})")
    print("-" * 30)

def Punto_G(lista):
    print("Punto G\n")
    for jedi in lista:
        if "amarillo" in jedi.colores_sable or "violeta" in jedi.colores_sable:
            print(f"- {jedi.nombre}")
    print("-" * 30)

def Punto_H(lista):
    print("Punto H\n")
    padawans_encontrados = False
    for jedi in lista:
        if "Qui-Gon Jinn" in jedi.maestros or "Mace Windu" in jedi.maestros:
            print(f"- {jedi.nombre} (Maestro: {', '.join(jedi.maestros)})")
            padawans_encontrados = True
    if not padawans_encontrados:
        print("No se encontraron padawans para Qui-Gon Jinn o Mace Windu en la lista.")
    print("-" * 30)


# --- Programa Principal ---
if __name__ == "__main__":
    lista_jedi = List()

    # Criterios de ordenación/búsqueda
    def by_name(jedi):
        return jedi.nombre

    def by_species(jedi):
        return jedi.especie

    lista_jedi.add_criterion('nombre', by_name)
    lista_jedi.add_criterion('especie', by_species)

    for data in jedi_data:
        lista_jedi.append(Jedi(
            nombre=data["nombre"],
            especie=data["especie"],
            maestros=data["maestros"],
            colores_sable=data["colores_sable"]
        ))

    print("-" * 30)
    Punto_A(lista_jedi)
    Punto_B(lista_jedi)
    Punto_C(lista_jedi)
    Punto_D(lista_jedi)
    Punto_E(lista_jedi)
    Punto_F(lista_jedi)
    Punto_G(lista_jedi)
    Punto_H(lista_jedi)
