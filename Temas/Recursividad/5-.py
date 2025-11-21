# --- IMPORTACIONES DE LIBRERÍAS ---
# Importamos tu librería `colores` para dar estilo a la salida en consola.
# Importamos la librería `re` (Regular Expressions) para validar el formato del número romano.
import colores
import re

def Romano_a_decimal(romano):
    """
    Función principal que convierte un número romano a decimal.
    Contiene dos funciones anidadas: una para validar y otra para convertir, ambas recursivas.
    """
    # Diccionario que mapea cada símbolo romano a su valor decimal.
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
    }
    
    # Convierte la entrada a mayúsculas para un manejo uniforme.
    romano = romano.upper()
    
    # Primera validación: si la cadena está vacía, lanza un error.
    if not romano:
        raise ValueError(colores.color("[x] Nada ingresado", colores.ROJO))
    
    def validar(indice):
        """
        Función anidada y recursiva para validar el formato del número romano.
        """
        # --- CASO BASE DE LA RECURSIÓN ---
        # Si el índice supera la longitud de la cadena, hemos revisado todo y es válido.
        if indice >= len(romano):
            return True

        # --- VALIDACIONES EN CADA PASO RECURSIVO ---
        # 1. Validación de repeticiones inválidas usando una expresión regular.
        #    - No se puede repetir más de 3 veces I, X, C, M.
        #    - No se pueden repetir V, L, D.
        patron = r"(IIII|XXXX|CCCC|MMMM|VV|LL|DD)"
        if re.search(patron, romano):
            raise ValueError(colores.color("[*] Formato inválido", colores.ROJO))

        # 2. Validación de que cada carácter sea un símbolo romano válido.
        if romano[indice] not in valores:
            raise ValueError(colores.color(f"[*] Carácter invalido en número romano: '{romano[indice]}'", colores.ROJO))
        
        # --- LLAMADA RECURSIVA ---
        # Se llama a sí misma para validar el siguiente carácter de la cadena.
        return validar(indice + 1)
    
    # Se inicia la validación desde el primer carácter (índice 0).
    validar(0)
    
    def convertir(indice):
        """
        Función anidada y recursiva que realiza la conversión a decimal.
        """
        # --- CASO BASE DE LA RECURSIÓN ---
        # Si el índice alcanza el final de la cadena, no hay más que sumar.
        if indice == len(romano):
            return 0
        
        # --- LÓGICA EN CADA PASO RECURSIVO ---
        # Se obtiene el valor decimal del símbolo en la posición actual.
        actual = valores[romano[indice]]
        
        # Se comprueba si hay un símbolo siguiente para aplicar la regla de sustracción.
        if indice + 1 < len(romano):
            siguiente = valores[romano[indice + 1]]
            
            # Si el valor actual es menor que el siguiente (ej: 'I' antes de 'X' en "IX")...
            if actual < siguiente:
                # ...se resta el valor actual y se continúa la conversión desde el siguiente índice.
                return -actual + convertir(indice + 1)
        
        # Si no hay regla de sustracción, se suma el valor actual y se continúa la conversión.
        return actual + convertir(indice + 1)

    # Se inicia la conversión desde el primer carácter (índice 0).
    return convertir(0)

# --- FUNCIÓN PRINCIPAL ---
def main():
    """Función principal que maneja la interacción con el usuario."""
    entrada = input(colores.color("[*] Ingresa un numero romano: ", colores.VERDE))
    try:
        # Intenta realizar la conversión.
        resultado = Romano_a_decimal(entrada)
        print(colores.color(f"[*] El numero romano ingresado en decimal es '{resultado}'", colores.AMARILLO))
    except ValueError as e:
        # Si ocurre un error de validación (ValueError), lo captura y muestra el mensaje.
        print(colores.color(f"Error: '{e}'", colores.ROJO))
        
# --- PUNTO DE ENTRADA DEL SCRIPT ---
# Este bloque se ejecuta solo si el archivo es el programa principal.
if __name__ == "__main__":
    main()