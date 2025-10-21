""" Ejercicio 6 """

def secuencia_invertida(x):
    if len(x) == 0:
        return x
    else:
        return x[-1] + secuencia_invertida(x[:-1])
    
secuencia = input("Ingrese la palabra: ")
result = secuencia_invertida(secuencia)
print(result)