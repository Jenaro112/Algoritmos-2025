""" Ejercicio 3 """

def producto(x,y):
    if (x == int(x)) and (y == int(y)):
        return x * y
    else:
        print('-------------------------------------------')
        print('los numeros no son enteros')

result = producto(5,7)
print('-------------------------------------------')
print(f'El producto es {result}')
print('-------------------------------------------')

""" producto(x,y) = producto(x,y-1) --> producto(x,y) y == 1 = x """
