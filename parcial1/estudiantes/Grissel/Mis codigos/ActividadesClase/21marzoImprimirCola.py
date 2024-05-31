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

def ImprimeCola(cola):
    nueva_cola = cola.copiar()
    res = []
    while nueva_cola.peek():
        res.append(str(nueva_cola.shift()))
    return ','.join(res)

    
if __name__ == '__main__':
    cola = Cola()
    n = int(input())
    for _ in range (n):
        cola.append(int(input()))
print(ImprimeCola(cola))