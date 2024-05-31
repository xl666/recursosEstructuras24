def sumar1(n, dic):
    for _ in range(n):
        llave = input()
        valor = int(input())
        dic[llave] = valor + 1


def ordenar_dic(dic):
    for llave in sorted(dic.keys()):
        print('%s:%s' % (llave, dic[llave]))



if __name__ == '__main__':
    n = int(input())
    dic = {}

    sumar1(n,dic)
    ordenar_dic(dic)