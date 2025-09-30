"""
* Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y resuelva las siguientes consultas: (RESUELTO)
*   a. listado inorden de las criaturas y quienes la derrotaron;
*   b. se debe permitir cargar una breve descripción sobre cada criatura;
*   c. mostrar toda la información de la criatura Talos;
*   d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
*   e. listar las criaturas derrotadas por Heracles;
*   f. listar las criaturas que no han sido derrotadas;
*   g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
*   h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
*   i. se debe permitir búsquedas por coincidencia;
*   j. eliminar al Basilisco y a las Sirenas;
*   k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
*   l. modifique el nombre de la criatura Ladón por Dragón Ladón;
*   m. realizar un listado por nivel del árbol;
*   n. muestre las criaturas capturadas por Heracles.


Criaturas                 | Derrotado por      | Criaturas             | Derrotado por
--------------------------|--------------------|-----------------------|----------------
Ceto                      | -                  | Cerda de Cromión       | Teseo
Tifón                     | Zeus               | Ortro                  | Heracles
Equidna                   | Argos Panoptes     | Toro de Creta          | Teseo
Dino                      | -                  | Jabalí de Calidón      | Atalanta
Pefredo                   | -                  | Carcinos               | -
Enio                      | -                  | Gerión                 | Heracles
Escila                    | -                  | Cloto                  | -
Caribdis                  | -                  | Láquesis               | -
Euríale                   | -                  | Átropos                | -
Esteno                    | -                  | Minotauro de Creta     | Teseo
Medusa                    | Perseo             | Harpías                | -
Ladón                     | Heracles           | Argos Panoptes         | Hermes
Águila del Cáucaso        | -                  | Aves del Estínfalo     | -
Quimera                   | Belerofonte        | Talos                  | Medea
Hidra de Lerna            | Heracles           | Sirenas                | -
León de Nemea             | Heracles           | Pitón                  | Apolo
Esfinge                   | Edipo              | Cierva de Cerinea      | -
Dragón de la Cólquida     | -                  | Basilisco              | -
Cerbero                   | -                  | Jabalí de Erimanto     | -

"""
from tree import BinaryTree
from collections import Counter

