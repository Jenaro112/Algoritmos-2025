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
from queue_ import Queue
from stack_ import Stack
from MiLibreria import imprimir_titulo, imprimir_subtitulo, imprimir_mensaje, imprimir_separador

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

# --- CREACIÓN Y CARGA DEL ÁRBOL ---
# 1. Se crea una instancia vacía de tu clase BinaryTree.
arbol_criaturas = BinaryTree()
# 2. Se itera sobre la lista de diccionarios `criaturas_data`.
for criatura in criaturas_data:
    # 3. Por cada diccionario, se inserta un nuevo nodo en el árbol.
    #    - El primer argumento ('nombre') es la clave por la cual el árbol se ordena.
    #    - El segundo argumento (el diccionario 'criatura' completo) se almacena en 'other_values' del nodo.
    arbol_criaturas.insert(criatura["nombre"], criatura)

# --- DEFINICIÓN DE FUNCIONES PARA CADA PUNTO DEL EJERCICIO ---

def punto_a(arbol):
    """a. Realiza un listado inorden de las criaturas y muestra quién las derrotó."""
    imprimir_subtitulo("a. Listado inorden de criaturas y quién las derrotó")
    # Se define una función interna y recursiva para realizar el recorrido inorden.
    def in_order_derrotado(root):
        # Un recorrido inorden visita: subárbol izquierdo, raíz, subárbol derecho.
        # Esto garantiza que los resultados se muestren en orden alfabético.
        if root is not None:
            in_order_derrotado(root.left)
            # Se obtiene el valor del campo "derrotado_por". Si no existe o es None, se usa un texto por defecto.
            derrotado_por = root.other_values.get("derrotado_por") or "No fue derrotada"
            print(f"    - {root.value} (Derrotado por: {derrotado_por})")
            in_order_derrotado(root.right)
    # Se inicia el recorrido desde la raíz del árbol.
    in_order_derrotado(arbol.root)

def punto_b(arbol):
    """b. Muestra la descripción de cada criatura. (La carga ya se hizo al inicio)."""
    imprimir_subtitulo("b. Descripciones de cada criatura")
    # Se define otra función interna para recorrer el árbol en inorden.
    def __mostrar_descripciones(root):
        if root is not None:
            __mostrar_descripciones(root.left)
            nombre = root.value
            # Se obtiene la descripción del diccionario 'other_values'.
            descripcion = root.other_values.get("descripcion", "No tiene descripción.")
            print(f"   - {nombre}: {descripcion}")
            __mostrar_descripciones(root.right)
    # Se inicia el recorrido.
    __mostrar_descripciones(arbol.root)

def punto_c(arbol, nombre_criatura):
    """c. Muestra toda la información de una criatura específica."""
    imprimir_subtitulo(f"c. Información completa de '{nombre_criatura}'")
    # Se utiliza el método search del árbol para encontrar el nodo de la criatura.
    nodo = arbol.search(nombre_criatura)
    # Si el nodo se encuentra...
    if nodo:
        # ...se imprime su nombre (la clave principal)...
        print(f"   - Nombre: {nodo.value}")
        # ...y luego se itera sobre el diccionario 'other_values' para mostrar el resto de la información.
        for key, value in nodo.other_values.items():
            print(f"   - {key.replace('_', ' ').capitalize()}: {value or 'No disponible'}")
    else:
        # Si no se encuentra, se informa al usuario.
        imprimir_mensaje(f"No se encontró a '{nombre_criatura}'.", "alerta")

