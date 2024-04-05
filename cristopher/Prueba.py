
def Llenar(Entrada):
    global Lista
    Lista = []
    for elemento in range(Entrada):
        Lista.append(str(input()))
    
    return Lista

if __name__ == '__main__':
    Entrada = int(input())
    print(Llenar(Entrada))
    