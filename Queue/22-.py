""" 
Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
b. mostrar los nombre de los superhéroes femeninos;
c. mostrar los nombres de los personajes masculinos;
d. determinar el nombre del superhéroe del personaje Scott Lang;
e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.
"""

from queue import Queue
from colorama import init, Fore, Style
init(autoreset=True)
subrayado = '\033[4m'

MCU = Queue()
MCU.put({"nombre": "Tony Stark", "superheroe": "Iron" , "genero": "M"})
MCU.put({"nombre": "Steve Rogers", "superheroe": "Capitan America" , "genero": "M"})
MCU.put({"nombre": "Natasha Romanoff", "superheroe": "Black Widow" , "genero": "F"})
MCU.put({"nombre": "Carol Danvers", "superheroe": "Capitana Marvel" , "genero": "F"})
MCU.put({"nombre": "Scott Lang", "superheroe": "Ant-Man" , "genero": "M"})
MCU.put({"nombre": "Wanda Maximoff", "superheroe": "Scarlet Witch" , "genero": "F"})

def nombre_superheroe_captain_marvel(cola: Queue):
    tamaño = cola.qsize()
    for _ in range(tamaño):
        superheroe = cola.get()
        if superheroe["superheroe"] == "Capitana Marvel":
            print(f"{Fore.GREEN}El nombre del personaje de la Capitana Marvel es: {Fore.CYAN}{subrayado}{superheroe['nombre']}{Style.RESET_ALL}")
        cola.put(superheroe)

def superheroes_femeninos(cola: Queue):
    tamaño = cola.qsize()
    print(f"{Fore.YELLOW}Superhéroes femeninos:{Style.RESET_ALL}")
    for _ in range(tamaño):
        superheroe = cola.get()
        if superheroe["genero"] == "F":
            print(f"  - {Fore.CYAN}{superheroe['superheroe']}{Style.RESET_ALL}")
        cola.put(superheroe)

def personajes_masculinos(cola: Queue):
    tamaño = cola.qsize()
    print(f"{Fore.YELLOW}Personajes masculinos:{Style.RESET_ALL}")
    for _ in range(tamaño):
        superheroe = cola.get()
        if superheroe["genero"] == "M":
            print(f"  - {Fore.CYAN}{superheroe['nombre']}{Style.RESET_ALL}")
        cola.put(superheroe)

def scott_lang(cola: Queue):
    tamaño = cola.qsize()
    for _ in range(tamaño):
        superheroe = cola.get()
        if superheroe["nombre"] == "Scott Lang":
            print(f"{Fore.GREEN}El nombre del superhéroe de Scott Lang es: {Fore.CYAN}{subrayado}{superheroe['superheroe']}{Style.RESET_ALL}")
        cola.put(superheroe)

def superheroes_con_S(cola: Queue):
    tamaño = cola.qsize()
    print(f"{Fore.YELLOW}Superhéroes cuyos nombres comienzan con S:{Style.RESET_ALL}")
    for _ in range(tamaño):
        superheroe = cola.get()
        if superheroe["nombre"].startswith("S"):
            print(f"  - {Fore.CYAN}{superheroe['nombre']}{Style.RESET_ALL} - {Fore.MAGENTA}{superheroe['superheroe']}{Style.RESET_ALL}")
        cola.put(superheroe)

def carol_danvers(cola: Queue):
    tamaño = cola.qsize()
    for _ in range(tamaño):
        superheroe = cola.get()
        if superheroe["nombre"] == "Carol Danvers":
            print(f"{Fore.GREEN}El nombre del superhéroe de Carol Danvers es: {Fore.CYAN}{subrayado}{superheroe['superheroe']}{Style.RESET_ALL}")
        cola.put(superheroe)

print(f"{Fore.YELLOW}Lista de personajes y superhéroes:{Style.RESET_ALL}")
for _ in range(MCU.qsize()):
    superheroe = MCU.get()
    print(f"  - {Fore.CYAN}{superheroe['nombre']}{Style.RESET_ALL} - {Fore.RED}{superheroe['superheroe']}{Style.RESET_ALL}")
    MCU.put(superheroe)
print("-" * 50)
nombre_superheroe_captain_marvel(MCU)
print("-" * 50)
superheroes_femeninos(MCU)
print("-" * 50)
personajes_masculinos(MCU)
print("-" * 50)
scott_lang(MCU)
print("-" * 50)
superheroes_con_S(MCU)
print("-" * 50)
carol_danvers(MCU)
print("-" * 50)