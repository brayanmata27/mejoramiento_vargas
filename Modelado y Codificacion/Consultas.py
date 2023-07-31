class Consulta:
    def __init__ (self,citas,nombre,fecha,consultorio):
        self.__citas=citas
        self.__nombre=nombre
        self.__fecha=fecha
        self.__consultorio=consultorio

    def setcitas(self,citas):
        self.__citas=citas
    def getcitas(self):
        return self.__citas
    
    def setnombre(self,nombre):
        self.__nombre=nombre
    def getnombre(self):
        return self.__nombre
    
    def setfecha(self,fecha):
        self.__fecha=fecha
    def getfecha(self):
        return self.__fecha
    
    def setconsultorio(self,consultorio):
        self.__consultorio=consultorio
    def getconsultorio(self):
        return self.__consultorio
    