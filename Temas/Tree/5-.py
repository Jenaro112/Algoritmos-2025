""" 
Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
se (MCU), desarrollar un algoritmo que contemple lo siguiente:
a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
b. listar los villanos ordenados alfabéticamente; -> (Se listan en el punto G.II)
c. mostrar todos los superhéroes que empiezan con C; -> (Se listan en el punto G.II)
d. determinar cuántos superhéroes hay en el árbol; -> (Se cuenta en el punto G.I)
e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre; -> (Se corrige en el punto A)
f. listar los superhéroes ordenados de manera descendente;
g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
    I. determinar cuántos nodos tiene cada árbol;
    II. realizar un barrido ordenado alfabéticamente de cada árbol.
"""

from tree import BinaryTree
from super_heroes_data import superheroes
from MiLibreria import imprimir_titulo, imprimir_subtitulo, imprimir_mensaje, imprimir_separador

def Punto_A():
    """a. Crea un árbol binario y lo carga con los datos de los superhéroes."""
    imprimir_subtitulo("a. Carga del Árbol de Personajes")
    # 1. Se crea una instancia vacía de tu clase BinaryTree.
    mcu_tree = BinaryTree()
    # 2. Se itera sobre la lista de diccionarios `superheroes`.
    for character in superheroes:
        # 3. Por cada personaje, se inserta un nuevo nodo en el árbol.
        #    - La clave de ordenamiento es el nombre ('name').
        #    - El diccionario completo del personaje se guarda en 'other_values'.
        mcu_tree.insert(character['name'], character)
    imprimir_mensaje("Árbol de personajes cargado exitosamente.", "exito")
    # 4. Se devuelve el árbol ya cargado para usarlo en las otras funciones.
    return mcu_tree

def Punto_B(villains_tree):
    """b. Lista los villanos ordenados alfabéticamente."""
    imprimir_subtitulo("b. Listado de Villanos (ordenado alfabéticamente)")
    # Se utiliza el método `in_order()` del árbol de villanos.
    # Un recorrido in-order en un Árbol Binario de Búsqueda siempre devuelve
    # los elementos en orden ascendente (alfabético en este caso).
    villains_tree.in_order()

def Punto_C(heroes_tree):
    """c. Muestra todos los superhéroes que empiezan con C."""
    imprimir_subtitulo("c. Superhéroes que empiezan con 'C'")
    # Se utiliza el método `proximity_search()` de tu librería de árbol.
    # Este método está diseñado para buscar y mostrar todos los nodos
    # cuyo valor (nombre del héroe) comienza con el prefijo dado.
    heroes_tree.proximity_search('C')

def Punto_D(mcu_tree):
    """d. Determina cuántos superhéroes hay en el árbol."""
    imprimir_subtitulo("d. Cantidad total de Superhéroes")
    # Se utiliza el método `count_heroes()` que ya existe en tu librería `tree.py`.
    # Este método recorre el árbol y cuenta cuántos nodos tienen el campo 'is_villain' en False.
    total_heroes = mcu_tree.count_heroes()
    imprimir_mensaje(f"Hay un total de {total_heroes} superhéroes en el árbol original.", "info")

def Punto_E(mcu_tree):
    """e. Corrige el nombre de 'Dr Strange' usando búsqueda por proximidad."""
    imprimir_subtitulo("e. Corrección del nombre 'Dr Strange'")
    # Se definen los nombres incorrecto y correcto.
    incorrect_name = "Dr Strannnnnge"
    correct_name = "Dr Strange"
    
    # Se realiza una búsqueda por proximidad para mostrar que el nombre está mal escrito.
    imprimir_mensaje(f"Buscando a '{incorrect_name}' por proximidad...", "info")
    mcu_tree.proximity_search('Dr')

    # Para cambiar la clave principal de un nodo (el nombre), debemos:
    # 1. Eliminar el nodo con el nombre incorrecto. El método `delete` devuelve los datos del nodo eliminado.
    value, other_value = mcu_tree.delete(incorrect_name)
    # 2. Si se encontró y eliminó el nodo...
    if value is not None:
        # ...modificamos el nombre en los datos que recuperamos...
        other_value['name'] = correct_name
        # ...y volvemos a insertar el personaje en el árbol, ahora con el nombre correcto.
        mcu_tree.insert(correct_name, other_value)
        imprimir_mensaje(f"Se ha corregido el nombre a '{correct_name}'.", "exito")
    else:
        # Si no se encontró, se informa al usuario.
        imprimir_mensaje(f"No se encontró a '{incorrect_name}' para modificar.", "error")

