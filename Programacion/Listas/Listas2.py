"""El siguiente arreglo """
import random


def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista

lista1=llenarLista(10,20)
print("La lista 1 es: ",lista1)

lista2=llenarLista(10,20)
print("La lista 2 es: ",lista2)

#b. Cual de los dos tiene el numero mayor 

def mayor(lista):
    max=0
    for i in lista:
        if i>max:
            max=i
    return max

mayor1=mayor(lista1)
print("El mayor de la primera lista es: ",mayor1)

mayor2=mayor(lista2)
print("El mayor de la segunda lista es: ",mayor2)

if mayor1>mayor2:
    print("La primera lista tiene el numero mayor")
elif mayor1==mayor2:
    print("Son iguales")
else:
    print("La segunda lista tiene el numero mayor")

#c. Cual de los dos tiene el numero menor 

def menor(lista):
    min=100000
    for i in lista:
        if i<min:
            min=i
    return min

menor1=menor(lista1)
print("El menor de la primera lista es: ",menor1)

menor2=menor(lista2)
print("El menor de la segunda lista es: ",menor2)

if menor1<menor2:
    print("La primera lista tiene el numero menor")
elif menor1==menor2:
    print("Son iguales")
else:
    print("La segunda lista tiene el numero menor")

