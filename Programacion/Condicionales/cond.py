def iguales():
    n1 = int(input("Ingrese número1: "))
    n2 = int(input("Ingrese numero 2: "))
    n3 = int(input("Ingrese número 3: "))
    if n1 == n2 and n1 == n3:
        print("Los números son iguales")
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print("Hay números iguales")
    else:
        print("Los tres números son distintos")

iguales()