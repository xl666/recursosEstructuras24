numElementos = int(input())
lista = []

if numElementos == 0:
    print ()
    exit 

for _ in  range (numElementos):
    lista.append(input()) 

for elemento in lista:
    print (elemento) 