class Cola():
    def __init__(self):
        self.interna = []

    def esta_vacia(self):
        return not self.interna

    def append(self, valor):
        for i in range(elements):
            self.interna.append(int(input()))
        return self.interna

    def shift(self):
        if self.esta_vacia():
            return None
        val = self.interna[0]
        self.interna = self.interna[1:]
        return val

    def peek(self):
        if self.esta_vacia():
            return None
        return self.interna[0]

    def __repr__(self):
        return str(self.interna)

    def copiar(self):
        nueva_cola = Cola()
        while self.interna:
            nueva_cola.append(self.shift())
        return ','.join(map(str, nueva_cola))

    
if  __name__ == "__main__":
    elements= int(input())
    fila = Cola()
    fila.append(elements)
    copiado = fila.copiar
    print(copiado)