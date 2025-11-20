"""
MiLibreria.py

Una pequeña librería con funciones para mejorar la estética de la salida en consola.
Incluye títulos, separadores y mensajes con colores para que todo quede más "fachero".
"""

class Colores:
    """
    Clase que contiene los códigos de escape ANSI para dar color al texto en la terminal.
    """
    HEADER = '\033[95m'     # Magenta claro
    OKBLUE = '\033[94m'     # Azul claro
    OKCYAN = '\033[96m'     # Cian claro
    OKGREEN = '\033[92m'    # Verde claro
    WARNING = '\033[93m'    # Amarillo
    FAIL = '\033[91m'       # Rojo
    ENDC = '\033[0m'        # Código para resetear el color
    BOLD = '\033[1m'        # Texto en negrita
    UNDERLINE = '\033[4m'   # Texto subrayado

def imprimir_titulo(texto: str, color: str = Colores.HEADER):
    """
    Imprime un título principal estilizado, centrado dentro de una caja.

    Args:
        texto (str): El texto del título.
        color (str): El código de color ANSI a utilizar.
    """
    texto_centrado = f" {texto.upper()} "
    longitud = len(texto_centrado)
    print(f"\n{color}{Colores.BOLD}╔{'═' * longitud}╗{Colores.ENDC}")
    print(f"{color}{Colores.BOLD}║{texto_centrado}║{Colores.ENDC}")
    print(f"{color}{Colores.BOLD}╚{'═' * longitud}╝{Colores.ENDC}")

def imprimir_subtitulo(texto: str, color: str = Colores.OKCYAN):
    """
    Imprime un subtítulo resaltado con un subrayado simple.

    Args:
        texto (str): El texto del subtítulo.
        color (str): El código de color ANSI a utilizar.
    """
    print(f"\n{color}{Colores.BOLD}{texto}{Colores.ENDC}")
    print(f"{color}{'─' * len(texto)}{Colores.ENDC}")

def imprimir_separador(caracter: str = '─', longitud: int = 60, color: str = Colores.OKBLUE):
    """
    Imprime una línea separadora para organizar la salida.

    Args:
        caracter (str): El carácter que formará la línea.
        longitud (int): El largo de la línea.
        color (str): El código de color ANSI a utilizar.
    """
    print(color + caracter * longitud + Colores.ENDC)

def imprimir_mensaje(texto: str, tipo: str = 'info'):
    """
    Imprime un mensaje con un ícono y color según su tipo.

    Args:
        texto (str): El contenido del mensaje.
        tipo (str): 'info', 'exito', 'alerta', o 'error'.
    """
    if tipo == 'exito':
        print(f"{Colores.OKGREEN}[✓] {texto}{Colores.ENDC}")
    elif tipo == 'alerta':
        print(f"{Colores.WARNING}[!] {texto}{Colores.ENDC}")
    elif tipo == 'error':
        print(f"{Colores.FAIL}[✗] {texto}{Colores.ENDC}")
    else: # info por defecto
        print(f"{Colores.OKBLUE}[i] {texto}{Colores.ENDC}")

# Ejemplo de uso (puedes descomentar esto para probar la librería directamente)
# if __name__ == "__main__":
#     imprimir_titulo("Demostración de MiLibreria")
#     imprimir_subtitulo("Mensajes de prueba")
#     imprimir_mensaje("Esto es un mensaje de información.")
#     imprimir_mensaje("La operación se completó correctamente.", "exito")
#     imprimir_mensaje("Ten cuidado, el archivo ya existe.", "alerta")
#     imprimir_mensaje("No se pudo conectar a la base de datos.", "error")
#     imprimir_separador('*', 40)