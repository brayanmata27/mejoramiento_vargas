def Ncifras():
    n = float(input("Ingrese numero entre 0 y 100: "))
    if n < 0 or n > 1000:
        print("El numero ingresado sobrepasa los limites.")
    else:
        cifras = 1
        while n >= 10:
            cifras += 1
            n //= 10
        print("El número tiene", cifras, "cifras.")
Ncifras()