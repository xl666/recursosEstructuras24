#While = Execute some code while some condition remains true

name = input('Enter your name: ')

while name == '':
    print('you did not print anything')
    name = input('Enter your name: ')

print(f'hello {name}')

#For loop 
for i in range(1,11):
    print(i)

#Reverse
for i in reversed(range(1, 11)):
    print(i)

#By steps           2 is the number of steps we will make 
for i in range(1,11,2):
    print(i)

Card = '1234-567-89123'
for i in Card:
    print(i, end='')
#            ^ This is for printing them in vertical 

#Continue and break 

for x in range(1, 21):
    if x == 13:
        continue
#       This can help skip iterations 
    else:
        print(x)

for x in range(1,21):
    if x == 13:
        break
#       This ends completely the loop
    else:
        print(x)