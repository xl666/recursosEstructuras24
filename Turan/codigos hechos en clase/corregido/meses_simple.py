numero_mes = int(input())

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

if numero_mes >= 1 and numero_mes <= 12:
    print(meses[numero_mes - 1])
else:
    print("Número fuera de rango")

