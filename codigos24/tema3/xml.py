
def dar_formato(cadena):
    partes = cadena.split('.')
    return '<nombre>%s</nombre><edad>%s</edad><grado>%s</grado>' % (partes[0], partes[1], partes[2])

if __name__ == '__main__':
    print(dar_formato(input()))
