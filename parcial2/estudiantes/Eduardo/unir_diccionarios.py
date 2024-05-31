if __name__ == "__main__":
    dic1 = {}
    dic2 = {}
    dicsal = {}   #se crean los diccionarios

    nelemd1 = int(input())  #se indica cuantos elementos se quieren en el diccionario
    nelemd2 = int(input())

    for _ in range(nelemd1):
        key = input()
        value = int(input())
        dic1[key] = dic1.get(key, 0) + value  #si la llave ya existe suma el valor y si no agrega una nueva llave

    for _ in range(nelemd2):
        key = input()
        value = int(input())
        dic2[key] = dic2.get(key, 0) + value  #si la llave ya existe suma el valor y si no agrega una nueva llave

    
    for key in dic1:  #fusiona diccionaios
        dicsal[key] = dic1[key]  #agrega las claves y valores del primer diccionario

    for key in dic2:
        if key in dicsal:
            dicsal[key] += dic2[key]  #si la clave ya existe suma los valores de ambos diccionarios
        else:
            dicsal[key] = dic2[key]  #si la clave no existe agrega la clave y valor del segundo diccionario

    for key, value in sorted(dicsal.items()): #ordenmaiento
        print(f"{key}: {value}")
