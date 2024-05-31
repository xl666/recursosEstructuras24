valores = int(input())
maximo = 0

if valores == 0:
    print('error')
    exit

for i in range(valores):
    num = int(input())
    if num > maximo:
        maximo = num
    print(maximo)

#print(maximo)