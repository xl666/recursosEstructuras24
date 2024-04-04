from random import *

numero_secreto = randint(1,20)
vida = 5
while vida > 0 :
    pregunta = (input("Quieres hacer una pregunta?"))
    if pregunta == "s":
        print("escoge tu pregunta")
        print("1 - Es menor a 10?\n 2- Es menor a 5? \n 3- Es mayor a 15?")
        opcion = int(input())
        if opcion == 1:
            print(numero_secreto < 10)
        elif opcion==2:
            print(numero_secreto < 5)
        elif opcion==3:
            print(numero_secreto > 15)
    else:
        print("adivina")
        adivina= int(input())
        if adivina == numero_secreto:
            print("Ganaste")
            break
        else:
            print("Fallaste")
            pass
    print(f'Te queda {vida -1} vida(s)')    
    vida -= 1    
    if vida == 0:
        print(f' el numero secreto era {numero_secreto}')