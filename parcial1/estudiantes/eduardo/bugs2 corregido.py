
def regregar_valor_mitad(lista):
    mitad = len(lista) // 2                #debe ser //, porque si es / da float y no pide float
    if len(lista) % 2 == 0:
        return lista[mitad - 1] + lista[mitad]   #se modifica la operacion para que sea resta y se cambia de lugar
    else:
          return lista[mitad]       #se cambia de lugar el return lista y el return lista con las operaciones

numeros = int(input('escribe la cantidad de numeros a introducir'))  
numeroslista = []

try:                                       
    numeros = int(numeros)
    if numeros == 0:
        print('None')
        exit()

    for i in range(numeros):
        numero = input()
        numeroslista.append(int(numero))

    if not numeroslista:  
        print("None")
    else:
        resultado = regregar_valor_mitad(numeroslista)
        print(resultado)

except ValueError:
    print("None")

print(regregar_valor_mitad([1, 2, 3]) == 2)
print(regregar_valor_mitad([5]) == 5)
print(regregar_valor_mitad([]) == None)
print(regregar_valor_mitad([1, 2]) == 3)  #se corrige regregar en vez de regresar
print(regregar_valor_mitad([1, 2, 3, 4, 5, 6]) == 7)
print(regregar_valor_mitad([1, 'hola', 3]) == None)
print(regregar_valor_mitad([1, 2, 3, 4, 5, 'hola']) == None)