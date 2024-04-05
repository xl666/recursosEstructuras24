def calcular(num):
    mes = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    if num > 1 or num < 13:
        print(mes[num - 1])
    else:
        exit()

a = int(input())
calcular(a)