def punto_d(arbol):
    """d. Determina los 3 héroes o dioses que derrotaron a más criaturas."""
    imprimir_subtitulo("d. Top 3 Héroes/Dioses con más victorias")
    # Se usa un diccionario para llevar la cuenta de las victorias de cada héroe.
    # La clave será el nombre del héroe y el valor será su contador de victorias.
    conteo_derrotas = {}

    # Función interna recursiva para recorrer el árbol y contar.
    def contar_derrotas(root):
        if root is not None:
            # Si la criatura actual tiene un "derrotado_por"...
            if root.other_values.get("derrotado_por"):
                heroe = root.other_values["derrotado_por"]
                # ...se incrementa el contador para ese héroe en el diccionario.
                # .get(heroe, 0) devuelve el valor actual o 0 si el héroe no está aún en el diccionario.
                conteo_derrotas[heroe] = conteo_derrotas.get(heroe, 0) + 1
            # Se continúa el recorrido por ambos subárboles.
            contar_derrotas(root.left)
            contar_derrotas(root.right)
    
    # Se inicia el conteo desde la raíz.
    contar_derrotas(arbol.root)

    # Como no podemos usar librerías externas como `collections.Counter`, ordenamos manualmente.
    # 1. Convertimos el diccionario a una lista de tuplas (heroe, victorias).
    lista_heroes = list(conteo_derrotas.items())
    # 2. Ordenamos la lista usando un algoritmo de burbuja simple para poner los mayores primero.
    for i in range(len(lista_heroes)):
        for j in range(i + 1, len(lista_heroes)):
            # Comparamos el número de victorias (el segundo elemento de la tupla).
            if lista_heroes[i][1] < lista_heroes[j][1]:
                # Si el elemento en 'i' es menor que el de 'j', los intercambiamos.
                lista_heroes[i], lista_heroes[j] = lista_heroes[j], lista_heroes[i]
    # 3. Mostramos los primeros 3 elementos de la lista ya ordenada.
    for heroe, count in lista_heroes[:3]:
        print(f"   - {heroe}: {count} criaturas derrotadas.")

def punto_e(arbol, heroe):
    """e. Lista todas las criaturas que fueron derrotadas por un héroe específico."""
    imprimir_subtitulo(f"e. Criaturas derrotadas por {heroe}")
    criaturas_derrotadas = []
    # Función interna para recorrer el árbol.
    def buscar_por_heroe(root):
        if root is not None:
            # Si la criatura fue derrotada por el héroe que buscamos...
            if root.other_values.get("derrotado_por") == heroe:
                # ...la agregamos a la lista de resultados.
                criaturas_derrotadas.append(root.value)
            # Continuamos la búsqueda en todo el árbol.
            buscar_por_heroe(root.left)
            buscar_por_heroe(root.right)
    buscar_por_heroe(arbol.root)
    
    if criaturas_derrotadas:
        for c in criaturas_derrotadas:
            print(f"   - {c}")
    else:
        imprimir_mensaje(f"{heroe} no derrotó a ninguna criatura de la lista.", "info")

def punto_f(arbol):
    """f. Lista todas las criaturas que no han sido derrotadas."""
    imprimir_subtitulo("f. Criaturas no derrotadas")
    # Recorrido inorden para mostrar los resultados alfabéticamente.
    def no_derrotadas(root):
        if root is not None:
            no_derrotadas(root.left)
            # Si el campo "derrotado_por" no existe o es None...
            if not root.other_values.get("derrotado_por"):
                # ...imprimimos el nombre de la criatura.
                print(f"   - {root.value}")
            no_derrotadas(root.right)
    no_derrotadas(arbol.root)

def punto_h(arbol):
    """h. Modifica los nodos de ciertas criaturas para indicar que fueron capturadas por Heracles."""
    imprimir_subtitulo("h. Actualizando capturas por Heracles")
    criaturas_a_capturar = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
    for nombre in criaturas_a_capturar:
        # Buscamos cada criatura en el árbol.
        nodo = arbol.search(nombre)
        if nodo:
            # Si la encontramos, modificamos el campo "capturada_por" en su diccionario 'other_values'.
            nodo.other_values["capturada_por"] = "Heracles"
            imprimir_mensaje(f"'{nombre}' ha sido marcada como capturada por Heracles.", "exito")

def punto_i(arbol, coincidencia):
    """i. Realiza una búsqueda por coincidencia de prefijo."""
    imprimir_subtitulo(f"i. Búsqueda por coincidencia para '{coincidencia}'")
    # La función `proximity_search` de tu librería solo imprime, no devuelve una lista.
    # Para poder verificar si hubo resultados, creamos una función local que los recolecte.
    resultados = []
    def __buscar_coincidencias(root, prefijo):
        if root is not None:
            # Si el nombre de la criatura (root.value) comienza con el texto de 'coincidencia'...
            if root.value.startswith(prefijo):
                # ...lo agregamos a nuestra lista de resultados.
                resultados.append(root.value)
            # Continuamos la búsqueda en todo el árbol.
            __buscar_coincidencias(root.left, prefijo)
            __buscar_coincidencias(root.right, prefijo)

    __buscar_coincidencias(arbol.root, coincidencia)
    
    # Al final, mostramos los resultados si encontramos alguno.
    if resultados:
        for r in resultados:
            print(f"   - Encontrado: {r}")
    else:
        imprimir_mensaje(f"No se encontraron criaturas que comiencen con '{coincidencia}'.", "alerta")

