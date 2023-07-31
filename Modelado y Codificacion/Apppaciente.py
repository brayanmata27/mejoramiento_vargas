from Iniciosesion import InicioSesion
from Paciente import Paciente
from Medico import Medico


usuarios_registrados = {
        "Manuel": "12345",
        "Raul": "contrasena",
        "Manuel": "12345",
        "Jose": "12345",
     
    }
inicio_sesion = InicioSesion(usuarios_registrados)

cita_hora={
        1:"1.cita medicina general 25 de julio, Hora: 14:00",
        2:"2.cita medicina general 28 de julio, Hora: 09:00",
        3:"3.cita medicina general 29 de julio, Hora: 10:00",
        4:"4.cita medicina general 01 de agosto, Hora: 15:00",
        5:"5.cita medicina general 05 de agosto, Hora: 13:00",
    }
hora=Paciente(cita_hora )

especialidades = ["Cardiología", "Dermatología", "Ginecología", "Oftalmología", "Pediatría"]

especilida=Paciente(especialidades)

Consultorio = ["1011", "1012", "1013", "1014", "1014"]

Consul=Paciente(Consultorio)



def menu():
    print("MENÚ\n")
    print("1. iniciar sesion")
    print("2.mostrar fechas disponibles ")
    print("3.Escoger especialidad")
    print("4.Consultorios Disponibles")
    print("5.ver informacion sobre la cita")
    print("6.Eliminar cita")
    print("7.Finalizar")

continuar=True   

while continuar:
    print("")
    menu()
    opcion = input("Ingrese el número de la opción deseada: ")
    print("")

    if opcion == "1":
        nombre=[]
        usuario_ingresado = input("Ingresa tu nombre de usuario: ")
        contrasena_ingresada = input("Ingresa tu contraseña: ")
        inicio_sesion.verificar_credenciales(usuario_ingresado, contrasena_ingresada)
        nombre.append(usuario_ingresado)
    elif opcion == "2":
        q=cita_hora[1]
        a=cita_hora[2]
        b=cita_hora[3]
        c=cita_hora[4]
        d=cita_hora[5]

        print(q)
        print(a)
        print(b)
        print(c)
        print(d)
        i=[]
        cita=(input("digite cual cita medica desea adquirir"))
        hora.Hora_Fecha(cita)
        i.append(cita)
    elif opcion =="3":
        e=[]
        espe=(input("digite que especilidad desea:"))
        especilida.Especilista(espe)
        e.append(especilida)
    elif opcion == "4":
        cons=[]
        con=(input("Ya elijio la especialidad?:"))
        if con == "si":
            Consul.Consultorio(Consultorio)
            con=(input("Ingrese el numero del consultorio para almacenar la informacion"))
            cons.append(con)
        elif con=="no":
            print("debe escoger primero una especilidad")
        else:
            print("No es una respuesta valida")

    elif opcion == "5":
        print(f"nombre de usuario{nombre[0]} tipo y hora {i[1]} tipo de especialidad {e[2]}consultorio {cons[3]}")

    elif opcion == "6":
        print(f"las citas agendadas son {nombre,i,e,cons}")
        p=(input("Desea borrar la cita medica?:"))
        if p == "si":
           print("la cita se elimino correctamente")
        else:
            print("la cita no se pudo eliminar porque excedio el tiempo limite de dos horas ") 
    else :
        opcion == "7"
        print ("Se cerro el inicio de sesion, vuelva pronto")
        break
        
    