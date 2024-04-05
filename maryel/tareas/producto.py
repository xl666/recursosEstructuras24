def resultado_multiplicar():
    numero_elementos = int(input())
    
    resultado = 1
    
    for x in range(numero_elementos):
        numero = int(input())
        resultado = resultado * numero
    
    return resultado

print(resultado_multiplicar())
