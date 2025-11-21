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

# --- IMPORTACIONES DE LIBRERÍAS ---
# Importamos la clase List de tu librería `list_.py` y los datos de los superhéroes.
from list_ import List
from super_heroes_data import superheroes

# --- DEFINICIÓN DE LA CLASE SUPERHERO ---
class Superhero:
    """
    Representa a un superhéroe con sus atributos principales.
    Esta clase sirve como un molde para crear objetos que se almacenarán en la lista.
    """
    def __init__(self, nombre, anio_aparicion, casa_comic, biografia):
        # El constructor inicializa un nuevo objeto Superhero con los datos proporcionados.
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa_comic = casa_comic
        self.biografia = biografia

    def __str__(self):
        # El método __str__ define cómo se debe imprimir un objeto Superhero.
        # Es útil para mostrar la información completa de un personaje de forma legible.
        return (f"Nombre: {self.nombre}\n"
                f"Año de aparición: {self.anio_aparicion}\n"
                f"Casa de cómic: {self.casa_comic}\n"
                f"Biografía: {self.biografia}")

# --- DEFINICIÓN DE FUNCIONES PARA CADA PUNTO DEL EJERCICIO ---

# a. eliminar el nodo que contiene la información de Linterna Verde
def Punto_A(lista):
    """a. Elimina el nodo que contiene la información de Linterna Verde."""
    print("PUNTO A")
    # Se utiliza el método `delete_value` de tu clase List.
    # Busca un héroe cuyo 'nombre' sea "Linterna Verde" y lo elimina de la lista.
    eliminado = lista.delete_value("Linterna Verde", "nombre")
    if eliminado:
        print(f"Se eliminó a: {eliminado.nombre}")
    else:
        print("Linterna Verde no se encontró en la lista.")

# b. mostrar el año de aparición de Wolverine
def Punto_B(lista):
    """b. Muestra el año de aparición de Wolverine."""
    print("PUNTO B")
    # Se utiliza el método `search` para encontrar la posición (índice) de Wolverine en la lista.
    index_wolverine = lista.search("Wolverine", "nombre")
    # Si se encuentra (el índice no es None), se accede al objeto en esa posición y se imprime su año.
    if index_wolverine is not None:
        print(f"Wolverine apareció en: {lista[index_wolverine].anio_aparicion}")
    else:
        print("Wolverine no se encontró en la lista.")

# c. cambiar la casa de Dr. Strange a Marvel
def Punto_C(lista):
    """c. Cambia la casa de cómic de Dr. Strange a 'Marvel'."""
    print("PUNTO C")
    # Se busca la posición de Dr. Strange.
    index_strange = lista.search("Dr Strange", "nombre")
    if index_strange is not None:
        # Se obtiene el objeto del superhéroe desde la lista.
        heroe = lista[index_strange]
        print(f"Casa original de Dr. Strange: {heroe.casa_comic}")
        # Se modifica directamente el atributo `casa_comic` del objeto.
        heroe.casa_comic = "Marvel"
        print(f"Nueva casa de Dr. Strange: {heroe.casa_comic}")
    else:
        print("Dr. Strange no se encontró en la lista.")

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”
def Punto_D(lista):
    """d. Muestra los superhéroes que tienen 'traje' o 'armadura' en su biografía."""
    print("PUNTO D")
    # Se recorre toda la lista de superhéroes.
    for heroe in lista:
        # Se comprueba si las palabras 'suit' o 'armor' (en inglés, como en los datos)
        # están en la biografía del héroe (convertida a minúsculas para no distinguir mayúsculas).
        if "suit" in heroe.biografia.lower() or "armor" in heroe.biografia.lower():
            print(heroe.nombre)

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963
def Punto_E(lista):
    """e. Muestra los superhéroes que aparecieron antes de 1963."""
    print("PUNTO E")
    # Se recorre toda la lista.
    for heroe in lista:
        # Se filtra por el año de aparición.
        if heroe.anio_aparicion < 1963:
            print(f"{heroe.nombre} ({heroe.casa_comic})")

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla
def Punto_F(lista):
    """f. Muestra la casa de cómic de Capitana Marvel y Mujer Maravilla."""
    print("PUNTO F")
    # Se itera sobre una lista de nombres específicos.
    for nombre_heroe in ["Capitana Marvel", "Mujer Maravilla"]:
        # Se busca cada uno en la lista principal.
        index = lista.search(nombre_heroe, "nombre")
        if index is not None:
            print(f"{nombre_heroe} pertenece a: {lista[index].casa_comic}")
        else:
            print(f"{nombre_heroe} no se encontró.")

# g. mostrar toda la información de Flash y Star-Lord
def Punto_G(lista):
    """g. Muestra toda la información de Flash y Star-Lord."""
    print("PUNTO G")
    for nombre_heroe in ["Flash", "Star-Lord"]:
        index = lista.search(nombre_heroe, "nombre")
        if index is not None:
            # Al imprimir el objeto directamente, se invoca su método __str__.
            print(lista[index])
            print()
        else:
            print(f"{nombre_heroe} no se encontró.")

# h. listar los superhéroes que comienzan con la letra B, M y S
def Punto_H(lista):
    """h. Lista los superhéroes cuyos nombres comienzan con B, M o S."""
    print("PUNTO H")
    for heroe in lista:
        # El método `startswith` puede recibir una tupla de prefijos para buscar.
        if heroe.nombre.startswith(('B', 'M', 'S')):
            print(heroe.nombre)

# i. determinar cuántos superhéroes hay de cada casa de comic
def Punto_I(lista):
    """i. Cuenta cuántos superhéroes pertenecen a cada casa de cómic."""
    print("PUNTO I")
    # Se utiliza un diccionario para llevar la cuenta.
    conteo_casas = {}
    for heroe in lista:
        # .get(clave, 0) devuelve el valor actual o 0 si la clave no existe.
        # Esto permite incrementar el contador de forma segura.
        conteo_casas[heroe.casa_comic] = conteo_casas.get(heroe.casa_comic, 0) + 1
    
    # Se itera sobre el diccionario de conteo para mostrar los resultados.
    for casa, cantidad in conteo_casas.items():
        print(f"{casa}: {cantidad} superhéroes")

# --- PUNTO DE ENTRADA DEL SCRIPT ---
# Este bloque se ejecuta solo si el archivo es el programa principal.
if __name__ == "__main__":
    # 1. Se crea una instancia vacía de tu clase List.
    lista_superheroes = List()

    # 2. Se definen y añaden los criterios de ordenación/búsqueda.
    #    Estos criterios son funciones que le dicen a la lista cómo acceder
    #    a los atributos de los objetos para ordenar o buscar.
    def by_name(hero):
        return hero.nombre

    lista_superheroes.add_criterion('nombre', by_name)

    # 3. Se cargan los datos desde la lista de diccionarios `superheroes`.
    for data in superheroes:
        # Se asigna una casa de cómic por defecto.
        # Se hace una excepción para que el punto C (cambiar casa) tenga sentido práctico.
        casa = "Marvel"
        if data["name"] == "Dr Strange":
            casa = "DC"

        # Se crea un objeto Superhero y se añade a la lista.
        lista_superheroes.append(Superhero(
            nombre=data["name"],
            anio_aparicion=data["first_appearance"],
            casa_comic=casa,
            biografia=data["short_bio"]
        ))

    # 4. Se ejecutan todas las funciones de los puntos del ejercicio en orden.
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
