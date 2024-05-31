class Usuario():
    def __init__(self, usuario, identificador, grupo):
        self.usuario = usuario
        self.identificador = identificador
        self.grupo = grupo
        if identificador == 1 and grupo == 1:
            self.tipo = 'root'
        else:
            self.tipo = 'normal'
    
    # Esto debe estar dentro de la definición de la clase
    def __repr__(self):
        return '%s (%s)' % (self.usuario, self.tipo)

if __name__ == '__main__':
    entrada = input()
    partes = entrada.split(':')
    usuario = partes[0]
    identificador = int(partes[1])
    grupo = int(partes[2])
    # Esto ahora debería funcionar como esperas, mostrando la representación personalizada
    print(Usuario(usuario, identificador, grupo))
