def Telefonica():
    min= int(input ("¿Minutos de duracion de la llamada: "))
    if min > 3:
        adicionales= min - 3
        cobroadicional= adicionales*50
        total= cobroadicional + 200
        print ("El total de su pago es ", total, "pesos")
    if min == 3:
        print ("Fue banderazo pague 200 pesos ")
Telefonica()