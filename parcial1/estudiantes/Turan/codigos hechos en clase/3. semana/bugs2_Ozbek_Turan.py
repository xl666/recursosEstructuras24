
# Regresa el valor que está a la mitad de la lista de números
# Si el número de elementos es par, regresar la suma
# del dos números a la mitad
# Si algún elemento no es un número, se regresa None
def regregar_valor_mitad(lista):
    mitad = len(lista)//2 #convertiendo la expresion en integre
    for x in lista: #buscando string en la lista
        if isinstance(x , str):
            return None
    
    if len(lista) % 2 != 0: #Corregiendo la expresion logica con != lugar de ==.
        return lista[mitad]
    
    elif not lista: #Agregando la lista vacia
        return None
    else:
        suma = (lista[mitad]) + (lista[mitad - 1]) #Hay que restar -1 por como comienza el indice desde 0
        return suma
 

# Pruebas, deben pasar todas
print(regregar_valor_mitad([1, 2, 3]) == 2)
print(regregar_valor_mitad([5]) == 5)
print(regregar_valor_mitad([]) == None)
print(regregar_valor_mitad([1, 2]) == 3) #Profe, por culpa de esa letra estuve trabajando como 3 horas aqui.
print(regregar_valor_mitad([1, 2, 3, 4, 5, 6]) == 7)
print(regregar_valor_mitad([1, 'hola', 3]) == None)
print(regregar_valor_mitad([1, 2, 3, 4, 5, 'hola']) == None)
