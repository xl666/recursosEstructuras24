class Ruta:
    def __init__(self, directorio, archivo, extension):
        self.directorio = directorio
        self.archivo = archivo
        self.extension = extension

    def __repr__(self):
        return "directorio:%s:archivo:%s:extension:%s" % (self.directorio, self.archivo, self.extension)

if __name__ == '__main__':
    entrada = input()
    if '/' not in entrada:
        directorio = './'
    else:
        directorio_primer_slash_index = entrada.find('/')
        directorio_ultimo_slash_index = entrada.rfind('/')
        directorio = entrada[directorio_primer_slash_index:directorio_ultimo_slash_index + 1]
    archivo1 = entrada.rfind('/')
    archivo2 = entrada.rfind('.')
    archivo = entrada[archivo1 + 1:]
    extension = entrada[archivo2 + 1:]
    print(Ruta(directorio, archivo, extension))
#Turan Ozbek