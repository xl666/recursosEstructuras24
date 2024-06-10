# Implementar una función que calcule la suma de los
# valores de un diccionario.

def llenar_dic(n: int) -> dict:
    d = {}
    if not n:
        return d
    for _ in range(n):
        k = input()
        v = int(input())
        d[k] = v
    return d

def calcular_suma(d: dict)-> int:
    x = 0
    for v in d.values():
        x += v
    return x

if __name__=='__main__':
    n = int(input())
    d = llenar_dic(n)
    print(calcular_suma(d))