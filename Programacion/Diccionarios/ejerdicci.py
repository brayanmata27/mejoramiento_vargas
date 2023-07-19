def clave(diccionario,animal):
    if animal in diccionario:
        return diccionario[animal]
    else:
        return(f"el animal{animal}no existe en este diccionario")

diccionario={
    "perro":"dog",
    "gato":"cat",
    "caballo":"horse",
    "pajaro":"bird"
}

animal= input ("Digite el animal a buscar en español")

print(clave(diccionario,animal))