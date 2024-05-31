
def fibonacci(Entrada):
    inicio = 0
    segundo = 1
    actual = 0

    for i in range(Entrada):
        actual = inicio + segundo
        segundo = inicio
        inicio = actual
    
    return actual

if __name__ == '__main__':
    Entrada = int(input())
    print(fibonacci(Entrada))