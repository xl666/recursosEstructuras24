
def palindromo(Entrada):
    if Entrada == Entrada[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    Entrada = str(input())
    if Entrada == '':
        print('No se puede')
    else:
        print(palindromo(Entrada))