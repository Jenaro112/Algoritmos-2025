"""
10. Se dispone de una lista de canciones de Spotify, de las cuales se sabe su nombre, banda o artista, duración y cantidad de reproducciones durante el último mes. Desarrollar un algoritmo que permita realizar las siguientes actividades:
-   a. obtener la información de la canción más larga;
-   b. obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas;
-   c. obtener todas las canciones de la banda Arctic Monkeys;
-   d. mostrar los nombres de las bandas o artistas que solo son de una palabra.
"""

from list_ import List


class Cancion:
    def __init__(self, nombre, banda, duracion, reproducciones):
        self.nombre = nombre
        self.banda = banda
        self.duracion = duracion  # en segundos
        self.reproducciones = reproducciones

    def __str__(self):
        return f"{self.nombre} - {self.banda} ({self.duracion}s, {self.reproducciones} reproducciones)"

def order_by_duracion(item):
    return item.duracion

def order_by_reproducciones(item):
    return item.reproducciones

# Lista de canciones como objetos
lista_canciones = List([
    Cancion("Mi Nena", "Walls", 120, 851617),
    Cancion("CONTANDO OVEJAS", "Wos", 180, 58000000),
    Cancion("Vida de Rock", "Duki", 200, 12000000),
    Cancion("Let Down", "Radiohead", 300, 250000000),
    Cancion("Cuchillos Guantanamera", "Airbag", 220, 4500000),
    Cancion("Mardy Bum", "Arctic Monkeys", 250, 50000000),
])

def cancion_mas_larga():
    lista_canciones.add_criterion('duracion', order_by_duracion)
    lista_canciones.sort_by_criterion('duracion')
    cancion_larga = lista_canciones[-1]
    print("--- Canción más larga: ---")
    print(f"La canción más larga es: {cancion_larga.nombre} de {cancion_larga.banda} con una duración de {cancion_larga.duracion} segundos.")

def top_canciones():
    lista_canciones.add_criterion('reproducciones', order_by_reproducciones)
    lista_canciones.sort_by_criterion('reproducciones')  # ordena de mayor a menor
    print("--- TOP 5 Canciones más escuchadas: ---")
    for cancion in lista_canciones[-1:-6:-1]:
        print(f"-   {cancion.nombre}")

def Arctic_Monkeys():
    arctic_songs = List([cancion for cancion in lista_canciones if cancion.banda == "Arctic Monkeys"])
    print("--- Canciones de Arctic Monkeys ---")
    arctic_songs.show()

def bandas():
    bandas_unicas = List(set(cancion.banda for cancion in lista_canciones if ' ' not in cancion.banda))
    print("--- Bandas o artistas de una sola palabra: ---")
    for banda in bandas_unicas:
        print("- " + banda)


print("-" * 50)
cancion_mas_larga()
top_canciones()
Arctic_Monkeys()
bandas()
print("-" * 50)
