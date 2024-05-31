def regresar_valor_mitad(lista):
    try:
        mitad = len(lista) // 2
        for x in lista:
            if isinstance(x, str):
                return None
       
        if len(lista) % 2 != 0:
            return lista[mitad]
        else:
            suma = lista[mitad] + lista[mitad - 1]
            return suma
    except :
        if not lista:
             return None

# Pruebas
print(regresar_valor_mitad([1, 2, 3]) == 2)
print(regresar_valor_mitad([5]) == 5)
print(regresar_valor_mitad([]) == None)
print(regresar_valor_mitad([1, 2]) == 3)
print(regresar_valor_mitad([1, 2, 3, 4, 5, 6]) == 7)
print(regresar_valor_mitad([1, 'hola', 3]) == None)
print(regresar_valor_mitad([1, 2, 3, 4, 5, 'hola']) == None)