criaturas_data = [
    {"nombre": "Ceto", "derrotado_por": None, "descripcion": "Una deidad marina primordial.", "capturada_por": None},
    {"nombre": "Tifón", "derrotado_por": "Zeus", "descripcion": "El 'padre de todos los monstruos'.", "capturada_por": None},
    {"nombre": "Equidna", "derrotado_por": "Argos Panoptes", "descripcion": "La 'madre de todos los monstruos'.", "capturada_por": None},
    {"nombre": "Dino", "derrotado_por": None, "descripcion": "Una de las Grayas.", "capturada_por": None},
    {"nombre": "Pefredo", "derrotado_por": None, "descripcion": "Una de las Grayas.", "capturada_por": None},
    {"nombre": "Enio", "derrotado_por": None, "descripcion": "Una de las Grayas.", "capturada_por": None},
    {"nombre": "Escila", "derrotado_por": None, "descripcion": "Monstruo marino con torso de mujer y cola de pez.", "capturada_por": None},
    {"nombre": "Caribdis", "derrotado_por": None, "descripcion": "Un remolino marino monstruoso.", "capturada_por": None},
    {"nombre": "Euríale", "derrotado_por": None, "descripcion": "Una de las Gorgonas, hermana de Medusa.", "capturada_por": None},
    {"nombre": "Esteno", "derrotado_por": None, "descripcion": "Una de las Gorgonas, la más sanguinaria.", "capturada_por": None},
    {"nombre": "Medusa", "derrotado_por": "Perseo", "descripcion": "Gorgona que convertía en piedra a quienes la miraban.", "capturada_por": None},
    {"nombre": "Ladón", "derrotado_por": "Heracles", "descripcion": "Dragón de cien cabezas que guardaba el jardín de las Hespérides.", "capturada_por": None},
    {"nombre": "Águila del Cáucaso", "derrotado_por": None, "descripcion": "Águila que devoraba el hígado de Prometeo.", "capturada_por": None},
    {"nombre": "Quimera", "derrotado_por": "Belerofonte", "descripcion": "Monstruo con cabeza de león, cuerpo de cabra y cola de serpiente.", "capturada_por": None},
    {"nombre": "Hidra de Lerna", "derrotado_por": "Heracles", "descripcion": "Serpiente acuática con múltiples cabezas que se regeneraban.", "capturada_por": None},
    {"nombre": "León de Nemea", "derrotado_por": "Heracles", "descripcion": "León con piel impenetrable.", "capturada_por": None},
    {"nombre": "Esfinge", "derrotado_por": "Edipo", "descripcion": "Demonio de destrucción y mala suerte, con rostro de mujer, cuerpo de león y alas de ave.", "capturada_por": None},
    {"nombre": "Dragón de la Cólquida", "derrotado_por": None, "descripcion": "Dragón que custodiaba el Vellocino de Oro.", "capturada_por": None},
    {"nombre": "Cerbero", "derrotado_por": None, "descripcion": "Perro de tres cabezas que guardaba la entrada al Inframundo.", "capturada_por": None},
    {"nombre": "Cerda de Cromión", "derrotado_por": "Teseo", "descripcion": "Una cerda monstruosa.", "capturada_por": None},
    {"nombre": "Ortro", "derrotado_por": "Heracles", "descripcion": "Perro de dos cabezas, hermano de Cerbero.", "capturada_por": None},
    {"nombre": "Toro de Creta", "derrotado_por": "Teseo", "descripcion": "Toro que lanzaba fuego por el hocico.", "capturada_por": None},
    {"nombre": "Jabalí de Calidón", "derrotado_por": "Atalanta", "descripcion": "Un jabalí de tamaño y fuerza descomunales.", "capturada_por": None},
    {"nombre": "Carcinos", "derrotado_por": None, "descripcion": "Cangrejo gigante que ayudó a la Hidra de Lerna.", "capturada_por": None},
    {"nombre": "Gerión", "derrotado_por": "Heracles", "descripcion": "Gigante de tres cuerpos.", "capturada_por": None},
    {"nombre": "Cloto", "derrotado_por": None, "descripcion": "Una de las Moiras, la que hilaba el destino.", "capturada_por": None},
    {"nombre": "Láquesis", "derrotado_por": None, "descripcion": "Una de las Moiras, la que medía la longitud del hilo.", "capturada_por": None},
    {"nombre": "Átropos", "derrotado_por": None, "descripcion": "Una de las Moiras, la que cortaba el hilo de la vida.", "capturada_por": None},
    {"nombre": "Minotauro de Creta", "derrotado_por": "Teseo", "descripcion": "Hombre con cabeza de toro encerrado en el Laberinto.", "capturada_por": None},
    {"nombre": "Harpías", "derrotado_por": None, "descripcion": "Seres con cuerpo de ave y rostro de mujer.", "capturada_por": None},
    {"nombre": "Argos Panoptes", "derrotado_por": "Hermes", "descripcion": "Gigante con cien ojos.", "capturada_por": None},
    {"nombre": "Aves del Estínfalo", "derrotado_por": None, "descripcion": "Aves con picos, garras y alas de bronce.", "capturada_por": None},
    {"nombre": "Talos", "derrotado_por": "Medea", "descripcion": "Gigante de bronce que protegía Creta.", "capturada_por": None},
    {"nombre": "Sirenas", "derrotado_por": None, "descripcion": "Criaturas marinas que atraían a los marineros con su canto.", "capturada_por": None},
    {"nombre": "Pitón", "derrotado_por": "Apolo", "descripcion": "Gran serpiente que guardaba el oráculo de Delfos.", "capturada_por": None},
    {"nombre": "Cierva de Cerinea", "derrotado_por": None, "descripcion": "Cierva con pezuñas de bronce y cuernos de oro.", "capturada_por": None},
    {"nombre": "Basilisco", "derrotado_por": None, "descripcion": "Serpiente legendaria que podía matar con la mirada.", "capturada_por": None},
    {"nombre": "Jabalí de Erimanto", "derrotado_por": None, "descripcion": "Un jabalí que causaba estragos en Erimanto.", "capturada_por": None},
]

