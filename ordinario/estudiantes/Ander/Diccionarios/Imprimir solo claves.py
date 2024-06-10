# Escribir una función que recorra un 
# diccionario e imprima solo las claves.

def llenar_dic(n: int) -> dict:
    d = {}
    if not n:
        return d
    for _ in range(n):
        k = input()
        v = input()
        d[k] = v
    return d

def imprimir_keys(d: dict)-> None:
    for k in d.keys():
        print(k)

if __name__=='__main__':
    n = int(input())
    d = llenar_dic(n)
    imprimir_keys(d)