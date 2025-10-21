""" Ejercicio 11 """

def espejo(x,y=0): #* donde X es el numero y Y es el numero ya invertido
    if x == 0 :
        return y
    else:
        y = y * 10 + x % 10
        return espejo(x // 10,y)
    
result = espejo(45)
print(result)