arbol_criaturas = BinaryTree()
for criatura in criaturas_data:
    arbol_criaturas.insert(criatura["nombre"], criatura)

# a. listado inorden de las criaturas y quienes la derrotaron;
def punto_a(arbol):
    print("a. Listado inorden de criaturas y quién las derrotó:")
    def in_order_derrotado(root):
        if root is not None:
            in_order_derrotado(root.left)
            derrotado_por = root.other_values.get("derrotado_por") or "Nadie"
            print(f"- {root.value} (Derrotado por: {derrotado_por})")
            in_order_derrotado(root.right)
    in_order_derrotado(arbol.root)

# b. se debe permitir cargar una breve descripción sobre cada criatura; (Ya incluido en la carga inicial)
def punto_b(arbol):
    print("\nb. Descripciones de cada criatura:")
    def __mostrar_descripciones(root):
        if root is not None:
            __mostrar_descripciones(root.left)
            nombre = root.value
            descripcion = root.other_values.get("descripcion", "No tiene descripción.")
            print(f"   - {nombre}: {descripcion}")
            __mostrar_descripciones(root.right)
    __mostrar_descripciones(arbol.root)

# c. mostrar toda la información de la criatura Talos;
def punto_c(arbol, nombre_criatura):
    print(f"\nc. Información completa de '{nombre_criatura}':")
    nodo = arbol.search(nombre_criatura)
    if nodo:
        print(f"   - Nombre: {nodo.value}")
        for key, value in nodo.other_values.items():
            print(f"   - {key.replace('_', ' ').capitalize()}: {value or 'No disponible'}")
    else:
        print(f"   No se encontró a '{nombre_criatura}'.")

# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
def punto_d(arbol):
    print("\nd. Top 3 héroes/dioses con más victorias:")
    derrotas = Counter()
    def contar_derrotas(root):
        if root is not None:
            if root.other_values.get("derrotado_por"):
                derrotas[root.other_values["derrotado_por"]] += 1
            contar_derrotas(root.left)
            contar_derrotas(root.right)
    contar_derrotas(arbol.root)
    for heroe, count in derrotas.most_common(3):
        print(f"   - {heroe}: {count} criaturas derrotadas.")

# e. listar las criaturas derrotadas por Heracles;
def punto_e(arbol, heroe):
    print(f"\ne. Criaturas derrotadas por {heroe}:")
    criaturas_derrotadas = []
    def buscar_por_heroe(root):
        if root is not None:
            if root.other_values.get("derrotado_por") == heroe:
                criaturas_derrotadas.append(root.value)
            buscar_por_heroe(root.left)
            buscar_por_heroe(root.right)
    buscar_por_heroe(arbol.root)
    if criaturas_derrotadas:
        for c in criaturas_derrotadas:
            print(f"   - {c}")
    else:
        print(f"   {heroe} no derrotó a ninguna criatura de la lista.")

# f. listar las criaturas que no han sido derrotadas;
def punto_f(arbol):
    print("\nf. Criaturas no derrotadas:")
    def no_derrotadas(root):
        if root is not None:
            no_derrotadas(root.left)
            if not root.other_values.get("derrotado_por"):
                print(f"   - {root.value}")
            no_derrotadas(root.right)
    no_derrotadas(arbol.root)

# g. y h. Modificar nodos para indicar capturas por Heracles
def punto_h(arbol):
    print("\nh. Actualizando capturas por Heracles...")
    criaturas_a_capturar = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
    for nombre in criaturas_a_capturar:
        nodo = arbol.search(nombre)
        if nodo:
            nodo.other_values["capturada_por"] = "Heracles"
            print(f"   - '{nombre}' ha sido marcada como capturada por Heracles.")

