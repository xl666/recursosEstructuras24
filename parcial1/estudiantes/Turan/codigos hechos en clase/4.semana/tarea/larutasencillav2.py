class Ruta:
    def __init__(self, ruta):
        
        self.archivo = ruta.split('/')[-1]
        self.extension = self.archivo.rsplit('.')[-1]
        if '/' not in ruta:
            self.directorio = './'
        else:
            directorio = ruta.split('/')[:-1]
            self.directorio = '/'.join(directorio) + '/'
   

    def __repr__(self):
        return "directorio:%s:archivo:%s:extension:%s" % (self.directorio, self.archivo, self.extension)

if __name__ == '__main__':
    entrada = input()
   
    print(Ruta(entrada))
#Turan Ozbek