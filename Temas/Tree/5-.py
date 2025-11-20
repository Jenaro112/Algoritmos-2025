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
    """a. Carga el árbol con los datos de los superhéroes."""
    imprimir_subtitulo("a. Carga del Árbol de Personajes")
    mcu_tree = BinaryTree()
    for character in superheroes:
        mcu_tree.insert(character['name'], character)
    imprimir_mensaje("Árbol de personajes cargado exitosamente.", "exito")
    return mcu_tree

def Punto_B(villains_tree):
    """b. Lista los villanos ordenados alfabéticamente."""
    imprimir_subtitulo("b. Listado de Villanos (ordenado alfabéticamente)")
    villains_tree.in_order()

def Punto_C(heroes_tree):
    """c. Muestra todos los superhéroes que empiezan con C."""
    imprimir_subtitulo("c. Superhéroes que empiezan con 'C'")
    heroes_tree.proximity_search('C')

def Punto_D(mcu_tree):
    """d. Determina cuántos superhéroes hay en el árbol."""
    imprimir_subtitulo("d. Cantidad total de Superhéroes")
    total_heroes = mcu_tree.count_heroes()
    imprimir_mensaje(f"Hay un total de {total_heroes} superhéroes en el árbol original.", "info")

def Punto_E(mcu_tree):
    """e. Corrige el nombre de 'Dr Strange' usando búsqueda por proximidad."""
    imprimir_subtitulo("e. Corrección del nombre 'Dr Strange'")
    incorrect_name = "Dr Strannnnnge"
    correct_name = "Dr Strange"
    imprimir_mensaje(f"Buscando a '{incorrect_name}' por proximidad...", "info")
    mcu_tree.proximity_search('Dr')
    value, other_value = mcu_tree.delete(incorrect_name)
    if value is not None:
        other_value['name'] = correct_name
        mcu_tree.insert(correct_name, other_value)
        imprimir_mensaje(f"Se ha corregido el nombre a '{correct_name}'.", "exito")
    else:
        imprimir_mensaje(f"No se encontró a '{incorrect_name}' para modificar.", "error")

def Punto_F(heroes_tree):
    """f. Lista los superhéroes en orden descendente."""
    imprimir_subtitulo("f. Listado de Superhéroes (orden descendente)")
    def in_order_desc(root):
        if root is not None:
            in_order_desc(root.right)
            print(f"   - {root.value}")
            in_order_desc(root.left)
    in_order_desc(heroes_tree.root)

def Punto_G(mcu_tree):
    """g. Genera un bosque a partir del árbol principal."""
    imprimir_subtitulo("g. Generación de Bosque (Héroes y Villanos)")
    heroes_tree = BinaryTree()
    villains_tree = BinaryTree()
    mcu_tree.divide_tree(heroes_tree, villains_tree)
    imprimir_mensaje("Bosque generado a partir del árbol principal.", "exito")
    return heroes_tree, villains_tree

def Punto_G_I(heroes_tree, villains_tree):
    """g.I. Determina cuántos nodos tiene cada árbol del bosque."""
    imprimir_subtitulo("g.I. Conteo de nodos en cada árbol del bosque")
    # La librería no tiene un contador genérico, así que lo implementamos aquí
    def count_nodes(root):
        if root is None:
            return 0
        return 1 + count_nodes(root.left) + count_nodes(root.right)
    
    print(f"   - Árbol de Héroes: {count_nodes(heroes_tree.root)} nodos.")
    print(f"   - Árbol de Villanos: {count_nodes(villains_tree.root)} nodos.")

def Punto_G_II(heroes_tree, villains_tree):
    """g.II. Realiza un barrido ordenado alfabéticamente de cada árbol."""
    imprimir_subtitulo("g.II. Barrido ordenado de cada árbol")
    imprimir_mensaje("Listado de Héroes:", "info")
    heroes_tree.in_order()
    imprimir_mensaje("Listado de Villanos:", "info")
    villains_tree.in_order()

def main():
    imprimir_titulo("Análisis de Personajes de MCU")
    mcu_tree = Punto_A()
    Punto_E(mcu_tree)
    Punto_D(mcu_tree)
    heroes_tree, villains_tree = Punto_G(mcu_tree)
    Punto_G_I(heroes_tree, villains_tree)
    Punto_B(villains_tree)
    Punto_C(heroes_tree)
    Punto_F(heroes_tree)
    # El punto G.II se resuelve implícitamente con los puntos B y C, pero lo llamamos para ser explícitos.
    # Punto_G_II(heroes_tree, villains_tree) # Descomentar si se desea un listado completo de ambos.

if __name__ == "__main__":
    main()
