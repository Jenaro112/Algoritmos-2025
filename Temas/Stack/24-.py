"""
Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y la cantidad de películas de la saga en la que participó,implementar las funciones necesarias para resolver las siguientes actividades:

a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
"""

# --- IMPORTACIONES DE LIBRERÍAS ---
# Importamos la clase Stack de tu librería `stack.py` y las funciones de estilo de `MiLibreria`.
from stack import Stack
from MiLibreria import imprimir_titulo, imprimir_subtitulo, imprimir_mensaje

# --- DATOS INICIALES ---
# Lista de diccionarios que contiene la información de cada personaje de MCU.
# Cada diccionario representa un personaje y sus atributos.
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

# --- CREACIÓN Y CARGA DE LA PILA ---
# 1. Se crea una instancia vacía de tu clase Stack.
pila_personajes = Stack()
# 2. Se itera sobre la lista de diccionarios `personajes_mcu`.
for personaje in personajes_mcu:
    # 3. Cada diccionario (personaje) se agrega a la cima de la pila.
    pila_personajes.push(personaje)

# --- DEFINICIÓN DE FUNCIONES PARA CADA PUNTO DEL EJERCICIO ---

def posicion_personajes(pila: Stack, nombres: list):
    """a. Determina en qué posición se encuentran los personajes cuyos nombres están en la lista `nombres`."""
    # Se crea una pila auxiliar para no perder los datos de la pila original.
    aux = Stack()
    # Se usa un diccionario para almacenar las posiciones encontradas.
    posiciones = {}
    # Se inicializa un contador para la posición, empezando en 1 (la cima).
    pos = 1
    # Se recorre la pila principal hasta que esté vacía.
    while pila.size() > 0:
        # Se saca el personaje de la cima.
        personaje = pila.pop()
        # Si el nombre del personaje está en la lista de nombres que buscamos...
        if personaje["nombre"] in nombres:
            # ...se guarda su nombre y posición en el diccionario.
            posiciones[personaje["nombre"]] = pos
        # Se guarda el personaje en la pila auxiliar para no perderlo.
        aux.push(personaje)
        # Se incrementa el contador de posición.
        pos += 1
    # Se restaura la pila original moviendo los elementos desde la pila auxiliar.
    while aux.size() > 0:
        pila.push(aux.pop())
    
    # Se muestran los resultados encontrados.
    for nombre in nombres:
        if nombre in posiciones:
            imprimir_mensaje(f"{nombre} está en la posición {posiciones[nombre]}.", "info")
        else:
            imprimir_mensaje(f"{nombre} no se encontró en la pila.", "alerta")

def personajes_mas_de_cinco(pila: Stack):
    """b. Determina y muestra los personajes que participaron en más de 5 películas."""
    # Se utiliza una pila auxiliar para un recorrido no destructivo.
    aux = Stack()
    # Se recorre la pila principal.
    while pila.size() > 0:
        personaje = pila.pop()
        # Si el personaje tiene más de 5 películas, se muestra su información.
        if personaje["peliculas"] > 5:
            print(f"  - {personaje['nombre']}: {personaje['peliculas']} películas")
        # Siempre se guarda el personaje en la pila auxiliar.
        aux.push(personaje)
    # Se restaura la pila original.
    while aux.size() > 0:
        pila.push(aux.pop())

def peliculas_black_widow(pila: Stack):
    """c. Determina en cuántas películas participó Black Widow."""
    # Pila auxiliar para recorrido no destructivo.
    aux = Stack()
    # Variable para almacenar la cantidad de películas.
    cantidad = None
    # Se recorre la pila principal.
    while pila.size() > 0:
        personaje = pila.pop()
        # Si se encuentra a Black Widow...
        if personaje["nombre"] == "Black Widow":
            # ...se guarda la cantidad de películas.
            cantidad = personaje["peliculas"]
        # Se guarda el personaje en la pila auxiliar.
        aux.push(personaje)
    # Se restaura la pila original.
    while aux.size() > 0:
        pila.push(aux.pop())
    
    # Se muestra el resultado.
    if cantidad is not None:
        imprimir_mensaje(f"Black Widow participó en {cantidad} películas.", "info")
    else:
        imprimir_mensaje("Black Widow no se encontró en la pila.", "alerta")

def personajes_letras_especificas(pila: Stack):
    """d. Muestra todos los personajes cuyos nombres comienzan con C, D o G."""
    # Pila auxiliar para recorrido no destructivo.
    aux = Stack()
    # Tupla con las letras iniciales a buscar.
    letras = ('C', 'D', 'G')
    # Se recorre la pila principal.
    while pila.size() > 0:
        personaje = pila.pop()
        # El método `startswith` puede recibir una tupla de prefijos.
        if personaje["nombre"].startswith(letras):
            print(f"  - {personaje['nombre']}")
        aux.push(personaje)
    # Se restaura la pila original.
    while aux.size() > 0:
        pila.push(aux.pop())

# --- FUNCIÓN PRINCIPAL ---
def main():
    """Función principal que orquesta la ejecución de todos los puntos del ejercicio."""
    imprimir_titulo("Análisis de Personajes de MCU")
    imprimir_subtitulo("a. Posición de Rocket Raccoon y Groot")
    posicion_personajes(pila_personajes, ["Rocket Raccoon", "Groot"])
    imprimir_subtitulo("b. Personajes con más de 5 películas")
    personajes_mas_de_cinco(pila_personajes)
    imprimir_subtitulo("c. Películas de Black Widow")
    peliculas_black_widow(pila_personajes)
    imprimir_subtitulo("d. Personajes que comienzan con C, D o G")
    personajes_letras_especificas(pila_personajes)

# --- PUNTO DE ENTRADA DEL SCRIPT ---
# Este bloque de código se ejecuta solo si este archivo es el programa principal.
if __name__ == "__main__":
    main()
