# Contar cuantos ceros
def cadena_rec(cadena, suma = 0):
    if cadena:
        if cadena[0:1] == '0':
            suma += 1
        suma = cadena_rec(cadena[1:], suma)
    return suma

if __name__ == '__main__':
    print(cadena_rec('00544000'))    