# i. se debe permitir búsquedas por coincidencia;
def punto_i(arbol, coincidencia):
    print(f"\ni. Búsqueda por coincidencia para '{coincidencia}':")
    # La función proximity_search original solo imprime, no devuelve una lista.
    # Para poder verificar si hubo resultados, creamos una función local que sí los recolecte.
    resultados = []
    def __buscar_coincidencias(root, prefijo):
        if root is not None:
            if root.value.startswith(prefijo):
                resultados.append(root.value)
            __buscar_coincidencias(root.left, prefijo)
            __buscar_coincidencias(root.right, prefijo)

    __buscar_coincidencias(arbol.root, coincidencia)
    
    if resultados:
        for r in resultados:
            print(f"   - Encontrado: {r}")
    else:
        print(f"   No se encontraron criaturas que comiencen con '{coincidencia}'.")

# j. eliminar al Basilisco y a las Sirenas;
def punto_j(arbol):
    print("\nj. Eliminando criaturas...")
    for nombre in ["Basilisco", "Sirenas"]:
        valor, _ = arbol.delete(nombre)
        if valor:
            print(f"   - '{valor}' ha sido eliminado del árbol.")
        else:
            print(f"   - No se pudo eliminar a '{nombre}' (no encontrado).")

# k. modificar el nodo que contiene a las Aves del Estínfalo
def punto_k(arbol):
    print("\nk. Modificando a las Aves del Estínfalo...")
    nodo = arbol.search("Aves del Estínfalo")
    if nodo:
        nodo.other_values["derrotado_por"] = "Heracles"
        nodo.other_values["descripcion"] += " Heracles derrotó a varias de ellas como parte de sus doce trabajos."
        print("   - Nodo modificado. Ahora derrotadas por Heracles y descripción actualizada.")

# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
def punto_l(arbol):
    print("\nl. Renombrando a Ladón...")
    valor, datos = arbol.delete("Ladón")
    if valor:
        datos["nombre"] = "Dragón Ladón"
        arbol.insert("Dragón Ladón", datos)
        print("   - 'Ladón' ha sido renombrado a 'Dragón Ladón'.")

# m. realizar un listado por nivel del árbol;
def punto_m(arbol):
    print("\nm. Listado por nivel del árbol:")
    arbol.by_level()

# n. muestre las criaturas capturadas por Heracles.
def punto_n(arbol, heroe):
    print(f"\nn. Criaturas capturadas por {heroe}:")
    criaturas_capturadas = []
    def capturadas_por(root):
        if root is not None:
            capturadas_por(root.left)
            if root.other_values.get("capturada_por") == heroe:
                criaturas_capturadas.append(root.value)
            capturadas_por(root.right)
    capturadas_por(arbol.root)
    
    if criaturas_capturadas:
        for c in criaturas_capturadas:
            print(f"   - {c}")
    else:
        print(f"   {heroe} no ha capturado ninguna criatura.")

if __name__ == "__main__":
    print('-' * 50)
    punto_a(arbol_criaturas)
    print('-' * 50)
    punto_b(arbol_criaturas)
    print('-' * 50)
    punto_c(arbol_criaturas, "Talos")
    print('-' * 50)
    punto_d(arbol_criaturas)
    print('-' * 50)
    punto_e(arbol_criaturas, "Heracles")
    print('-' * 50)
    punto_f(arbol_criaturas)
    print('-' * 50)
    punto_h(arbol_criaturas)
    print('-' * 50)
    punto_i(arbol_criaturas, "Cer")
    print('-' * 50)
    punto_j(arbol_criaturas)
    print('-' * 50)
    punto_k(arbol_criaturas)
    print('-' * 50)
    punto_l(arbol_criaturas)
    print('-' * 50)
    punto_m(arbol_criaturas)
    print('-' * 50)
    punto_n(arbol_criaturas, "Heracles")
    print('-' * 50)
