#El cifrado César consiste en aplicar un "shift" a cada carácter de una cadena.
#Un shift es mover un número de posiciones a la derecha, por ejemplo
#a partir de la letra 'a'  y un shift de 3, la letra correspondiente es 'd', en el caso de
#que el shift sobrepase la 'z' se vuelve a empezar en la letra 'a'.

#Considera que para este ejercicio sólo habrá letras minúsculas, sin considerar la ñ
#ni acentos (26 letras, osea el alfabeto en inglés). 
#Los espacios se ignoran y mantienen como están
def cifrado(cadena, shift):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""
    
    for letra in cadena:
        if 'a' <= letra <= 'z':
            indice = (ord(letra) - ord('a') + shift) % 26
            letra_cifrada = abecedario[indice]
            resultado += letra_cifrada
        else:
            resultado += letra
    
    return resultado

shift = int(input())
cadena = input()

frase_cifrada = cifrado(cadena, shift)
print(frase_cifrada)