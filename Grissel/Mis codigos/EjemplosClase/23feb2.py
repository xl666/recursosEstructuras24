#BUG2

def todos_son_enteros(lista):
    for elemento in lista:
        try:
            int(elemento)
        except:
            return False
    return True

def regresar_valor_mitad(lista):
    if len(lista) == 0:
        return None
    if not todos_son_enteros(lista):
        return None
    mitad = len(lista)//2
    if len(lista) % 2 == 1:
        return lista[mitad]
    else:
        suma = lista[mitad] + lista[mitad - 1]
        
        return suma

if __name__ == '__main__':
    print(regresar_valor_mitad([1, 2, 3]) == 2)
    print(regresar_valor_mitad([5]) == 5)
    print(regresar_valor_mitad([]) == None)
    print(regresar_valor_mitad([1, 2]) == 3)
    print(regresar_valor_mitad([1, 2, 3, 4, 5, 6]) == 7)
    print(regresar_valor_mitad([1, 'hola', 3]) == None)
    print(regresar_valor_mitad([1, 2, 3, 4, 5, 'hola']) == None)
    print(regresar_valor_mitad([1, 2, 'hola']) == None)