from Paciente import *
class Medico:
    def __init__(self):
        self.dias_agendados = []

    def agregar_dia(self, dia):
        self.dias_agendados.append(dia)
        
    def mostrar_dias_agendados(self):
        print("Días agendados:")
        for dia in self.dias_agendados:
            print(dia)
