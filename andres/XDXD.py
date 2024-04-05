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

def pertenece_a_cola(valor, N, cola):
    cola_copia = cola.copiar() 
    for _ in range(N):
        if cola_copia.esta_vacia():
            return False
        if cola_copia.peek() == valor:
            return True
        cola_copia.shift()
    
    
    return False

N = int(input("Ingrese el número de elementos de la cola: "))
cola = Cola()
for _ in range(N):
    elemento = int(input("Ingrese un elemento de la cola: "))
    cola.append(elemento)

valor = int(input("Ingrese el valor a buscar: "))
print(pertenece_a_cola(valor, N, cola))
