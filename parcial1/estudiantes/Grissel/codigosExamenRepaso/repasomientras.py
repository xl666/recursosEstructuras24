# - - - Contador regresivo (de x numero al 1)
numero = int(input())
while numero >= 1:
    print(numero)
    numero -= 1
    
# - - - Tabla de multiplicar
numero = int(input())
hasta_numero = int(input())
i = 1
while i <= hasta_numero:
    print(numero, 'x', i, '=', numero * i)
    i = i + 1

# - - - Calculo de potencia
base = int(input())
exponente = int(input())
resultado = 1
i = 1
while i <= exponente:
    resultado *= base
    i = i + 1
print(base, 'elevado a', exponente, 'es:', resultado)

# - - - Secuencia de Fibonacci
n = int(input())
a, b = 0, 1
contador = 0
while contador < n:
    print(a, end = '')
    a, b = b, a + b
    contador = contador + 1