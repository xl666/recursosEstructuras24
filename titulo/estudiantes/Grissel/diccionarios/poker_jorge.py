diccionario = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J':11, 'Q':12, 'K':13, 'A':14}
def get_puntaje(maso):
    suma=0
    for carta in maso:
        valor = diccionario[carta]
        suma += valor
    return suma
    
if __name__ == '__main__':
    jugador_c1 = input()
    jugador_c2 = input()
    cadena_1 = input()
    cadena_2 = input()
    if get_puntaje(cadena_1) > get_puntaje(cadena_2):
        print(jugador_c1)
    if get_puntaje(cadena_2) > get_puntaje(cadena_1):
        print(jugador_c2)
    if get_puntaje(cadena_1) == get_puntaje(cadena_2):
        print('empate')    