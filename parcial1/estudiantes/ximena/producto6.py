# Dada una lista de números enteros, crea un programa que devuelve el producto de todos los números, esto es, multiplica cada número de la lista entre si y devuelve el resultado acumulado.
def pl(numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

n = int(input())
print()

numeros = []

for _ in range(n):
    numero = int(input())
    numeros.append(numero)

rf = pl(numeros)

print(rf)
