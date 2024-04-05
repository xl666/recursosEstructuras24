class Cola():
    def __init__(self):
        self.interna = []

    def esta_vacia(self):
        return not self.interna

    def append(self, valor):
        self.interna.append(valor)

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
        for elemento in self.interna:
            nueva_cola.append(elemento)
        return nueva_cola

def verificar(v, cola):
    nueva_cola = cola.copiar()
    while not nueva_cola.esta_vacia():
        if nueva_cola.shift() == v:
            return True
    return False

if __name__ == '__main__':
    cola = Cola()
    v = int(input())
    n = int(input())
    for _ in range (n):
        cola.append(int(input()))
print(verificar(v, cola))

