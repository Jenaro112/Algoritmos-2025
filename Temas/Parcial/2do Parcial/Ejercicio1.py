""" 
* Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) de los cuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega evolucion (bool) y si tiene forma gigamax (bool) para el cual debemos construir tres árboles para acceder de manera eficiente a los datos contemplando lo siguiente:
*- los índices de cada uno de los árboles deben ser nombre, número y tipo.
*- mostrar todos los datos de un Pokémon a partir de su número y nombre para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres.
*- mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico.
*- realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre.
*- mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum.
*- mostrar todos los tipos de Pokémons y cuántos hay de cada tipo.
*- determinar cuantos Pokémons tienen megaevolucion.
*- determinar cuantos Pokémons tiene forma gigamax.
"""

from tree import BinaryTree
print("----------------------------------------")
print("2DO PARCIAL DE ALGORITMOS Y ESTRUCTURAS DE DATOS")
print("JENARO GALDINI")
print("----------------------------------------")

class Pokemon:
    def __init__(self, name, number, types, weaknesses, has_mega, has_gigantamax):
        self.name = name
        self.number = number
        self.types = types
        self.weaknesses = weaknesses
        self.has_mega = has_mega
        self.has_gigantamax = has_gigantamax

    def __str__(self):
        return (f"#{self.number} - {self.name} | Tipos: {self.types} | Debilidades: {self.weaknesses} | "
                f"Mega: {'Sí' if self.has_mega else 'No'} | Gigantamax: {'Sí' if self.has_gigantamax else 'No'}")

