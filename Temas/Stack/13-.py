"""
Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Universe (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver las siguientes actividades:
a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas, además mostrar el nombre de dichas películas;
b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
c. eliminar los modelos de los trajes destruidos mostrando su nombre;
d. un modelo de traje puede usarse en más de una película y en una película se pueden usar más de un modelo de traje, estos deben cargarse por separado;
e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos repetidos en una misma película;
f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y “Capitan America: Civil War”.
"""

# --- IMPORTACIONES DE LIBRERÍAS ---
# Importamos la clase Stack de tu librería `stack.py` y las funciones de estilo de `MiLibreria`.
from stack import Stack
from MiLibreria import imprimir_titulo, imprimir_subtitulo, imprimir_mensaje

# --- DATOS INICIALES ---
# Lista de diccionarios que contiene la información de cada traje de Iron Man.
# Cada diccionario representa un traje y sus atributos.
trajes_ironman = [
    {"modelo": "Mark III", "pelicula": "Iron Man", "estado": "Dañado"},
    {"modelo": "Mark IV", "pelicula": "Iron Man 2", "estado": "Impecable"},
    {"modelo": "Mark V", "pelicula": "Iron Man 2", "estado": "Dañado"},
    {"modelo": "Mark VI", "pelicula": "The Avengers", "estado": "Destruido"},
    {"modelo": "Mark VII", "pelicula": "The Avengers", "estado": "Impecable"},
    {"modelo": "Mark XLII", "pelicula": "Iron Man 3", "estado": "Destruido"},
    {"modelo": "Mark XLIV", "pelicula": "Avengers: Age of Ultron", "estado": "Dañado"},
    {"modelo": "Mark XLVI", "pelicula": "Captain America: Civil War", "estado": "Dañado"},
    {"modelo": "Mark XLVII", "pelicula": "Spider-Man: Homecoming", "estado": "Impecable"},
    {"modelo": "Mark L", "pelicula": "Avengers: Infinity War", "estado": "Destruido"},
]

# --- CREACIÓN Y CARGA DE LA PILA ---
# 1. Se crea una instancia vacía de tu clase Stack.
pila_trajes = Stack()
# 2. Se itera sobre la lista de diccionarios `trajes_ironman`.
for traje in trajes_ironman:
    # 3. Cada diccionario (traje) se agrega a la cima de la pila.
    pila_trajes.push(traje)

# --- DEFINICIÓN DE FUNCIONES PARA CADA PUNTO DEL EJERCICIO ---

def buscar_hulkbuster(pila: Stack):
    """a. Determina si el modelo Mark XLIV (Hulkbuster) fue utilizado y en qué películas."""
    # Se crea una pila auxiliar para no perder los datos de la pila original.
    aux = Stack()
    # Se crea una lista para almacenar los nombres de las películas donde aparece.
    peliculas = []
    # Se recorre la pila principal. El bucle se detiene cuando la pila está vacía.
    while pila.size() > 0:
        # Se saca el elemento de la cima de la pila.
        traje = pila.pop()
        # Se comprueba si el modelo es el "Mark XLIV".
        if traje["modelo"] == "Mark XLIV":
            # Si coincide, se añade la película a la lista de resultados.
            peliculas.append(traje["pelicula"])
        # Se guarda el traje en la pila auxiliar para no perderlo.
        aux.push(traje)
    # Una vez que la pila original está vacía, se restaura.
    # Se sacan todos los elementos de la pila auxiliar y se vuelven a meter en la original.
    while aux.size() > 0:
        pila.push(aux.pop())
    
    # Se muestra el resultado al usuario.
    if peliculas:
        imprimir_mensaje(f"El modelo Mark XLIV (Hulkbuster) fue usado en: {peliculas}", "exito")
    else:
        imprimir_mensaje("El modelo Mark XLIV (Hulkbuster) no fue encontrado.", "alerta")

