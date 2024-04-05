
# Regresa el valor que está a la mitad de la lista de números
# Si el número de elementos es par, regresar la suma
# del dos números a la mitad
# Si algún elemento no es un número, se regresa None
def regresar_valor_mitad(lista):
    try:
        mitad = len(lista) // 2
        if len(lista) == 0:
            return None
        elif len(lista) % 2 == 0:
            return lista[mitad - 1] + lista[mitad] 
        else:
            return lista[mitad]
    
    except TypeError:
        return None 

# Pruebas, deben pasar todas
print(regresar_valor_mitad([1, 2, 3]) == 2)
print(regresar_valor_mitad([5]) == 5)
print(regresar_valor_mitad([]) == None)
print(regresar_valor_mitad([1, 2]) == 3)
print(regresar_valor_mitad([1, 2, 3, 4, 5, 6]) == 7)
print(regresar_valor_mitad([1, 'hola', 3]) == None)
print(regresar_valor_mitad([1, 2, 3, 4, 5, 'hola']) == None)

