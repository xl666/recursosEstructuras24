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

def pertenece_a_cola(valor, cola):
    cola_copia = cola.copiar()
    while not cola_copia.esta_vacia():
        elemento = cola_copia.shift()
        if elemento == valor:
            return True
    return False

valor = int(input())
N = int(input())
n=N-1
elementos_cola = list(map(int, input().split()))

cola = Cola()
for _ in range(n):
    elemento = int(input())
    cola.append(elemento)

print(pertenece_a_cola(valor, cola))