# Lista con 50 Pokémon importantes/populares
pokemon_list = [
    Pokemon("Bulbasaur", 1, ["Planta", "Veneno"], ["Fuego", "Hielo", "Volador", "Psíquico"], False, True),
    Pokemon("Charmander", 4, ["Fuego"], ["Agua", "Tierra", "Roca"], False, True),
    Pokemon("Squirtle", 7, ["Agua"], ["Planta", "Eléctrico"], False, True),
    Pokemon("Pikachu", 25, ["Eléctrico"], ["Tierra"], False, True),
    Pokemon("Jigglypuff", 39, ["Normal", "Hada"], ["Acero", "Veneno"], False, False),
    Pokemon("Meowth", 52, ["Normal"], ["Lucha"], False, True),
    Pokemon("Psyduck", 54, ["Agua"], ["Planta", "Eléctrico"], False, False),
    Pokemon("Machamp", 68, ["Lucha"], ["Volador", "Psíquico", "Hada"], False, True),
    Pokemon("Gengar", 94, ["Fantasma", "Veneno"], ["Fantasma", "Siniestro", "Psíquico", "Tierra"], True, True),
    Pokemon("Eevee", 133, ["Normal"], ["Lucha"], False, True),
    Pokemon("Jolteon", 135, ["Eléctrico"], ["Tierra"], False, False),
    Pokemon("Snorlax", 143, ["Normal"], ["Lucha"], False, True),
    Pokemon("Mewtwo", 150, ["Psíquico"], ["Bicho", "Fantasma", "Siniestro"], True, False),
    Pokemon("Mew", 151, ["Psíquico"], ["Bicho", "Fantasma", "Siniestro"], False, False),
    Pokemon("Chikorita", 152, ["Planta"], ["Fuego", "Hielo", "Veneno", "Volador", "Bicho"], False, False),
    Pokemon("Cyndaquil", 155, ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    Pokemon("Totodile", 158, ["Agua"], ["Planta", "Eléctrico"], False, False),
    Pokemon("Togepi", 175, ["Hada"], ["Veneno", "Acero"], False, False),
    Pokemon("Ampharos", 181, ["Eléctrico"], ["Tierra"], True, False),
    Pokemon("Lugia", 249, ["Psíquico", "Volador"], ["Eléctrico", "Hielo", "Roca", "Fantasma", "Siniestro"], False, False),
    Pokemon("Ho-Oh", 250, ["Fuego", "Volador"], ["Eléctrico", "Agua", "Roca"], False, False),
    Pokemon("Treecko", 252, ["Planta"], ["Fuego", "Hielo", "Veneno", "Volador", "Bicho"], False, False),
    Pokemon("Torchic", 255, ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    Pokemon("Mudkip", 258, ["Agua"], ["Planta", "Eléctrico"], False, False),
    Pokemon("Gardevoir", 282, ["Psíquico", "Hada"], ["Veneno", "Fantasma", "Acero"], True, False),
    Pokemon("Absol", 359, ["Siniestro"], ["Lucha", "Bicho", "Hada"], True, False),
    Pokemon("Groudon", 383, ["Tierra"], ["Agua", "Planta", "Hielo"], False, False),
    Pokemon("Kyogre", 382, ["Agua"], ["Planta", "Eléctrico"], False, False),
    Pokemon("Rayquaza", 384, ["Dragón", "Volador"], ["Hielo", "Roca", "Dragón", "Hada"], True, False),
    Pokemon("Lucario", 448, ["Lucha", "Acero"], ["Fuego", "Lucha", "Tierra"], True, False),
    Pokemon("Garchomp", 445, ["Dragón", "Tierra"], ["Hielo", "Dragón", "Hada"], True, False),
    Pokemon("Darkrai", 491, ["Siniestro"], ["Lucha", "Bicho", "Hada"], False, False),
    Pokemon("Arceus", 493, ["Normal"], ["Lucha"], False, False),
    Pokemon("Zoroark", 571, ["Siniestro"], ["Lucha", "Bicho", "Hada"], False, False),
    Pokemon("Greninja", 658, ["Agua", "Siniestro"], ["Eléctrico", "Planta", "Lucha", "Bicho", "Hada"], False, False),
    Pokemon("Sylveon", 700, ["Hada"], ["Veneno", "Acero"], False, False),
    Pokemon("Xerneas", 716, ["Hada"], ["Veneno", "Acero"], False, False),
    Pokemon("Yveltal", 717, ["Siniestro", "Volador"], ["Eléctrico", "Hielo", "Roca", "Hada"], False, False),
    Pokemon("Zygarde", 718, ["Dragón", "Tierra"], ["Hielo", "Dragón", "Hada"], False, False),
    Pokemon("Decidueye", 724, ["Planta", "Fantasma"], ["Fuego", "Hielo", "Volador", "Fantasma", "Siniestro"], False, False),
    Pokemon("Incineroar", 727, ["Fuego", "Siniestro"], ["Agua", "Lucha", "Tierra", "Roca"], False, False),
    Pokemon("Primarina", 730, ["Agua", "Hada"], ["Eléctrico", "Planta", "Veneno"], False, False),
    Pokemon("Lycanroc", 745, ["Roca"], ["Agua", "Planta", "Lucha", "Tierra", "Acero"], False, False),
    Pokemon("Mimikyu", 778, ["Fantasma", "Hada"], ["Fantasma", "Acero"], False, False),
    Pokemon("Zacian", 888, ["Hada", "Acero"], ["Fuego", "Tierra"], False, False),
    Pokemon("Zamazenta", 889, ["Lucha", "Acero"], ["Fuego", "Lucha", "Tierra"], False, False),
    Pokemon("Eternatus", 890, ["Veneno", "Dragón"], ["Tierra", "Psíquico", "Hielo", "Dragón"], False, True),
    Pokemon("Fuecoco", 909, ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    Pokemon("Sprigatito", 906, ["Planta"], ["Fuego", "Hielo", "Veneno", "Volador", "Bicho"], False, False),
    Pokemon("Tyrantrum", 697, ["Roca", "Dragón"], ["Hielo", "Lucha", "Tierra", "Acero", "Dragón", "Hada"], False, False),
]

# a. Creación de los tres árboles
name_tree = BinaryTree()
number_tree = BinaryTree()
type_tree = BinaryTree()

for pokemon in pokemon_list:
    name_tree.insert(pokemon.name, pokemon)
    number_tree.insert(pokemon.number, pokemon)
    for type_ in pokemon.types:
        type_node = type_tree.search(type_)
        if type_node:
            type_node.other_values.insert(pokemon.name, pokemon)
        else:
            sub_tree = BinaryTree()
            sub_tree.insert(pokemon.name, pokemon)
            type_tree.insert(type_, sub_tree)

print("Árboles de Pokémon creados y cargados.")

def punto_b():
    print("\n" + "="*50)
    print("--- b. Búsqueda por número y nombre ---")
    print("="*50)
    # Búsqueda por número
    num_to_search = 150
    print(f"\n> Buscando Pokémon número {num_to_search}:")
    pokemon_node = number_tree.search(num_to_search)
    if pokemon_node:
        print(f"  > {pokemon_node.other_values}")
    
    # Búsqueda por proximidad de nombre
    name_to_search = "bul"
    print(f"\n> Buscando Pokémon que contengan '{name_to_search}':")
    name_tree.proximity_search(name_to_search)

def punto_c():
    print("\n" + "="*50)
    print("--- c. Pokémon por tipo ---")
    print("="*50)
    types_to_list = ["Fantasma", "Fuego", "Acero", "Eléctrico"]
    for type_ in types_to_list:
        print(f"\n--- TIPO {type_.upper()} ---")
        type_node = type_tree.search(type_)
        if type_node:
            type_node.other_values.in_order()
        else:
            print(f"No hay Pokémon de tipo {type_} en la lista.")

def punto_d():
    print("\n" + "="*50)
    print("--- d. Listados ordenados ---")
    print("="*50)
    print("\n> Listado por nombre (ascendente):")
    name_tree.in_order()
    print("\n> Listado por número (ascendente):")
    number_tree.in_order()
    # "Listado por nivel por nombre" se interpreta como in-order por nombre, que es el mismo que el primero.
    print("\n> Listado por nivel por nombre (in-order):")
    name_tree.in_order()

def punto_e():
    print("\n" + "="*50)
    print("--- e. Pokémon débiles contra Jolteon, Lycanroc y Tyrantrum ---")
    print("="*50)
    targets = ["Jolteon", "Lycanroc", "Tyrantrum"]
    for target_name in targets:
        target_node = name_tree.search(target_name)
        if target_node:
            target_pokemon = target_node.other_values
            print(f"\nPokémon que son débiles contra {target_pokemon.name} (que es de tipo/s {target_pokemon.types}):")
            for pokemon in pokemon_list:
                # Un pokémon es débil si alguno de los tipos del atacante está en su lista de debilidades
                if any(t in pokemon.weaknesses for t in target_pokemon.types):
                    print(f" - {pokemon.name} es débil.")

def punto_f():
    print("\n" + "="*50)
    print("--- f. Conteo de Pokémon por tipo ---")
    print("="*50)
    def count_types(root):
        if root is not None:
            count_types(root.left)
            # Usamos el nuevo método size() que agregamos a la clase BinaryTree.
            print(f"Tipo: {root.value}, Cantidad: {root.other_values.size()}")
            count_types(root.right)
    if type_tree.root:
        count_types(type_tree.root)

def punto_g():
    print("\n" + "="*50)
    print("--- g. Conteo de Pokémon con Megaevolución ---")
    print("="*50)
    count = 0
    for pokemon in pokemon_list:
        if pokemon.has_mega:
            count += 1
    print(f"Hay {count} Pokémon con megaevolución.")

def punto_h():
    print("\n" + "="*50)
    print("--- h. Conteo de Pokémon con forma Gigantamax ---")
    print("="*50)
    count = 0
    for pokemon in pokemon_list:
        if pokemon.has_gigantamax:
            count += 1
    print(f"Hay {count} Pokémon con forma Gigantamax.")


def main():
    punto_b()
    punto_c()
    punto_d()
    punto_e()
    punto_f()
    punto_g()
    punto_h()

if __name__ == "__main__":
    main()