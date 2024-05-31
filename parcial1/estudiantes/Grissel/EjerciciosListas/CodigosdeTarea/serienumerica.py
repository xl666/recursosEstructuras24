serie_numerica = int(input())

def encontrar_posicion(elemento):
    num1 = 0
    num2 = 1
    
    for _ in range(elemento):
        num3 = num2+num1
        num1 = num2
        num2 = num3     
    return num1

print(encontrar_posicion(serie_numerica))
