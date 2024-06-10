def minuscula(nombre):
    return nombre.lower()

def mayuscula(nombre):
    return nombre.upper()

def soloInicial(nombre):
    nombre = nombre.split(' ')
    nom = ''
    for palabra in nombre:
        nom = nom + palabra.capitalize() + ' '
        
    return nom

if __name__ == '__main__':
    nombre = input('Ingresa tu nombre completo de la forma que quieras: ')
    print(minuscula(nombre))
    print(mayuscula(nombre))
    print(soloInicial(nombre))