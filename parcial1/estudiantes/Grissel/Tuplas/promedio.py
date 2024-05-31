def calcular_promedio(tupla):
    return sum(tupla) / len(tupla)

if __name__ == "__main__":
    numeros = (10, 20, 30, 40, 50)
    promedio = calcular_promedio(numeros)
    print("El promedio de la tupla es:", promedio)
