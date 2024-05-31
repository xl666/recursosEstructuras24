def llenar_lista (n):
    for i in range(n):
        lista.append(input())
    return lista

def contar (listaa):
    diccionario={}
    for palabra in listaa:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario



if __name__=='__main__':
    lista=[]
    n=int(input())
    listaa=llenar_lista(n)
    print (contar(listaa))