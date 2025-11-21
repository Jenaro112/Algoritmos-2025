""" 
------------------------------
|       Trabajo N° 22        |
------------------------------
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

# --- IMPORTACIONES DE LIBRERÍAS ---
# Importamos la clase List de tu librería `list_.py` y las funciones de estilo de `MiLibreria`.
from list_ import List
from MiLibreria import imprimir_titulo, imprimir_subtitulo, imprimir_mensaje, imprimir_separador

# --- DEFINICIÓN DE LA CLASE JEDI ---
class Jedi:
    """
    Representa a un Jedi con sus atributos principales.
    Esta clase sirve como un molde para crear los objetos que se almacenarán en la lista.
    """
    def __init__(self, nombre, especie, maestros, colores_sable):
        # El constructor inicializa un nuevo objeto Jedi con los datos proporcionados.
        self.nombre = nombre
        self.especie = especie
        self.maestros = maestros
        self.colores_sable = colores_sable

    def __str__(self):
        # El método __str__ define cómo se debe imprimir un objeto Jedi.
        # Es útil para mostrar la información completa de un personaje de forma legible.
        maestros_str = ", ".join(self.maestros) if self.maestros else "Ninguno"
        sables_str = ", ".join(self.colores_sable)
        return (f"Nombre: {self.nombre} | Especie: {self.especie} | "
                f"Maestros: {maestros_str} | Sables: {sables_str}")

# --- DATOS INICIALES ---
# Lista de diccionarios que contiene la información de cada Jedi.
# Esta será la fuente de datos para cargar en nuestra lista de objetos.
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

# --- DEFINICIÓN DE FUNCIONES PARA CADA PUNTO DEL EJERCICIO ---

def Punto_A(lista):
    """a. Realiza un listado ordenado por nombre y luego por especie."""
    imprimir_subtitulo("a. Listado ordenado por Nombre y Especie")
    print("Ordenado por Nombre:")
    # Se utiliza el método `sort_by_criterion` para ordenar la lista alfabéticamente por el nombre del Jedi.
    lista.sort_by_criterion('nombre')
    for jedi in lista:
        print(f"  - {jedi.nombre}")
    
    print("\nOrdenado por Especie:")
    # Se vuelve a ordenar la lista, esta vez por el criterio de especie.
    lista.sort_by_criterion('especie')
    for jedi in lista:
        print(f"  - {jedi.nombre} ({jedi.especie})")

def Punto_B(lista):
    """b. Muestra toda la información de Ahsoka Tano y Kit Fisto."""
    imprimir_subtitulo("b. Información de Ahsoka Tano y Kit Fisto")
    # Se itera sobre una lista con los nombres de los Jedi a buscar.
    for nombre_jedi in ["Ahsoka Tano", "Kit Fisto"]:
        # Se usa el método `search` para encontrar el índice del Jedi en la lista.
        index = lista.search(nombre_jedi, 'nombre')
        # Si se encuentra (el índice no es None)...
        if index is not None:
            # ...se imprime el objeto Jedi directamente, lo que invoca su método __str__.
            print(lista[index])
        else:
            # Si no se encuentra, se informa al usuario.
            imprimir_mensaje(f"{nombre_jedi} no encontrado.", "alerta")

def Punto_C(lista):
    """c. Muestra todos los padawans (aprendices) de Yoda y Luke Skywalker."""
    imprimir_subtitulo("c. Padawans de Yoda y Luke Skywalker")
    # Se recorre toda la lista de Jedi.
    for jedi in lista:
        # Se comprueba si "Yoda" o "Luke Skywalker" están en la lista de maestros de cada Jedi.
        if "Yoda" in jedi.maestros or "Luke Skywalker" in jedi.maestros:
            print(f"- {jedi.nombre}")

def Punto_D(lista):
    """d. Muestra los Jedi que son de especie Humana o Twi'lek."""
    imprimir_subtitulo("d. Jedi de especie Humana y Twi'lek")
    for jedi in lista:
        # Se comprueba si la especie del Jedi está en la lista de especies buscadas.
        if jedi.especie in ["Humano", "Twi'lek"]:
            print(f"- {jedi.nombre} ({jedi.especie})")

