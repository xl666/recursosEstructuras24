def cuantos0_recursivo(cadena, contador):
    if not cadena:
        return contador
    if cadena[0] == '0':
        contador += 1
        return cuantos0_recursivo(cadena[1:], contador)
    else:
        return cuantos0_recursivo(cadena[1:], contador)
    



if __name__ == '__main__':
    cadena = input()
    contador = 0
    print(cuantos0_recursivo(cadena, contador))
   