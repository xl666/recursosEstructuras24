class Ruta:
    def __init__(self, ruta):
        if '/' not in ruta:
            directorio = './'
        else:
            directorio_primer_slash_index = ruta.find('/')
            directorio_ultimo_slash_index = ruta.rfind('/')
            directorio = ruta[directorio_primer_slash_index:directorio_ultimo_slash_index + 1]
        archivo1 = ruta.rfind('/')
        archivo2 = ruta.rfind('.')
        archivo = ruta[archivo1 + 1:]
        extension = ruta[archivo2 + 1:]
        self.directorio = directorio
        self.archivo = archivo
        self.extension = extension

    def __repr__(self):
        return "directorio:%s:archivo:%s:extension:%s" % (self.directorio, self.archivo, self.extension)

if __name__ == '__main__':
    entrada = input()
   
    print(Ruta(entrada))
#Turan Ozbek