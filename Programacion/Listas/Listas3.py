"""Llenar un arreglo con la serie de Fibonacci, con la cantidad de dígitos que el usuario
indique al inicio del programa"""

def fib(x):
    a=0
    b=1
    for y in range(x):
        c=a+b
        a = b 
        b =c 
        
    return b

num=int(input("Ingrese la cantidad de digitos: "))
a=[]

for z in range(num):
    a.append(fib(z))
    
print(a)
