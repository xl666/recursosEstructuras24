def numMayor (lista): #defino mi funcion numero mayor
    mayor = lista[0] #aquí creo mi lista con 0
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor 
cantNumeros = int(input()) #Solicito la cantidad de numeros que no se cuantos son 
if cantNumeros > 0:
    numeros = [int(input()) for i in range(cantNumeros)]
    mayor = numMayor(numeros)
    print(mayor)

