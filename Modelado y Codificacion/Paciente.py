from Iniciosesion import InicioSesion
class Paciente(InicioSesion):
    
    def __init__(self,cita_hora,):
        self.__cita_hora=cita_hora
    def setcitahora(self,cita_hora):
        self.__cita_hora=cita_hora
    def getcitahora(self):
        return self.__cita_hora
    
    def Hora_Fecha(self, cita_fecha):
        if  cita_fecha and [cita_fecha] == cita_fecha:
            print(f"Su cita para el {cita_fecha}  ha sido agendada.")
            return True
        else:
            print("No fue posible agendar la cita médica.")
            return False


    def Especilista(self,especialidades):
      
        especialidades = ["Cardiología", "Dermatología", "Ginecología", "Oftalmología", "Pediatría"]
        print("Especialidades disponibles:")
        contador=1
        for especialidad in especialidades:
            print(f"{contador}. {especialidad}")   
            contador+=1
        continuar=True
        while continuar :
            print("") 
            opcion = int(input("Ingrese el número de la especialidad que desea consultar: "))
            # Verificamos si el número de opción es válido
            if opcion >= 1 and opcion <= len(especialidades):
                especialidad_elegida = especialidades[opcion-1]
                print(f"Ha seleccionado la especialidad de {especialidad_elegida}.")
                return True
            else:
                print("Opción inválida. Por favor, ingrese un número válido.")
                return None
            break
       

    def Consultorio(self, Consultorio):
        Consultorio = ["1011", "1012", "1013", "1014", "1014"]
        print("Consultorios disponibles:")
        contador=1
        for Consul in Consultorio:
            print(f"{contador}. {Consul}")   
            contador+=1
        continuar=True
        while continuar :
            print("") 
            opcion = int(input("Ingrese el número del consultorio al que desea asistir: "))
            # Verificamos si el número de opción es válido
            if opcion >= 1 and opcion <= len(Consultorio):
                Consultorio_elegido = Consultorio[opcion-1]
                print(f"Ha seleccionado el Consultorio numero: {Consultorio_elegido }.")
                return True
            else:
                print("Opción inválida. Por favor, ingrese un número válido.")
                return None
            break
       


        

