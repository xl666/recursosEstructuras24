class Cadena():
    def __init__(self,cadena):
        self.cadena  = cadena
    
    def usuario(self):
        usuario = self.cadena[0:(self.cadena.find(':'))]
        return usuario
    
    def tipo(self):

        tipo = self.cadena.split(':')
        if tipo[1] == tipo[2]:
            return "(root)"
        else:
            return "(normal)"
    
    def __repr__(self):
        return (self.usuario() + " " + self.tipo())


if __name__=='__main__':
    cadena = Cadena(input())
    print(cadena)