#Suma de todos los elementos de una matriz
def suma_valores_matriz(matriz:list)->int:
    suma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            suma+=matriz[i][j]
    return suma
    
#Suma de los elementos de una fila de una matriz
def suma_fila(matriz:list,fila:int)->int:
    suma=0
    for j in range(len(matriz[fila])):
        suma+=matriz[fila][j]
    return suma
    
#Suma de los elementos de una columna de una matriz
def suma_columna(matriz:list,columna:int)->int:
    suma=0
    for i in range(len(matriz)):
        suma+=matriz[i][columna]
    return suma
    
#Indicador de si hay negativo en una matriz
def hay_negativo(matriz:list)->int:
    rta=True
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if(matriz[i][j]<0):
                rta=True
    return rta

#Fila con más ceros
def fila_mas_ceros(matriz:list)->int:
    mayor=0
    cantidad=0
    for i in range(len(matriz)):
        contador=0
        for j in range(len(matriz[i])):
            if(matriz[i][j]==0):
                contador+=1
        if(contador>cantidad):
            mayor=i
            cantidad=contador
    return mayor
    
    
    
#La columna con mayor suma de una matriz
def mayor_col(matriz:list)->tuple:
    mayor = 0
    mayor_Columna=''
    for columna in range(1,len(matriz[0])):
        suma=0
        for i in range(1,len(matriz)):
            suma+=matriz[i][columna]
        if suma > mayor:
            mayor = suma
            mayor_Columna = matriz[0][columna] #matriz[columna][0]
        
    return (mayor_Columna,mayor)
matriz = [ ["","A","B","C"],
["A",2,5,1],
["B",6,5,1],
["C",8,7,9]    ]
print(mayor_col(matriz))

def normalizar(matriz:list)->list:
    for i in range(1,len(matriz)):
        suma = sum(matriz[i][1:])
        for j in range(1,len(matriz[i])):
            matriz[i][j] /= suma
    return matriz
print(normalizar(matriz))