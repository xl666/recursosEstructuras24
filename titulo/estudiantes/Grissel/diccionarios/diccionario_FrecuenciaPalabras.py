def contar_palabras(partes, diccionario):
    for palabra in partes:
        frecuencia = partes.count(palabra)
        diccionario[palabra] = frecuencia
    
def crear_diccionario(diccionario, lista):
    lista.sort()
    for palabra in lista:
        diccionario[palabra] = 0

def quita_repetidas(lista):
    lista_nueva=[]
    for _ in lista:
        if _ not in lista_nueva:
            lista_nueva.append(_)
    return lista_nueva
    
if __name__ == '__main__':
    diccionario = {}
    palabras = input()
    partes = palabras.split(' ')
    lista_palabras = partes.copy()
    lista_palabras = quita_repetidas(lista_palabras)
    # print(lista_palabras)
    crear_diccionario(diccionario, lista_palabras)
    contar_palabras(partes, diccionario)
    print(diccionario)
    #print(diccionario['hola'])
    #diccionario['adios'] = 100
    #print(diccionario['adios'])