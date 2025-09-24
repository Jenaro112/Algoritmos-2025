""" 
Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
se (MCU), desarrollar un algoritmo que contemple lo siguiente:
a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
leano que indica si es un héroe o un villano, True y False respectivamente;
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

# --- Funciones auxiliares para recorridos específicos ---

def in_order_filter_and_print(root, prefix, is_villain_filter, results_list):
    """
    Recorrido in-order que filtra nodos y los agrega a una lista.
    - prefix: El prefijo con el que debe comenzar el nombre.
    - is_villain_filter: True para villanos, False para héroes.
    - results_list: Lista donde se almacenan los resultados.
    """
    if root is not None:
        in_order_filter_and_print(root.left, prefix, is_villain_filter, results_list)
        if root.other_values.get('is_villain') == is_villain_filter and root.value.startswith(prefix):
            results_list.append(root.value)
        in_order_filter_and_print(root.right, prefix, is_villain_filter, results_list)

def in_order_desc(root, results_list):
    """
    Recorrido in-order que almacena los valores del árbol en orden descendente.
    """
    if root is not None:
        in_order_desc(root.right, results_list)
        results_list.append(root.value)
        in_order_desc(root.left, results_list)

def in_order_names_only(root):
    """
    Recorrido in-order que imprime solo los nombres (root.value).
    """
    if root is not None:
        in_order_names_only(root.left)
        print(f"   - {root.value}")
        in_order_names_only(root.right)

def count_nodes(root):
    """
    Cuenta el número total de nodos en un árbol de forma recursiva.
    """
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)



def Punto_A():
    """Punto A: Carga de datos en el árbol."""
    print("Punto A")
    mcu_tree = BinaryTree()
    for character in superheroes:
        mcu_tree.insert(character['name'], character)
    print("-> Árbol de personajes cargado exitosamente.")
    return mcu_tree

def Punto_B(mcu_tree):
    """Punto B: Listar los villanos ordenados alfabéticamente."""
    print("Punto B")
    mcu_tree.villain_in_order()

def Punto_C(mcu_tree):
    """Punto C: Mostrar todos los superhéroes que empiezan con C."""
    print("Punto C")
    heroes_con_C = []
    in_order_filter_and_print(mcu_tree.root, "C", False, heroes_con_C)
    if heroes_con_C:
        for name in heroes_con_C:
            print(f"   - {name}")
    else:
        print("   No se encontraron superhéroes que comiencen con 'C'.")

def Punto_D(mcu_tree):
    """Punto D: Determinar cuántos superhéroes hay en el árbol."""
    print("Punto D")
    print(f"-> Hay {mcu_tree.count_heroes()} superhéroes en el árbol.")

def Punto_E(mcu_tree):
    """Punto E: Corrección de 'Dr Strannnnnge'."""
    print("Punto E")
    incorrect_name = "Dr Strannnnnge"
    correct_name = "Dr Strange"

    print(f"-> Buscando personajes que comienzan con 'Dr':")
    mcu_tree.proximity_search('Dr')

    value, other_value = mcu_tree.delete(incorrect_name)
    if value is not None:
        other_value['name'] = correct_name
        mcu_tree.insert(correct_name, other_value)
        print(f"-> Se ha corregido el nombre de '{incorrect_name}' a '{correct_name}'.")
    else:
        print(f"No se encontró a '{incorrect_name}' para modificar.")

def Punto_F(mcu_tree):
    """Punto F: Listar superhéroes ordenados de manera descendente."""
    print("Punto F")
    superheroes_desc = []
    if mcu_tree.root:
        in_order_desc(mcu_tree.root, superheroes_desc)

    for i, name in enumerate(superheroes_desc):
        print(f"{i+1}. {name}")

def Punto_G(mcu_tree):
    """Punto G: Generar y analizar bosque de héroes y villanos."""
    print("Punto G")
    heroes_tree = BinaryTree() 
    villains_tree = BinaryTree()

    mcu_tree.divide_tree(heroes_tree, villains_tree)

    print("\nI. Cantidad de nodos en cada árbol:")
    num_heroes = count_nodes(heroes_tree.root)
    num_villains = count_nodes(villains_tree.root)
    print(f"   - Árbol de Héroes: {num_heroes} nodos.")
    print(f"   - Árbol de Villanos: {num_villains} nodos.")

    print("\nII. Barrido ordenado de cada árbol:")

    print("\n   [ HÉROES ]")
    in_order_names_only(heroes_tree.root)

    print("\n   [ VILLANOS ]")
    in_order_names_only(villains_tree.root)


if __name__ == "__main__":
    print("-" * 40)
    mcu_tree = Punto_A()
    print("-" * 40)
    Punto_B(mcu_tree)
    print("-" * 40)
    Punto_C(mcu_tree)
    print("-" * 40)
    Punto_D(mcu_tree)
    print("-" * 40)
    Punto_E(mcu_tree)
    print("-" * 40)
    Punto_F(mcu_tree)
    print("-" * 40)
    Punto_G(mcu_tree)
    print("-" * 40)
