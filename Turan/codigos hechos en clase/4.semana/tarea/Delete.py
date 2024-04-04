def ordenar(lista , del_num):
    lista= [num for num in lista if num != del_num]
    return lista
        
if __name__ == '__main__':
    del_num = int(input())
    N = int(input())
    lista = [int(input()) for _ in range(N)]
    resultado = ordenar(lista, del_num)
    print(resultado)


    #Turan Ozbek