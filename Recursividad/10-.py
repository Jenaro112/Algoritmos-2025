""" Ejercicio 10 """

def conteo(x):
    if x == 0:
        return 1
    elif abs(x) < 10:
        return 1
    else:
        return 1 + conteo(x // 10)

result = conteo(676543534)
print(result)
