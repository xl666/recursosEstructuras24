def leerDic(n, m):
    """
    En esta funcion se leen cada uno de los elementos (llave, valor) y 
    se guardan en su respectivo diccionario, luego se retorna para su uso
    """
    dic1 = {}
    dic2 = {}
    for _ in range(n):
        llave = input()
        valor = int(input())
        dic1[llave] = valor
    
    for _ in range(m):
        llave = input()
        valor = int(input())
        dic2[llave] = valor
    
    return dic1, dic2

def sumar(n,m):
    """
    En esta funcion se manda a llamar la función 'leerDic' para usarlos, después
    se hace una copia del diccionario 1 y se recorre el diccionario 2. Las llaves
    que ya se encuentran en el diccionario 1 cambian los valores por la suma
    de ambos y los valores que no es encuentra se agregan y se retorna el diccionario final
    """
    dic1, dic2 = leerDic(n, m)
    final = dic1.copy()
    for llave, valor in dic2.items():
        if llave in final:
            valor = dic2[llave]
            final[llave] = final[llave] + valor
        else:
            final[llave] = valor
    return final

def formato(n, m):
    """
    En esta funcion se manda a llamar la funcion 'sumar' para tener el diccionario final
    despues se ordena el diccionario, se crea la plantilla de impresión y al final se 
    recorre el diccionario y se va imprimiendo de acuerdo a lo especificado en la plantilla
    """
    diccionario = sumar(n, m)
    ordenar = {key: diccionario[key] for key in sorted(diccionario)}
    plantilla = '%s: %s'
    for llave, valor in ordenar.items():
        print(plantilla % (llave, valor))

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    formato(n, m)