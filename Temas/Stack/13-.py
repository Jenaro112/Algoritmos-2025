"""
Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Universe (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver las siguientes actividades:
a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas, además mostrar el nombre de dichas películas;
b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
c. eliminar los modelos de los trajes destruidos mostrando su nombre;
d. un modelo de traje puede usarse en más de una película y en una película se pueden usar más de un modelo de traje, estos deben cargarse por separado;
e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos repetidos en una misma película;
f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y “Capitan America: Civil War”.
"""

from stack import Stack
from MiLibreria import imprimir_titulo, imprimir_subtitulo, imprimir_mensaje

# Diccionario de trajes
trajes_ironman = [
    {"modelo": "Mark III", "pelicula": "Iron Man", "estado": "Dañado"},
    {"modelo": "Mark IV", "pelicula": "Iron Man 2", "estado": "Impecable"},
    {"modelo": "Mark V", "pelicula": "Iron Man 2", "estado": "Dañado"},
    {"modelo": "Mark VI", "pelicula": "The Avengers", "estado": "Destruido"},
    {"modelo": "Mark VII", "pelicula": "The Avengers", "estado": "Impecable"},
    {"modelo": "Mark XLII", "pelicula": "Iron Man 3", "estado": "Destruido"},
    {"modelo": "Mark XLIV", "pelicula": "Avengers: Age of Ultron", "estado": "Dañado"},  # Hulkbuster
    {"modelo": "Mark XLVI", "pelicula": "Captain America: Civil War", "estado": "Dañado"},
    {"modelo": "Mark XLVII", "pelicula": "Spider-Man: Homecoming", "estado": "Impecable"},
    {"modelo": "Mark L", "pelicula": "Avengers: Infinity War", "estado": "Destruido"},
]

# Cargar la pila
pila_trajes = Stack()
for traje in trajes_ironman:
    pila_trajes.push(traje)

# (a) Buscar Hulkbuster (Mark XLIV)
def buscar_hulkbuster(pila: Stack):
    aux = Stack()
    peliculas = []
    while pila.size() > 0:
        traje = pila.pop()
        if traje["modelo"] == "Mark XLIV":
            peliculas.append(traje["pelicula"])
        aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())
    if peliculas:
        print(f"El modelo Mark XLIV (Hulkbuster) fue usado en: {peliculas}")
    else:
        print("El modelo Mark XLIV (Hulkbuster) no fue encontrado.")

# (b) Mostrar modelos dañados
def mostrar_danados(pila: Stack):
    aux = Stack()
    while pila.size() > 0:
        traje = pila.pop()
        if traje["estado"] == "Dañado":
            print(f'  - {traje["modelo"]} en {traje["pelicula"]}')
        aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())

# (c) Eliminar modelos destruidos
def eliminar_destruidos(pila: Stack):
    aux = Stack()
    while pila.size() > 0:
        traje = pila.pop()
        if traje["estado"] == "Destruido":
            print(f"Eliminado: {traje['modelo']} de la película '{traje['pelicula']}'", "info")
        else:
            aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())

# (e) Agregar Mark LXXXV si no existe en Endgame
def agregar_mark_85(pila: Stack):
    nuevo_traje = {
        "modelo": "Mark LXXXV",
        "pelicula": "Avengers: Endgame",
        "estado": "Dañado"
    }
    aux = Stack()
    existe = False
    while pila.size() > 0:
        traje = pila.pop()
        if traje["modelo"] == nuevo_traje["modelo"] and traje["pelicula"] == nuevo_traje["pelicula"]:
            existe = True
        aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())
    if not existe:
        pila.push(nuevo_traje)
        print("Se agregó el modelo Mark LXXXV a la pila.", "exito")
    else:
        print("El modelo Mark LXXXV para 'Avengers: Endgame' ya existe.", "alerta")

# (f) Mostrar trajes de Homecoming y Civil War
def mostrar_trajes_peliculas(pila: Stack):
    aux = Stack()
    while pila.size() > 0:
        traje = pila.pop()
        if traje["pelicula"] in ["Spider-Man: Homecoming", "Captain America: Civil War"]:
            print(f'  - {traje["modelo"]} en {traje["pelicula"]}')
        aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())

def main():
    imprimir_titulo("ejercicio 13")

    imprimir_subtitulo("a. Búsqueda del modelo Mark XLIV (Hulkbuster)")
    buscar_hulkbuster(pila_trajes)

    imprimir_subtitulo("b. Modelos con estado 'Dañado'")
    mostrar_danados(pila_trajes)

    imprimir_subtitulo("c. Eliminación de modelos 'Destruidos'")
    eliminar_destruidos(pila_trajes)

    imprimir_subtitulo("e. Agregar modelo Mark LXXXV")
    agregar_mark_85(pila_trajes)

    imprimir_subtitulo("f. Trajes de 'Spider-Man: Homecoming' y 'Civil War'")
    mostrar_trajes_peliculas(pila_trajes)

if __name__ == "__main__":
    main()