def punto_j(arbol):
    """j. Elimina del árbol a las criaturas "Basilisco" y "Sirenas"."""
    imprimir_subtitulo("j. Eliminando criaturas")
    for nombre in ["Basilisco", "Sirenas"]:
        # Usamos el método delete del árbol.
        valor, _ = arbol.delete(nombre)
        if valor:
            imprimir_mensaje(f"'{valor}' ha sido eliminado del árbol.", "info")
        else:
            imprimir_mensaje(f"No se pudo eliminar a '{nombre}' (no encontrado).", "error")

def punto_k(arbol):
    """k. Modifica el nodo de las Aves del Estínfalo."""
    imprimir_subtitulo("k. Modificando a las Aves del Estínfalo")
    # Buscamos el nodo.
    nodo = arbol.search("Aves del Estínfalo")
    if nodo:
        # Modificamos sus campos "derrotado_por" y "descripcion".
        nodo.other_values["derrotado_por"] = "Heracles"
        nodo.other_values["descripcion"] += " Heracles derrotó a varias de ellas como parte de sus doce trabajos."
        imprimir_mensaje("Nodo modificado. Ahora derrotadas por Heracles y descripción actualizada.", "exito")

def punto_l(arbol):
    """l. Modifica el nombre de "Ladón" a "Dragón Ladón"."""
    imprimir_subtitulo("l. Renombrando a Ladón")
    # Para cambiar la clave principal de un nodo, debemos:
    # 1. Eliminar el nodo antiguo, guardando sus datos.
    valor, datos = arbol.delete("Ladón")
    if valor:
        # 2. Modificar el nombre en los datos guardados.
        datos["nombre"] = "Dragón Ladón"
        # 3. Insertar un nuevo nodo con la nueva clave y los datos actualizados.
        arbol.insert("Dragón Ladón", datos)
        imprimir_mensaje("'Ladón' ha sido renombrado a 'Dragón Ladón'.", "exito")

def punto_m(arbol):
    """m. Realiza un listado por nivel del árbol."""
    imprimir_subtitulo("m. Listado por nivel del árbol")
    # El método by_level utiliza una cola para recorrer el árbol nivel por nivel.
    arbol.by_level()

def punto_n(arbol, heroe):
    """n. Muestra todas las criaturas capturadas por un héroe específico."""
    imprimir_subtitulo(f"n. Criaturas capturadas por {heroe}:")
    criaturas_capturadas = []
    # Recorrido inorden para buscar en todo el árbol.
    def capturadas_por(root):
        if root is not None:
            capturadas_por(root.left)
            # Si el campo "capturada_por" coincide con el héroe...
            if root.other_values.get("capturada_por") == heroe:
                # ...se agrega a la lista de resultados.
                criaturas_capturadas.append(root.value)
            capturadas_por(root.right)
    capturadas_por(arbol.root)
    
    if criaturas_capturadas:
        for c in criaturas_capturadas:
            print(f"   - {c}")
    else:
        imprimir_mensaje(f"{heroe} no ha capturado ninguna criatura.", "info")

# --- FUNCIÓN PRINCIPAL ---
def main():
    """Función principal que orquesta la ejecución de todos los puntos del ejercicio."""
    imprimir_titulo("Mitología Griega: Criaturas y Héroes")
    punto_a(arbol_criaturas)
    punto_b(arbol_criaturas)
    punto_c(arbol_criaturas, "Talos")
    punto_d(arbol_criaturas)
    punto_e(arbol_criaturas, "Heracles")
    punto_f(arbol_criaturas)
    punto_h(arbol_criaturas)
    punto_i(arbol_criaturas, "Cer")
    punto_j(arbol_criaturas)
    punto_k(arbol_criaturas)
    punto_l(arbol_criaturas)
    punto_m(arbol_criaturas)
    punto_n(arbol_criaturas, "Heracles")
    imprimir_separador()

# --- PUNTO DE ENTRADA DEL SCRIPT ---
# Este bloque de código se ejecuta solo si este archivo es el programa principal
# y no si es importado desde otro script.
if __name__ == "__main__":
    main()
