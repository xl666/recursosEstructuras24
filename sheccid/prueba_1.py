def regresar_valor_mitad(lista):
    if not all(isinstance(x, (int, float)) for x in lista):
        return None
    if not lista:
        return None
    mitad = len(lista) // 2
    if len(lista) % 2 == 0:
        return lista[mitad - 1] + lista[mitad]
    else:
        return lista[mitad]

# Pruebas, deben pasar todas
print(regresar_valor_mitad([1, 2, 3]) == 2)
print(regresar_valor_mitad([5]) == 5)
print(regresar_valor_mitad([]) == None)
print(regresar_valor_mitad([1, 2]) == 3)
print(regresar_valor_mitad([1, 2, 3, 4, 5, 6]) == 7)
print(regresar_valor_mitad([1, 'hola', 3]) == None)
print(regresar_valor_mitad([1, 2, 3, 4, 5, 'hola']) == None)


