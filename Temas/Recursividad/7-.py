""" Ejercicio 7 """

def serie(x):
    if x == 0:
        return 0
    else:
        return (1/x) + serie(x-1)

result = serie(5)
print(result)