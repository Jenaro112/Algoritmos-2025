""" 
*Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
*-   a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
*-   b. mostrar los nombre de los superhéroes femeninos;
*-  c. mostrar los nombres de los personajes masculinos;
*-  d. determinar el nombre del superhéroe del personaje Scott Lang;
*-  e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
*-  f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.
"""

from queue_ import Queue
from MiLibreria import imprimir_titulo, imprimir_subtitulo, imprimir_mensaje, imprimir_separador
MCU = Queue()
MCU.arrive({"nombre": "Tony Stark", "superheroe": "Iron" , "genero": "M"})
MCU.arrive({"nombre": "Steve Rogers", "superheroe": "Capitan America" , "genero": "M"})
MCU.arrive({"nombre": "Natasha Romanoff", "superheroe": "Black Widow" , "genero": "F"})
MCU.arrive({"nombre": "Carol Danvers", "superheroe": "Capitana Marvel" , "genero": "F"})
MCU.arrive({"nombre": "Scott Lang", "superheroe": "Ant-Man" , "genero": "M"})
MCU.arrive({"nombre": "Wanda Maximoff", "superheroe": "Scarlet Witch" , "genero": "F"})

def Punto_A(cola: Queue):
    tamaño = cola.size() 
    for _ in range(tamaño):
        superheroe = cola.attention()
        if superheroe["superheroe"] == "Capitana Marvel":
            imprimir_mensaje(f"El nombre del personaje de la Capitana Marvel es: {superheroe['nombre']}", "exito")
        cola.arrive(superheroe)

def Punto_B(cola: Queue):
    tamaño = cola.size()
    for _ in range(tamaño):
        superheroe = cola.attention()
        if superheroe["genero"] == "F":
            print(f"  - {superheroe['superheroe']}")
        cola.arrive(superheroe)

def Punto_C(cola: Queue):
    tamaño = cola.size()
    for _ in range(tamaño):
        superheroe = cola.attention()
        if superheroe["genero"] == "M":
            print(f"  - {superheroe['nombre']}")
        cola.arrive(superheroe)

def Punto_D(cola: Queue):
    tamaño = cola.size()
    for _ in range(tamaño):
        superheroe = cola.attention()
        if superheroe["nombre"] == "Scott Lang":
            imprimir_mensaje(f"El nombre del superhéroe de Scott Lang es: {superheroe['superheroe']}", "exito")
        cola.arrive(superheroe)

def Punto_E(cola: Queue):
    tamaño = cola.size()
    for _ in range(tamaño):
        superheroe = cola.attention()
        if superheroe["nombre"].startswith("S") or superheroe["superheroe"].startswith("S"):
            print(f"  - Personaje: {superheroe['nombre']}, Superhéroe: {superheroe['superheroe']}")
        cola.arrive(superheroe)

def Punto_F(cola: Queue):
    tamaño = cola.size()
    encontrado = False
    for _ in range(tamaño):
        superheroe = cola.attention()
        if superheroe["nombre"] == "Carol Danvers":
            imprimir_mensaje(f"Carol Danvers está en la cola. Su nombre de superhéroe es: {superheroe['superheroe']}", "exito")
            encontrado = True
        cola.arrive(superheroe)
    if not encontrado:
        imprimir_mensaje("Carol Danvers no se encuentra en la cola.", "alerta")

def main():
    imprimir_titulo("Ejercicio 22")
    imprimir_subtitulo("a. Nombre del personaje de Capitana Marvel")
    Punto_A(MCU)
    imprimir_subtitulo("b. Nombres de superhéroes femeninos")
    Punto_B(MCU)
    imprimir_subtitulo("c. Nombres de personajes masculinos")
    Punto_C(MCU)
    imprimir_subtitulo("d. Nombre de superhéroe de Scott Lang")
    Punto_D(MCU)
    imprimir_subtitulo("e. Personajes/Superhéroes cuyos nombres comienzan con 'S'")
    Punto_E(MCU)
    imprimir_subtitulo("f. Búsqueda de Carol Danvers")
    Punto_F(MCU)
    imprimir_separador()

if __name__ == "__main__":
    main()
