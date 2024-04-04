def funcionmayor():
    lista = []
    numero_elementos = int(input()) 

   
    for _ in range(numero_elementos):
        lista.append(int(input()))

    nummayor = lista[0]  

    
    for i in range(1, numero_elementos):  
        if lista[i] > nummayor: 
            nummayor = lista[i] 

    return nummayor 

print(funcionmayor())


#Version del Maestro 
elementos=int(input())
def leer_lista(elementos):
    lista_resultado.append(int(input()))
    return lista_resultado

def mayor_lista(lista):
    if not lista: #si la lista esta vacia if len(lista) == 0
     return None
    mayor= lista[0]
    for elemento in lista: #pero para mejoarar el codigo lista[1:] "significa slicing, desde 1" o list(range (1,5)) apartir de [1,2,3,4]
        if elemento > mayor:
            mayor=elemento
    return mayor 
lista_numeros=leer_lista(elementos)
print(mayor_lista(lista_numeros)) #(mayor_lista(leer_lista(elementos)))
