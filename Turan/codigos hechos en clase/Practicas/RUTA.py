class  Ruta:

    def __init__(self,ruta):
        self.ruta =ruta

    def separador(self):
        if not "/" in self.ruta :
            directorio = './'
            archivo= self.ruta[:]
            extension = self.ruta[self.ruta.rfind('.') +1 :]
            return  (directorio,archivo,extension)
        else:
            primerslash = self.ruta.find('/')
            lastslash = self.ruta.rfind('/')
            directorio = self.ruta[primerslash:lastslash +1]
            archivo = self.ruta[lastslash + 1:]
            extension = archivo[archivo.rfind('.') +1:]
            return (directorio,archivo,extension)
        
    def __repr__(self):
         return "directorio:%s:archivo:%s:extension:%s" % (ruta.separador())
         


if __name__== '__main__':
    ruta = input()
    ruta = Ruta(ruta)
    print(ruta)
   
   