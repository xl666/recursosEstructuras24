a=[]
b=[]
N=int(input(""))
M=int(input(""))

for i in range(N):
    listaa=int(input(""))
    a.append(listaa)

for i in range(M):
    listaa=int(input(""))
    a.append(listaa)

s=a+b
g=[]
x=len(s)
for i in range(x):
    f=(min(s))
    g.append(f)
    s.remove(f)

print(g)




