N=int(input ("Dame un numero: "))

if N==0:
    print("Sin datos")

else:
    listaelementos=[]
    for i in range(N):
        element=input(f"Dame un elemento {i+1}:")
        listaelementos.append(element)

for element in listaelementos:
    print(element)
