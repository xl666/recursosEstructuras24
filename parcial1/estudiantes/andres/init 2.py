class Usuario:
    def __init__(self, cadena):
        usuario, id_grupo, grupo = cadena.split(':')
        self.usuario = usuario
        self.id = id_grupo
        self.grupo = grupo
        self.tipo = 'root' if self.id == '1' and self.grupo == '1' else 'normal'

    def __repr__(self):
        return f'{self.usuario} ({self.tipo})'

cadena = input("Ingrese la cadena en el formato usuario:id:grupo: ")
usuario = Usuario(cadena)
print(usuario)
