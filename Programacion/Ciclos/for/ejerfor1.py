def divisor():
    d=[]
    x= int(input("ingrese numero:",))
    contador=0
    for i in range (1, x+1):
        if x % i == 0:
            d.append(i)
            contador=contador+1
    if contador<=2:
        print("Es primo")
    else:
        print("No es primo")
    print("Los divisores del numero", x, "Son: ", d)
    print(contador)

divisor()

