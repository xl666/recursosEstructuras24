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

def invertir_secuencia(secuencia):
    cola = Cola()
    for elemento in secuencia:
        cola.append(elemento)
    secuencia_invertida = ''
    while not cola.esta_vacia():
        secuencia_invertida += cola.shift()
    return secuencia_invertida

if __name__ == "__main__":
    secuencia = input("Ingrese una secuencia de elementos: ")
    secuencia_invertida = invertir_secuencia(secuencia)
    print("Secuencia invertida:", secuencia_invertida)
