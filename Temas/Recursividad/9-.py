""" Ejercicio 9 """
import math

def serie(a,b):
    if  a == 0 or b == 0:
        return 'no se puede'
    else:
        return math.log(a,b)

result = serie(2,10)
print(result)