# --- IMPORTACIONES DE LIBRERÍAS ---
# Importamos las librerías necesarias:
# - random: para generar la mochila con objetos aleatorios.
# - time: para simular pausas y hacer la ejecución más visual.
# - colores: tu librería personalizada para dar color a la salida en consola.
import random
import time
import colores

def usar_la_fuerza(mochila:list, contador:int=0):
    """
    Función recursiva que busca un "Sable de luz" en una lista (mochila).
    Simula el proceso de sacar objetos uno por uno hasta encontrarlo o vaciar la mochila.
    
    Args:
        mochila (list): La lista de objetos donde se buscará.
        contador (int): El número de objetos sacados hasta el momento.
    """
    
    # --- CASO BASE 1: Mochila Vacía ---
    # Si la lista `mochila` está vacía, significa que hemos sacado todos los objetos
    # y no hemos encontrado el sable de luz. La recursión termina.
    if not mochila:
        print(colores.color("[x] El sable de luz no se encuentra en la mochila.", colores.ROJO))  
        return -1  # Retorna -1 para indicar que no se encontró.
    
    # Simulación de la búsqueda para hacerla más interactiva.
    print(colores.color("[*] Buscando sable de luz...",colores.CIAN))
    time.sleep(1)
    print(colores.color("[*] concentrando la fuerza...",colores.CIAN))
    time.sleep(2)
    
    # --- PASO RECURSIVO ---
    # Sacamos el último objeto de la mochila. `pop()` modifica la lista original.
    item = mochila.pop()
    
    # --- CASO BASE 2: Objeto Encontrado ---
    # Si el objeto que sacamos es el "Sable de luz", hemos terminado la búsqueda.
    # La recursión se detiene y devolvemos el número total de intentos.
    if item == "Sable de luz":
        print(colores.color(f"¡Lo encontreee! me llevo {contador + 1} intentos!",colores.VERDE))
        return contador + 1
    else:
        # Si no es el sable de luz, informamos qué objeto sacamos.
        print(colores.color(f"[?] Qué es esto...? '{item}'. Mmmm no es el sable",colores.AMARILLO))
        time.sleep(0.5)
    
    # --- LLAMADA RECURSIVA ---
    # Como no encontramos el sable, llamamos a la misma función de nuevo, pero con:
    # - La mochila (que ahora tiene un objeto menos).
    # - El contador incrementado en 1.
    return usar_la_fuerza(mochila, contador + 1)
    

def generar_mochila() -> list:
    """Genera una mochila con 20 objetos aleatorios, con la posibilidad de incluir un sable de luz."""
    # Lista de objetos que pueden aparecer en la mochila.
    posibles_objetos: list = [
        "Holocrón Jedi", "Comunicador galáctico", "Medpac", "Comida racionada",
        "Filtro de agua", "Cable de agarre", "Manta térmica", "Repulsor",
        "Droide de bolsillo", "Sensor de vida", "Mapa estelar", "Cristal Kyber"
    ]
    # Se genera una lista con 20 objetos aleatorios de la lista de posibles objetos.
    mochila = random.choices(posibles_objetos, k=20)

    # Hay un 50% de probabilidad de que el sable de luz esté en la mochila.
    if random.random() < 0.5:
        # Si se cumple, se elige una posición al azar y se reemplaza el objeto por el sable.
        indice = random.randint(0, 19)
        mochila[indice] = "Sable de luz"
    
    return mochila

# --- FUNCIÓN PRINCIPAL ---
def main():
    """Función principal que orquesta la ejecución del programa."""
    # 1. Se genera la mochila con objetos aleatorios.
    mochila = generar_mochila()
    # 2. Se inicia la búsqueda recursiva del sable de luz.
    usar_la_fuerza(mochila, 0)
    
# --- PUNTO DE ENTRADA DEL SCRIPT ---
# Este bloque se ejecuta solo si el archivo es el programa principal.
if __name__ == "__main__":
    main()