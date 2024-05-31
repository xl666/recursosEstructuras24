def pertenece(lista, elem):
    for i in range(len(lista)):
        if (lista[i] == elem):
            return True

def tieneRepetido(lista):
    for i in range(len(lista)):
        if (pertenece(lista[i+1:], lista[i])):
            return True
    return False 

if __name__ == '__main__':
    lista = [10, 20, 30, 40, 20]
    print(pertenece(lista, 20))
    print(tieneRepetido(lista))