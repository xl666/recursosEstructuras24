def contar(palabras: list) -> list:
    """
    En esta función se cuenta la frecuencia de las palabras, 
    guarda en una lista y la retorna
    """
    valores = []
    for palabra in palabras:
        valores.append(palabras.count(palabra))
    return valores

def dic(palabras):
    """
    En esta función volvemos las palabras y los valores en una tupla,
    después se van agregando al diccionario mediante un for y se
    retorna el diccionario
    """
    valores = contar(palabras)
    var = tuple(zip(palabras, valores))
    diccionario = {}
    for llave, valor in var:
        diccionario[llave] = valor
    return diccionario

def formato(palabras):
    """
    En está función primero se ordenan las llaves en orden alfabético
    y después se pone el formato en el que se
    quieren imprimir cada una de las llaves con su valor
    correspondiente
    """
    diccionario = dic(palabras)
    ordenar = {key: diccionario[key] for key in sorted(diccionario)}
    plantilla = '%s: %s'
    for llave, valor in ordenar.items():
        print(plantilla % (llave, valor))

if __name__ == '__main__':
    cadena = input()
    palabras = cadena.split(' ')
    formato(palabras)