def formato(nombre, edad, grado):
    plantilla = "<nombre>%s</nombre><edad>%s</edad><grado>%s</grado>"%(nombre, edad, grado)
    return 

if __name__ == '__main__':
    cadena = str(input())
    partes = cadena.split('.')
    nombre = partes[0]
    edad = partes[1]
    grado = partes [2]
    print(formato(nombre, edad, grado))

