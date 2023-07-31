from Iniciosesion import InicioSesion
from Medico import Medico
from Apppaciente import nombre,i,cons


usuarios_registrados = {
        "Jose": "12345",
        "Rodriguez": "12345",
        "Miguel": "12345",
        "Ana": "12345",
     
    }
inicio_sesion = InicioSesion(usuarios_registrados)

mi_agenda = Medico()

def mostrar_menu():
    print("----- Menú -----")
    print("1.iniciar sesion")
    print("2. Agendar día")
    print("3. Mostrar días agendados")
    print("4.Consultar nombre del paciente")
    print("5.Consultar motivo de la cita")
    print("6.Consultario de la cita")
    print("8. Salir")

c=True
while c:
    mostrar_menu()
    opcion = input("Ingrese el número de opción: ")

    if opcion =="1":
        usuario_ingresado = input("Ingresa tu nombre de usuario: ")
        contrasena_ingresada = input("Ingresa tu contraseña: ")
        inicio_sesion.verificar_credenciales(usuario_ingresado, contrasena_ingresada)   
    elif opcion == "2":
        dia = input("Ingrese el día a agendar (formato: yyyy-mm-dd): ")
        mi_agenda.agregar_dia(dia)
    elif opcion == "3":
        mi_agenda.mostrar_dias_agendados()
    elif opcion == "4":
        print(f"el nombre del paciente que tiene cita es {nombre}")
    elif opcion == "5":
        print(f"La cita agendada es para {i}")
    elif opcion == "6":
        print (f"el consultorio es {cons}")
    elif opcion == "7":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")






































