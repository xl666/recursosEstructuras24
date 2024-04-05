
def xor(Entrada1, Entrada2):
    Salida = None

    if Entrada1 == 0 and Entrada2 == 0:
        Salida = False
    elif Entrada1 == 1 and Entrada2 == 1:
        Salida = False
    else:
        Salida = True
    
    return Salida

if __name__ == '__main__':
    Entrada1 = int(input())
    Entrada2 = int(input())

    if Entrada1 < 0 or Entrada1 > 1:
        print('No se puede')
    elif Entrada2 < 0 or Entrada2 > 1:
        print('No se puede')
    else:
        print(xor(Entrada1, Entrada2))