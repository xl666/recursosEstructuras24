def ganadores1(cadena_1, suma2 = 0):
    diccionario = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J':11, 'Q':12, 'K':13, 'A':14}
    for carta in cadena_1:
        valor = diccionario[carta]
        suma2 += valor
    return suma2

def ganadores2(cadena_2, suma2 = 0):
    diccionario = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J':11, 'Q':12, 'K':13, 'A':14}
    for carta in cadena_2:
        valor = diccionario[carta]
        suma2 += valor
    return suma2
        
if __name__ == '__main__':
    jugador_c1 = input()
    jugador_c2 = input()
    cadena_1 = input()
    cadena_2 = input()
    if ganadores1(cadena_1) > ganadores2(cadena_2):
        print(jugador_c1)
    if ganadores2(cadena_2) > ganadores1(cadena_1):
        print(jugador_c2)
    if ganadores1(cadena_1) == ganadores2(cadena_2):
        print('empate')