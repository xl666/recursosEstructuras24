def encontrar_maximo_minimo(tupla):
    return max(tupla), min(tupla)

if __name__ == "__main__":
    numeros = (10, 5, 30, 15, 20)
    maximo, minimo = encontrar_maximo_minimo(numeros)
    print("Máximo:", maximo)
    print("Mínimo:", minimo)
