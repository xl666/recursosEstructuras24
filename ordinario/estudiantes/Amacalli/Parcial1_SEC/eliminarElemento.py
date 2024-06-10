def eliminar_ele(e, l):
    lista = [num for num in l if not num == e]
    return lista

if __name__ == '__main__':
    e = int(input())
    n = int(input())
    l = [int(input()) for _ in range(n)]
    print(eliminar_ele(e, l))