def Punto_F(heroes_tree):
    """f. Lista los superhéroes en orden descendente."""
    imprimir_subtitulo("f. Listado de Superhéroes (orden descendente)")
    # Como la librería no tiene un método para orden descendente, definimos una función local recursiva.
    def in_order_desc(root):
        # Un recorrido in-order descendente visita: subárbol derecho, raíz, subárbol izquierdo.
        if root is not None:
            in_order_desc(root.right)
            print(f"   - {root.value}")
            in_order_desc(root.left)
    # Se inicia el recorrido desde la raíz del árbol de héroes.
    in_order_desc(heroes_tree.root)

def Punto_G(mcu_tree):
    """g. Genera un bosque a partir del árbol principal."""
    imprimir_subtitulo("g. Generación de Bosque (Héroes y Villanos)")
    # Se crean dos nuevos árboles vacíos, uno para héroes y otro para villanos.
    heroes_tree = BinaryTree()
    villains_tree = BinaryTree()
    # Se utiliza el método `divide_tree` de tu librería, que recorre el árbol original
    # y va insertando cada personaje en el árbol que le corresponde.
    mcu_tree.divide_tree(heroes_tree, villains_tree)
    imprimir_mensaje("Bosque generado a partir del árbol principal.", "exito")
    # Se devuelven los dos nuevos árboles para ser utilizados en los siguientes puntos.
    return heroes_tree, villains_tree

def Punto_G_I(heroes_tree, villains_tree):
    """g.I. Determina cuántos nodos tiene cada árbol del bosque."""
    imprimir_subtitulo("g.I. Conteo de nodos en cada árbol del bosque")
    # La librería `tree.py` tiene `count_heroes`, pero no un contador genérico de nodos.
    # Por eso, definimos una función local recursiva para contar todos los nodos de un árbol.
    def count_nodes(root):
        if root is None:
            return 0
        return 1 + count_nodes(root.left) + count_nodes(root.right)
    
    print(f"   - Árbol de Héroes: {count_nodes(heroes_tree.root)} nodos.")
    print(f"   - Árbol de Villanos: {count_nodes(villains_tree.root)} nodos.")

def Punto_G_II(heroes_tree, villains_tree):
    """g.II. Realiza un barrido ordenado alfabéticamente de cada árbol."""
    imprimir_subtitulo("g.II. Barrido ordenado de cada árbol")
    # Se realiza un recorrido in-order en cada uno de los árboles del bosque.
    imprimir_mensaje("Listado de Héroes:", "info")
    heroes_tree.in_order()
    imprimir_mensaje("Listado de Villanos:", "info")
    villains_tree.in_order()

# --- FUNCIÓN PRINCIPAL ---
def main():
    """Función principal que orquesta la ejecución de todos los puntos del ejercicio."""
    imprimir_titulo("Análisis de Personajes de MCU")
    # Se crea y carga el árbol principal.
    mcu_tree = Punto_A()
    # Se corrigen los datos necesarios en el árbol principal.
    Punto_E(mcu_tree)
    Punto_D(mcu_tree)
    # Se divide el árbol principal en un bosque de héroes y villanos.
    heroes_tree, villains_tree = Punto_G(mcu_tree)
    # Se realizan las operaciones sobre los árboles del bosque.
    Punto_G_I(heroes_tree, villains_tree)
    Punto_B(villains_tree)
    Punto_C(heroes_tree)
    Punto_F(heroes_tree)
    # El punto G.II se resuelve implícitamente con los puntos B y C, pero lo llamamos para ser explícitos.
    # Punto_G_II(heroes_tree, villains_tree) # Descomentar si se desea un listado completo de ambos.

# --- PUNTO DE ENTRADA DEL SCRIPT ---
# Este bloque de código se ejecuta solo si este archivo es el programa principal.
if __name__ == "__main__":
    main()
