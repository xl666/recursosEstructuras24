
def dar_formato(entrada):
    lista=entrada.split('.')
    nombre=lista[0]
    edad=lista[1]
    grado=lista[2]
    print(f'<nombre>{nombre}</nombre><edad>{edad}</edad><grado>{grado}</grado>')

if __name__=='__main__':
    entrada=input()
    dar_formato(entrada)
    
    