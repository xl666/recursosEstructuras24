# crear lista
# verificar que si elemento pertenece a la lista

def pertenece_rec(lista,num, repetido = False):
    if lista:
        print(lista)
        if lista[0] == num:
            repetido = True
            print(repetido)
        lista.pop(0)
        repetido = pertenece_rec(lista,num, repetido)
    return repetido
            
if __name__ == '__main__':
    num = int(input())
    n = int(input())
    lista = [int(input()) for _ in range(n)]
    resultado = pertenece_rec(lista,num)
    print(resultado)