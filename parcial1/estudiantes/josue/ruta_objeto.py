class Ruta:
    def __init__(self, directorio, archivo, extension):
        self.directorio = directorio
        self.archivo = archivo
        self.extension = extension

        

    def __repr__(self):
        return 'directorio:%s:archivo:%s:extension:%s' % (self.directorio, self.archivo, self.extension)
    



if __name__ == '__main__':
    entrada = input()
    partes = entrada.rsplit('/', 1)
    if len(partes) == 1:
        directorio = './'
        archivo = partes[0]
    else:
        directorio = partes[0] + '/'
        archivo = partes[1]
        extension_partes = archivo.rsplit('.', 1)
        extension = extension_partes[1]

    print(Ruta(directorio, archivo, extension))