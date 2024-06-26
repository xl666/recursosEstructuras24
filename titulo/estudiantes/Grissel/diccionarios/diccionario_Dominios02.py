def Dominios(n):
    diccionario = {}
    for _ in range(n):
        llave, dato = input().split(":")
        if llave in diccionario:
            if diccionario[llave] == 1:
                diccionario[llave] += 1
                continue
            diccionario[llave] += 1
            continue
        if dato == "Error":
            continue
        diccionario[llave] = 1
    return diccionario

def Ordenar(diccionario):
    lista = list(diccionario) #Es otra manera de sacar la llaves de un diccionario 
    lista.sort() # A qui las ordeno 
    for llave2 in lista:
        if diccionario[llave2] >= 2:  #verifico si tiene dos OK o mayor a dos
            print(llave2)
    
if __name__ == "__main__":
    n = int(input())
    diccionario = Dominios(n)
    Ordenar(diccionario)
    