""" Recursividad """

def factorial (number):
    if number == 0: 
        print(f'----------------------------------------------')
        print('llegamos a la condicion de fin')
        return 1
    else:
        print(f'-   resultado parcial: {number}, llamada recursiva con {number - 1}!')
        return number * factorial(number-1) #* llamada recursiva

result = factorial(5)
print(f'----------------------------------------------')
print(f'el resultado del factorial es {result}!!!')

#* Formula general de Fibonacci
#? fib(n) = fib(n-1) + fib(n-2) --> fib(0) = 0 <==> fib(1) = 1
def fib(number):
    if number == 0 or number == 1:
        return number
    else:
        return fib(number-1) + fib(number-2)

print(f'----------------------------------------------')
for i in range(6):
    print(fib(i))