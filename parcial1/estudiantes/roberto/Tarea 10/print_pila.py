class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def tamano(self):
        return len(self.items)

def imprimir_pila_en_orden(pila):
    elementos = []
    while not pila.esta_vacia():
        elementos.append(str(pila.pop()))
    print(",".join(elementos))


n = int(input())
pila = Pila()
for _ in range(n):
    elemento = int(input())
    pila.push(elemento)

imprimir_pila_en_orden(pila)