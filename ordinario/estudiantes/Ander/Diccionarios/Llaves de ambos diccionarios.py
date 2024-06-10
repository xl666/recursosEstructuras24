# Crear una función que reciba dos diccionarios y devuelva un nuevo
#  diccionario que contenga las claves que están presentes en ambos
#  diccionarios.

def llenar_dic(n: int) -> dict:
    d = {}
    if not n:
        return d
    for _ in range(n):
        k = input()
        v = input()
        d[k] = v
    return d

def claves_en_comun(d1: dict, d2: dict) -> dict:
    l = []
    d3 = {}
    for k in d1.keys():
        l.append(k)
    for k, v in d2.items():
        if k in l:
            d3[k] = v
    return d3

if __name__=='__main__':
    n, m = int(input()), int(input())
    d1, d2 = llenar_dic(n), llenar_dic(m)
    print(claves_en_comun(d1, d2))