def Punto_E(lista):
    """e. Lista todos los Jedi cuyo nombre comienza con la letra 'A'."""
    imprimir_subtitulo("e. Jedi que comienzan con 'A'")
    for jedi in lista:
        # El método `startswith` comprueba si el string (nombre) comienza con el prefijo dado.
        if jedi.nombre.startswith('A'):
            print(f"- {jedi.nombre}")

def Punto_F(lista):
    """f. Muestra los Jedi que usaron sables de luz de más de un color."""
    imprimir_subtitulo("f. Jedi que usaron más de un color de sable")
    for jedi in lista:
        # Se comprueba si la longitud de la lista de colores de sable es mayor que 1.
        if len(jedi.colores_sable) > 1:
            print(f"- {jedi.nombre} (Colores: {', '.join(jedi.colores_sable)})")

def Punto_G(lista):
    """g. Indica los Jedi que utilizaron sable de luz de color amarillo o violeta."""
    imprimir_subtitulo("g. Jedi que usaron sable amarillo o violeta")
    for jedi in lista:
        # Se comprueba si alguno de los colores buscados está en la lista de colores del Jedi.
        if "amarillo" in jedi.colores_sable or "violeta" in jedi.colores_sable:
            print(f"- {jedi.nombre}")

def Punto_H(lista):
    """h. Indica los nombres de los padawans de Qui-Gon Jinn y Mace Windu."""
    imprimir_subtitulo("h. Padawans de Qui-Gon Jinn y Mace Windu")
    # Se usa una bandera para saber si se encontró al menos un padawan.
    padawans_encontrados = False
    for jedi in lista:
        # Se comprueba si alguno de los dos maestros está en la lista de maestros del Jedi.
        if "Qui-Gon Jinn" in jedi.maestros or "Mace Windu" in jedi.maestros:
            print(f"- {jedi.nombre} (Maestro: {', '.join(jedi.maestros)})")
            padawans_encontrados = True
    # Si después de recorrer toda la lista no se encontró ninguno, se informa al usuario.
    if not padawans_encontrados:
        imprimir_mensaje("No se encontraron padawans para Qui-Gon Jinn o Mace Windu en la lista.", "info")


# --- PUNTO DE ENTRADA DEL SCRIPT ---
# Este bloque se ejecuta solo si el archivo es el programa principal.
if __name__ == "__main__":
    # 1. Se crea una instancia vacía de tu clase List.
    lista_jedi = List()

    # 2. Se definen y añaden los criterios de ordenación/búsqueda.
    #    Estas funciones le dicen a la lista cómo acceder a los atributos de los objetos
    #    para poder ordenar o buscar por ellos.
    def by_name(jedi):
        return jedi.nombre

    def by_species(jedi):
        return jedi.especie

    lista_jedi.add_criterion('nombre', by_name)
    lista_jedi.add_criterion('especie', by_species)

    # 3. Se cargan los datos. Se itera sobre la lista de diccionarios `jedi_data`.
    for data in jedi_data:
        lista_jedi.append(Jedi(
            nombre=data["nombre"],
            especie=data["especie"],
            maestros=data["maestros"],
            colores_sable=data["colores_sable"]
        ))

    # 4. Se define una función `main` para orquestar la ejecución de todos los puntos.
    def main():
        imprimir_titulo("Análisis de la Orden Jedi")
        Punto_A(lista_jedi)
        imprimir_separador()
        Punto_B(lista_jedi)
        imprimir_separador()
        Punto_C(lista_jedi)
        imprimir_separador()
        Punto_D(lista_jedi)
        imprimir_separador()
        Punto_E(lista_jedi)
        imprimir_separador()
        Punto_F(lista_jedi)
        imprimir_separador()
        Punto_G(lista_jedi)
        imprimir_separador()
        Punto_H(lista_jedi)
    main()
