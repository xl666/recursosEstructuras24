def CrearLista(numero):
    lista = []
    for i in range(numero):
        num = int(input())
        lista.append(num)
    return lista

def RegresarInterseccion(lista1, lista2):
   
    interseccion = set()
    
   
    for item in lista1:
        for item2 in lista2:
            if item2 - 1 < item <= item2:
                interseccion.add(item)
    
   
    interseccion = sorted(list(interseccion))
    
    return interseccion

var1 = int(input())
var2 = int(input())
lista1 = CrearLista(var1)
lista2 = CrearLista(var2)
print(RegresarInterseccion(lista1, lista2))
