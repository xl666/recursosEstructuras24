class Ruta():
    def __init__(self, directorio, archivo, extension):
        self.directorio = directorio
        self.archivo = archivo
        self.extension = extension
    def __repr__(self):
        return 'directorio:%s:archivo:%s:extension:%s' % (self.directorio, self.archivo, self.extension)
    
if __name__ == '__main__':
    cadena = str(input())
    if cadena[0] == '/':
        partes = cadena.split('/')
        directorio = '/'.join(partes[:-1]) + '/'
        slash = partes[-1]
        slash_2 = slash.split('.')
        archivo = slash
        extension = slash_2[-1]
    else:
        directorio = './'
        partes = cadena.split('.')
        archivo = cadena
        extension = partes[-1]
    print(Ruta(directorio, archivo, extension))