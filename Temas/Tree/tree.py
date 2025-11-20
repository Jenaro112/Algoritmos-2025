from typing import Any, Optional
from queue_ import Queue

class BinaryTree:
    """
    Representa un Árbol Binario de Búsqueda Auto-balanceable (AVL).
    - Los valores menores se insertan a la izquierda.
    - Los valores mayores o iguales se insertan a la derecha.
    - Mantiene su altura balanceada para optimizar las operaciones.
    """

    class __nodeTree:
        """
        Clase interna que representa un nodo dentro del árbol.
        Cada nodo contiene un valor principal, datos adicionales, y punteros
        a sus hijos izquierdo y derecho.
        """

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            """
            Inicializa un nuevo nodo del árbol.
            """
            self.value = value
            self.other_values = other_values
            self.left = None
            self.right = None
            self.hight = 0

    def __init__(self):
        """
        Inicializa un árbol binario vacío.
        """
        self.root = None

    def insert(self, value: Any, other_values: Optional[Any] = None):
        """
        Inserta un nuevo valor en el árbol de forma recursiva y lo balancea.
        """
        def __insert(root, value, other_values):
            # Caso base: si el nodo actual es nulo, hemos encontrado la posición para insertar.
            if root is None:
                return BinaryTree.__nodeTree(value, other_values)
            # Si el valor es menor, vamos por la rama izquierda.
            elif value < root.value:
                root.left = __insert(root.left, value, other_values)
            # Si el valor es mayor o igual, vamos por la rama derecha.
            else:
                root.right = __insert(root.right, value, other_values)

            # Después de insertar, balancea el árbol desde el nodo actual hacia arriba.
            root = self.auto_balance(root)
            # Actualiza la altura del nodo.
            self.update_hight(root)

            return root

        # Inicia el proceso de inserción desde la raíz del árbol.
        self.root = __insert(self.root, value, other_values)

    def pre_order(self):
        """
        Realiza un recorrido en pre-orden (Raíz, Izquierda, Derecha).
        """
        def __pre_order(root):
            if root is not None:
                print(root.value, root.other_values, root.hight)
                __pre_order(root.left)
                __pre_order(root.right)

        # Inicia el recorrido desde la raíz.
        if self.root is not None:
            __pre_order(self.root)

    def in_order(self):
        """
        Realiza un recorrido en in-orden (Izquierda, Raíz, Derecha).
        Para un Árbol Binario de Búsqueda, esto lista los elementos en orden ascendente.
        """
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                print(root.value, root.other_values)
                __in_order(root.right)

        # Inicia el recorrido desde la raíz.
        if self.root is not None:
            __in_order(self.root)

    def post_order(self):
        """
        Realiza un recorrido en post-orden (Izquierda, Derecha, Raíz).
        """
        def __post_order(root):
            if root is not None:
                __post_order(root.right)
                print(root.value)
                __post_order(root.left)

        # Inicia el recorrido desde la raíz.
        if self.root is not None:
            __post_order(self.root)

    def search(self, value: Any) -> __nodeTree:
        """
        Busca un valor específico en el árbol.

        Returns:
            __nodeTree: El nodo si se encuentra, de lo contrario None.
        """
        def __search(root, value):
            if root is not None:
                # Si el valor coincide, hemos encontrado el nodo.
                if root.value == value:
                    return root
                # Si el valor buscado es menor, buscamos en el subárbol izquierdo.
                elif root.value > value:
                    return __search(root.left, value)
                # Si es mayor, buscamos en el subárbol derecho.
                else:
                    return __search(root.right, value)

        aux = None
        # Inicia la búsqueda desde la raíz.
        if self.root is not None:
            aux = __search(self.root, value)
        return aux

    def proximity_search(self, value: Any) -> __nodeTree:
        """
        Busca y muestra todos los nodos cuyo valor comienza con un prefijo dado.
        Recorre todo el árbol para encontrar todas las coincidencias.
        """
        def __search(root, value):
            if root is not None:
                # Si el valor del nodo comienza con el prefijo, lo imprime.
                if root.value.startswith(value):
                    print(root.value)
                # Continúa la búsqueda en ambos subárboles.
                __search(root.left, value)
                __search(root.right, value)

        aux = None
        # Inicia la búsqueda desde la raíz.
        if self.root is not None:
            aux = __search(self.root, value)
        return aux

    def delete(self, value: Any):
        """
        Elimina un valor del árbol y lo rebalancea.
        """
        def __replace(root):
            """Función auxiliar para encontrar el nodo que reemplazará al eliminado (el mayor del subárbol izquierdo)."""
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            """Función recursiva para encontrar y eliminar el nodo."""
            delete_value = None
            deleter_other_values = None
            if root is not None:
                # Búsqueda del nodo a eliminar.
                if value < root.value:
                    root.left, delete_value, deleter_other_values = __delete(root.left, value)
                elif value > root.value:
                    root.right, delete_value, deleter_other_values = __delete(root.right, value)
                else:
                    delete_value = root.value
                    deleter_other_values = root.other_values
                    # Caso 1: El nodo a eliminar no tiene hijo izquierdo.
                    if root.left is None:
                        root = root.right
                    # Caso 2: El nodo a eliminar no tiene hijo derecho.
                    elif root.right is None:
                        root = root.left # Corregido: debería ser root = root.left
                    # Caso 3: El nodo tiene dos hijos.
                    else:
                        # Se busca el nodo reemplazante (el mayor del subárbol izquierdo).
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        root.other_values = replace_node.other_values

                # Se rebalancea y actualiza la altura después de la eliminación.
                root = self.auto_balance(root)
                self.update_hight(root)
            return root, delete_value, deleter_other_values

        delete_value = None
        deleter_other_values = None
        if self.root is not None:
            self.root, delete_value, deleter_other_values = __delete(self.root, value)
        
        return delete_value, deleter_other_values
    
    def by_level(self):
        """
        Muestra el árbol nivel por nivel, como si lo leyeras de arriba hacia abajo
        y de izquierda a derecha. Utiliza una cola para lograrlo.
        """
        # 1. Creamos una "fila de espera" (una cola) para saber qué nodos visitar.
        tree_queue = Queue()
        # 2. Si el árbol no está vacío, ponemos el primer nodo (la raíz) en la fila.
        if self.root is not None:
            tree_queue.arrive(self.root)

            # 3. Mientras queden nodos en la fila de espera...
            while tree_queue.size() > 0:
                # 4. Sacamos el primer nodo de la fila para procesarlo.
                node = tree_queue.attention()
                # 5. Mostramos el valor del nodo que acabamos de sacar.
                print(node.value)
                # 6. Si este nodo tiene hijos, los ponemos al final de la fila para visitarlos después.
                if node.left is not None: 
                    tree_queue.arrive(node.left)
                if node.right is not None:
                    tree_queue.arrive(node.right)

    def hight(self, root):
        """
        Devuelve la altura de un nodo. Si el nodo es None, la altura es -1.
        """
        if root is None:
            return -1
        else:
            return root.hight

    def update_hight(self, root):
        if root is not None:
            """
            Recalcula la altura de un nodo basándose en la altura máxima de sus hijos.
            """
            alt_left = self.hight(root.left)
            alt_right = self.hight(root.right)
            root.hight = max(alt_left, alt_right) + 1

    def simple_rotation(self, root, control):
        """
        Realiza una rotación simple (derecha o izquierda).
        Imagina que "subes" un nodo hijo para que ocupe el lugar de su padre,
        y el padre "baja" para convertirse en hijo, reacomodando el árbol.
        """
        if control: # Rotación Simple a la Derecha (el hijo izquierdo sube)
            aux = root.left
            root.left = aux.right
            aux.right = root
        else: # Rotación Simple a la Izquierda (el hijo derecho sube)
            aux = root.right
            root.right = aux.left
            aux.left = root

        # Después de mover los nodos, recalculamos sus alturas.
        self.update_hight(root)
        self.update_hight(aux)
        
        # 'aux' es ahora la nueva raíz de esta parte del árbol.
        root = aux
        return root

    def double_rotation(self, root, control):
        """
        Realiza una rotación doble. Es un movimiento de dos pasos para
        corregir desbalances más complejos que una rotación simple no puede arreglar.
        """
        if control: # Rotación Doble a la Derecha
            # 1. Primero, hacemos una rotación simple a la IZQUIERDA en el hijo izquierdo.
            #    Esto "alinea" el desbalance para poder corregirlo.
            root.left = self.simple_rotation(root.left, False)
            # 2. Luego, hacemos la rotación simple a la DERECHA en el nodo original.
            root = self.simple_rotation(root, True)
        else:
            # 1. Primero, hacemos una rotación simple a la DERECHA en el hijo derecho.
            root.right = self.simple_rotation(root.right, True)
            # 2. Luego, hacemos la rotación simple a la IZQUIERDA en el nodo original.
            root = self.simple_rotation(root, False)
        
        return root

    def auto_balance(self, root):
        """
        Verifica el factor de balanceo de un nodo y aplica las rotaciones
        necesarias para mantener el árbol balanceado (AVL).
        """
        if root is not None:
            # Si el subárbol izquierdo es más alto (desbalance hacia la izquierda).
            if self.hight(root.left) - self.hight(root.right) == 2:
                # Si el desbalance es causado por el hijo izquierdo (Rotación Simple).
                if self.hight(root.left.left) >= self.hight(root.left.right):
                    root = self.simple_rotation(root, True)
                # Si el desbalance es causado por el hijo derecho del hijo izquierdo (Rotación Doble).
                else:
                    root = self.double_rotation(root, True)
            # Si el subárbol derecho es más alto (desbalance hacia la derecha).
            if self.hight(root.right) - self.hight(root.left) == 2:
                # Si el desbalance es causado por el hijo derecho (Rotación Simple).
                if self.hight(root.right.right) >= self.hight(root.right.left):
                    root = self.simple_rotation(root, False)
                # Si el desbalance es causado por el hijo izquierdo del hijo derecho (Rotación Doble).
                else:
                    root = self.double_rotation(root, False)
        return root

    # --- Métodos específicos para problemas concretos ---

    def villain_in_order(self):
        """
        Recorrido in-order que imprime solo los nodos marcados como villanos.
        """
        def __villain_in_order(root):
            if root is not None:
                __villain_in_order(root.left)
                if root.other_values["is_villain"] is True:
                    print(root.value)
                __villain_in_order(root.right)

        if self.root is not None:
            __villain_in_order(self.root)

    def count_heroes(self):
        """
        Cuenta recursivamente el número de nodos marcados como héroes.
        """
        def __count_heroes(root):
            count = 0
            if root is not None:
                if root.other_values["is_villain"] is False:
                    count += 1
                count += __count_heroes(root.left)
                count += __count_heroes(root.right)

            return count

        total = 0
        if self.root is not None:
            total = __count_heroes(self.root)
        
        return total
    
    def divide_tree(self, arbol_h, arbol_v):
        """
        Recorre el árbol actual y distribuye sus nodos en otros dos árboles:
        uno para héroes (arbol_h) y otro para villanos (arbol_v).
        """
        def __divide_tree(root, arbol_h, arbol_v):
            if root is not None:
                if root.other_values["is_villain"] is False:
                    arbol_h.insert(root.value, root.other_values)
                else:
                    arbol_v.insert(root.value, root.other_values)
                __divide_tree(root.left, arbol_h, arbol_v)
                __divide_tree(root.right, arbol_h, arbol_v)


        __divide_tree(self.root, arbol_h, arbol_v)
    
    def in_order_height(self):
        """
        Recorrido in-order que imprime nodos cuya altura (height) es mayor a 100.
        """
        def __in_order_height(root):
            if root is not None:
                __in_order_height(root.left)
                if root.other_values['height'] > 100:
                    print(root.value, root.other_values['height'])
                __in_order_height(root.right)

        if self.root is not None:
            __in_order_height(self.root)
    
    def in_order_weight(self):
        """
        Recorrido in-order que imprime nodos cuyo peso (weight) es menor a 75.
        """
        def __in_order_weight(root):
            if root is not None:
                __in_order_weight(root.left)
                if root.other_values['weight'] < 75:
                    print(root.value, root.other_values['weight'])
                __in_order_weight(root.right)

        if self.root is not None:
            __in_order_weight(self.root)

arbol = BinaryTree()
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()
