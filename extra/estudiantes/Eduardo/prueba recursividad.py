
def sumahasta1(n):
    if n == 0:
        return 0
    else:
        return n + sumahasta1(n-1)
    
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
    
def contar(i):
    if i == 1:
        return 1
    else:
        print(i)
        return contar(i-1)
    
def invertir(y):
    if not y:
        return "nada"
    else:
        return y[-1] + invertir(y[:-1])
        

n = int(input("escribe el numero a sumar hasta 1"))
x = int(input("escribe el numero a calcular el factorial"))
i = int(input("escribe el numero a contar en reverso"))
y = input("escribe la cadena a invertir")

print(sumahasta1(n))
print(factorial(x))
print(contar(i))
print(invertir(y))