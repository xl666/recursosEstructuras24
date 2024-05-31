def creardiccionarios(n, m, dic1, dic2):

    for _ in range(n):
        llave = input()
        valor = int(input())
        dic1[llave] = valor

    for _ in range(m):
        llave = input()
        valor = int(input())
        dic2[llave] = valor
    
    return dic1, dic2



def unir_dic(dic1, dic2, repetidas):
    repetidas = {}

    for llave in dic1.keys():
        if llave in repetidas:
            repetidas[llave] = dic1[llave] + dic2[llave]
        else:
            repetidas[llave] = dic1[llave]

    for llave in dic2.keys():
        if llave in repetidas:
            repetidas[llave] = dic1[llave] + dic2[llave]
        else:
            repetidas[llave] = dic2[llave]
            
    return repetidas
    
def ordenar_dic(repetidas):
    for llave in sorted(repetidas.keys()):
        print('%s: %s' % (llave, repetidas[llave]))

    



if __name__ == '__main__':
    n = int(input())
    m = int(input())
    dic1 = {}
    dic2 = {}
    repetidas = {}

    creardiccionarios(n, m, dic1, dic2)
    dicfin = unir_dic(dic1, dic2, repetidas)
    ordenar_dic(dicfin)