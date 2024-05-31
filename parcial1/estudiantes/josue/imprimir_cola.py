class Cola():
    def __init__(self):
        self.interna = []

    def esta_vacia(self):
        return len(self.interna) == 0

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
    
def imprimir_cola(cola):
    lista = []
    while cola.peek():
        lista.append(str(cola.shift()))
    print(','.join(lista))

def elemento_pertenece(expresion, v):
    otra = cola.copiar()
    for c in expresion:
        if c == 'v':
            return True
        return False
    if not cola.esta_vacia():
        return False
    return True

        



if __name__ == '__main__':
    v = int(input())
    n = int(input())
    cola = Cola()
    for _ in range(n):
        cola.append(int(input()))
    print(elemento_pertenece(cola,v))