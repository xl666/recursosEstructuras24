class Ruta():
    def __init__(self,directorio,archivo,extension):
        self.directorio = directorio
        self.archivo = archivo
        self.extension = extension
        
    def __repr__(self):
        print(self.directorio,self.archivo,self.extension)
    
if __name__ == '__main__':
    entrada = str(input())
    directorio_primer_slash_index = entrada.find('/')
    directorio_ultimo_slash_index = entrada.rfind('/')
    directorio= [directorio_primer_slash_index:directorio_ultimo_slash_index + 1]
    archivo1 = entrada.rfind('/')
    archivo2 = entrada.rfind('.')
    archivo = [archivo1:archivo2 -1]
    extension1 =entrada.rfind('.')
    extension = [extension1:]
    print(Ruta(directorio,archivo,extension))