def mostrar_danados(pila: Stack):
    """b. Muestra los modelos que quedaron dañados, sin perder datos de la pila."""
    # Se utiliza una pila auxiliar para conservar los datos.
    aux = Stack()
    # Se recorre la pila principal.
    while pila.size() > 0:
        traje = pila.pop()
        # Si el estado del traje es "Dañado", se muestra su información.
        if traje["estado"] == "Dañado":
            print(f'  - {traje["modelo"]} en {traje["pelicula"]}')
        # Siempre se guarda el traje en la pila auxiliar.
        aux.push(traje)
    # Se restaura la pila original.
    while aux.size() > 0:
        pila.push(aux.pop())

def eliminar_destruidos(pila: Stack):
    """c. Elimina de la pila los modelos de trajes que quedaron 'Destruido'."""
    # Se usa una pila auxiliar para guardar solo los trajes que NO se van a eliminar.
    aux = Stack()
    # Se recorre la pila principal.
    while pila.size() > 0:
        traje = pila.pop()
        # Se comprueba el estado del traje.
        if traje["estado"] == "Destruido":
            # Si está "Destruido", se informa que se elimina y NO se guarda en la pila auxiliar.
            print(f"Eliminado: {traje['modelo']} de la película '{traje['pelicula']}'", "info")
        else:
            # Si no está destruido, se guarda en la pila auxiliar.
            aux.push(traje)
    # Al final, la pila auxiliar solo contiene los trajes "Dañado" e "Impecable".
    # Se restaura la pila original con el contenido de la pila auxiliar.
    while aux.size() > 0:
        pila.push(aux.pop())

def agregar_mark_85(pila: Stack):
    """e. Agrega el modelo Mark LXXXV si no existe ya para la película 'Avengers: Endgame'."""
    # Se define el diccionario del nuevo traje a agregar.
    nuevo_traje = {
        "modelo": "Mark LXXXV",
        "pelicula": "Avengers: Endgame",
        "estado": "Dañado"
    }
    # Se usa una pila auxiliar para el recorrido no destructivo.
    aux = Stack()
    # Se usa una bandera para saber si el traje ya existe.
    existe = False
    # Se recorre la pila principal.
    while pila.size() > 0:
        traje = pila.pop()
        # Se comprueba si el modelo y la película coinciden con el que queremos agregar.
        if traje["modelo"] == nuevo_traje["modelo"] and traje["pelicula"] == nuevo_traje["pelicula"]:
            # Si coincide, marcamos que ya existe.
            existe = True
        aux.push(traje)
    # Se restaura la pila original.
    while aux.size() > 0:
        pila.push(aux.pop())
    
    # Después de restaurar, se comprueba la bandera.
    if not existe:
        # Si no existía, se agrega el nuevo traje a la pila.
        pila.push(nuevo_traje)
        imprimir_mensaje("Se agregó el modelo Mark LXXXV a la pila.", "exito")
    else:
        imprimir_mensaje("El modelo Mark LXXXV para 'Avengers: Endgame' ya existe.", "alerta")

def mostrar_trajes_peliculas(pila: Stack):
    """f. Muestra los nombres de los trajes usados en películas específicas."""
    # Pila auxiliar para recorrido no destructivo.
    aux = Stack()
    # Se recorre la pila principal.
    while pila.size() > 0:
        traje = pila.pop()
        # Se comprueba si la película del traje está en nuestra lista de interés.
        if traje["pelicula"] in ["Spider-Man: Homecoming", "Captain America: Civil War"]:
            print(f'  - {traje["modelo"]} en {traje["pelicula"]}')
        aux.push(traje)
    # Se restaura la pila original.
    while aux.size() > 0:
        pila.push(aux.pop())

# --- FUNCIÓN PRINCIPAL ---
def main():
    """Función principal que orquesta la ejecución de todos los puntos del ejercicio."""
    imprimir_titulo("Análisis de Trajes de Iron Man")

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

# --- PUNTO DE ENTRADA DEL SCRIPT ---
# Este bloque de código se ejecuta solo si este archivo es el programa principal.
if __name__ == "__main__":
    main()
