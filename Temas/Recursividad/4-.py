""" Ejercicio 4 """

def potencia(x,y): #* X es la base, Y es el exponente
    if y==0:
        return 1
    else:
        return x * potencia(x,y-1)

result = potencia(3,2)
print(result)