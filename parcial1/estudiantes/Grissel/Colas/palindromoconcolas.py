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

def es_palíndroma(secuencia):
    cola = Cola()
    for elemento in secuencia:
        cola.append(elemento)
    while not cola.esta_vacia():
        if cola.shift() != cola.pop():
            return False
    return True

if __name__ == "__main__":
    secuencia = input("Ingrese una secuencia de elementos: ")
    if es_palíndroma(secuencia):
        print("La secuencia es un palíndromo.")
    else:
        print("La secuencia no es un palíndromo.")
