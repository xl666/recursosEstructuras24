a=[]
b=[]
N=int(input(""))
M=int(input(""))

for i in range(N):
    listaa=int(input(""))
    a.append(listaa)

for i in range(M):
    listaa=int(input(""))
    b.append(listaa)
s=[]
while a or b:
    if a:
        numero=a[0]
        s.append(numero)
        a.remove(numero)
    if b:
        numero=b[0]
        s.append(numero)
        b.remove(numero)

print(s)
