def obtener_directorio_archivo_extension(ruta):
    if '/' not in ruta:
        directorio = './'
        return directorio,ruta
    
    directorio_primer_slash_index = ruta.find('/')
    directorio_ultimo_slash_index = ruta.rfind('/')
    directorio = ruta[directorio_primer_slash_index:directorio_ultimo_slash_index + 1]
    archivo1 = ruta.rfind('/')
    archivo2 = ruta.rfind('.')
    archivo = ruta[archivo1 + 1:]
    extension = ruta[archivo2 + 1:]
    return directorio, archivo, extension

class Ruta:
    def __init__(self, directorio, archivo, extension):
        self.directorio = directorio
        self.archivo = archivo
        self.extension = extension

    def __repr__(self):
        return f"directorio:{self.directorio}:archivo:{self.archivo}:extension:{self.extension}"

if __name__ == '__main__':
    entrada = input()
    directorio, archivo, extension = obtener_directorio_archivo_extension(entrada)
    print(Ruta(directorio, archivo, extension))
