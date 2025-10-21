""" Ejercicio 3 """

def producto(x,y):
    if y == 1:
        return x
    else:
        return x + producto(x,y-1)

resultado = producto(2,3)
print(resultado)
