from queue import Queue
from datetime import datetime
from colorama import init, Fore, Back, Style # librería para colores

init(autoreset=True)
subrayado = '\033[4m'

"""
Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje, resolver las siguientes actividades:

a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra Python, sin perder datos en la cola;
c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.
"""

def eliminar_notificaciones_facebook(cola):
    tamaño = cola.qsize()
    for _ in range(tamaño):
        notificacion = cola.get()
        if notificacion['aplicacion'] != 'Facebook':
            cola.put(notificacion)

def mostrar_notificaciones_twitter_python(cola):
    tamaño = cola.qsize()
    for _ in range(tamaño):
        notificacion = cola.get()
        if notificacion['aplicacion'] == 'Twitter' and 'Python' in notificacion['mensaje']:
            print(f"{Fore.GREEN}[{notificacion['hora']}] {Fore.CYAN}{subrayado}{notificacion['mensaje']}{Style.RESET_ALL}")
        cola.put(notificacion)

def almacenar_notificaciones_rango_horario(cola):
    pila = []
    tamaño = cola.qsize()
    contador = 0
    for _ in range(tamaño):
        notificacion = cola.get()
        hora = datetime.strptime(notificacion['hora'], '%H:%M')
        if datetime.strptime('11:43', '%H:%M') <= hora <= datetime.strptime('15:57', '%H:%M'):
            pila.append(notificacion)
            contador += 1
        cola.put(notificacion)
    return pila, contador

def imprimir_notificaciones(cola, titulo):
    print(f"{Fore.YELLOW}{titulo}{Style.RESET_ALL}")
    print("-" * 50)
    for notificacion in cola.queue:
        print(f"{Fore.LIGHTWHITE_EX}[{notificacion['hora']}] {Fore.LIGHTMAGENTA_EX}{notificacion['aplicacion']}: {Fore.LIGHTCYAN_EX}{notificacion['mensaje']}{Style.RESET_ALL}")
    print("-" * 50)

cola_notificaciones = Queue()
cola_notificaciones.put({'hora': '11:45', 'aplicacion': 'Facebook', 'mensaje': 'Nueva foto etiquetada'})
cola_notificaciones.put({'hora': '12:30', 'aplicacion': 'Twitter', 'mensaje': 'Aprendiendo Python es divertido'})
cola_notificaciones.put({'hora': '14:00', 'aplicacion': 'Instagram', 'mensaje': 'Nueva historia publicada'})
cola_notificaciones.put({'hora': '16:00', 'aplicacion': 'Twitter', 'mensaje': 'Python es increíble'})

imprimir_notificaciones(cola_notificaciones, "Lista de notificaciones:")

eliminar_notificaciones_facebook(cola_notificaciones)

imprimir_notificaciones(cola_notificaciones, "Lista de notificaciones sin Facebook:")

print(f"{Fore.CYAN}Notificaciones de Twitter con {subrayado}Python{Style.RESET_ALL}:")
mostrar_notificaciones_twitter_python(cola_notificaciones)

pila, cantidad = almacenar_notificaciones_rango_horario(cola_notificaciones)
print("-" * 50)
print(f"Cantidad de notificaciones entre 11:43 y 15:57: {cantidad}")
print("Notificaciones en la pila:")
for notif in pila:
    print(f"{Fore.MAGENTA}[{notif['hora']}] {notif['aplicacion']}: {notif['mensaje']}{Style.RESET_ALL}")