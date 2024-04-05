def regregar_valor_mitad(lista):
    try:
        if len(lista) == 0:
            return None
        mitad = len(lista) // 2
        if len(lista) % 2 == 0:
            return lista[mitad - 1] + lista[mitad]
        else:
            return lista[mitad]
    except TypeError:
        return None


# Pruebas, deben pasar todas
print(regregar_valor_mitad([1, 2, 3]) == 2)
print(regregar_valor_mitad([5]) == 5)
print(regregar_valor_mitad([]) == None)
print(regregar_valor_mitad([1, 2]) == 3)
print(regregar_valor_mitad([1, 2, 3, 4, 5, 6]) == 7)
print(regregar_valor_mitad([1, 'hola', 3]) == None)
print(regregar_valor_mitad([1, 2, 3, 4, 5, 'hola']) == None)
