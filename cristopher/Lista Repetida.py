def Repetidos(Lista):
    for caracter in Lista:
        if Lista.count(caracter) > 1:
            return True
        else:
            return False

if __name__ == '__main__':
    Lista = []
    Entrada = int(input())
    for cantidad in range(Entrada):
        Lista.append(int(input()))
    print(Repetidos(Lista))