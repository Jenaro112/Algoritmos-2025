""" Ejercicio 8 """

def binario(x):
    if x == 0:
        return '0'
    else:
        return binario(x // 2) + str(x % 2)

result = binario(4)
print(result)