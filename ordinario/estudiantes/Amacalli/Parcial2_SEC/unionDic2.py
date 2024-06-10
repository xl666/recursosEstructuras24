def leerDic(n, m):
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
    dic1, dic2 = leerDic(n, m)
    final = dic1.copy()
    for llave, valor in dic2.items():
        if llave in dic1:
            valor = dic2[llave]
            final[llave] = final[llave] + valor
        else:
            final[llave] = valor
    return final

def formato(n, m):
    diccionario = sumar(n, m)
    ordenar = {key: diccionario[key] for key in sorted(diccionario)}
    plantilla = '%s: %s'
    for llave, valor in ordenar.items():
        print(plantilla % (llave, valor))


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    formato(n, m)
    #print(sumar(n, m))