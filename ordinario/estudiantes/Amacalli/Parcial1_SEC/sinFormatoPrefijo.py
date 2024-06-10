def quitarPrefijo(numero):
    sin = numero.split('-')
    return sin[1]

if __name__ == '__main__':
    numero = input()
    print(quitarPrefijo(numero))