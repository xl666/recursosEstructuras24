numero1 = bool(int(input()))
numero2 = bool(int(input()))

if numero1 == True and numero2 == True:
    print (False)
elif numero1 == True or numero2 == True:
    print(True)
else:
    print(False)
