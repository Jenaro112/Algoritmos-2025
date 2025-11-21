"""
Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje, resolver las siguientes actividades:

a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra Python, sin perder datos en la cola;
c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.
"""

from queue_ import Queue
from stack_ import Stack
from MiLibreria import imprimir_titulo, imprimir_subtitulo, imprimir_mensaje, imprimir_separador

# --- Carga Inicial de Datos ---
cola_notificaciones = Queue()
cola_notificaciones.arrive({'hora': '10:30', 'aplicacion': 'Twitter', 'mensaje': '¿Viste este hilo sobre Python?'})
cola_notificaciones.arrive({'hora': '11:45', 'aplicacion': 'Facebook', 'mensaje': 'Nueva foto etiquetada'})
cola_notificaciones.arrive({'hora': '12:30', 'aplicacion': 'Twitter', 'mensaje': 'Aprendiendo Python es divertido'})
cola_notificaciones.arrive({'hora': '14:00', 'aplicacion': 'Instagram', 'mensaje': 'Nueva historia publicada'})
cola_notificaciones.arrive({'hora': '15:57', 'aplicacion': 'Facebook', 'mensaje': 'Recordatorio de cumpleaños'})
cola_notificaciones.arrive({'hora': '16:00', 'aplicacion': 'Twitter', 'mensaje': 'Python es increíble'})

def Punto_A(cola):
    """a. Elimina de la cola todas las notificaciones de Facebook."""
    tamaño_original = cola.size()
    for _ in range(tamaño_original):
        notificacion = cola.attention()
        if notificacion['aplicacion'] != 'Facebook':
            cola.arrive(notificacion)
    imprimir_mensaje("Notificaciones de Facebook eliminadas.", "exito")

def Punto_B(cola):
    """b. Muestra notificaciones de Twitter que incluyen 'Python'."""
    tamaño = cola.size()
    for _ in range(tamaño):
        notificacion = cola.attention()
        if notificacion['aplicacion'] == 'Twitter' and 'Python' in notificacion['mensaje']:
            print(f"  - [{notificacion['hora']}] {notificacion['mensaje']}")
        cola.arrive(notificacion)

def Punto_C(cola):
    """c. Almacena en una pila notificaciones entre 11:43 y 15:57."""
    pila_temporal = Stack()
    tamaño = cola.size()
    
    for _ in range(tamaño):
        notificacion = cola.attention()
        # Comparamos las horas como strings, funciona para el formato HH:MM
        if '11:43' <= notificacion['hora'] <= '15:57':
            pila_temporal.push(notificacion)
        cola.arrive(notificacion)
    
    imprimir_mensaje(f"Se almacenaron {pila_temporal.size()} notificaciones en la pila temporal.", "info")
    print("   Contenido de la pila (de más reciente a más antigua):")
    pila_temporal.show()

def main():
    imprimir_titulo("Gestor de Notificaciones")

    imprimir_subtitulo("Cola de notificaciones original")
    cola_notificaciones.show()
    imprimir_separador()

    imprimir_subtitulo("a. Eliminando notificaciones de Facebook")
    Punto_A(cola_notificaciones)
    imprimir_separador()

    imprimir_subtitulo("b. Notificaciones de Twitter con la palabra 'Python'")
    Punto_B(cola_notificaciones)
    imprimir_separador()

    imprimir_subtitulo("c. Notificaciones entre 11:43 y 15:57")
    Punto_C(cola_notificaciones)
    imprimir_separador()

if __name__ == "__main__":
    main()