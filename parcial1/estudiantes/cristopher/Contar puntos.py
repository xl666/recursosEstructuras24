
def contar(Entrada):
    Cadena_sin_Repetir_1 = Entrada.replace('...', '.')
    Cadena_sin_Repetir_2 = Cadena_sin_Repetir_1.replace('..', '.')
    return Cadena_sin_Repetir_2.count('.')

if __name__ == '__main__':
    Entrada = str(input())
    print(contar(Entrada))