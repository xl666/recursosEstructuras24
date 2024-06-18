N = int(input().strip())

conteo_ok = {}

for _ in range(N):
    entrada = input().strip()
    dominio, resultado = entrada.split(':')
    
    if dominio not in conteo_ok:
        conteo_ok[dominio] = 0
    
    if resultado == "OK":
        conteo_ok[dominio] += 1

dominios_alcanzables = [dominio for dominio, conteo in conteo_ok.items() if conteo >= 2]

dominios_alcanzables.sort()

for dominio in dominios_alcanzables:
    print(dominio)
