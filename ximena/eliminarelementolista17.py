#Dada una lista de números, elimina todas las ocurrencias de un valor V

#Tip: utiliza comprensiones de listas
#Ejemplo de entrada
#44
#6
#11, 22, 44, 77, 44, 11
#Ejemplo de salida
#[11, 22, 77, 11]
filtro = int(input())

numdeelementos = int(input())

lista = [int(input()) for _ in range(numdeelementos)]

lista = [x for x in lista if x != filtro]

print(lista)