class Pila:
    def __init__(self):
        self.interna = []

    def push(self, valor):
        for element in range(valor):
            self.interna.append(int(input()))
        return self.interna

    def pop(self):
        if not self.interna:
            return None
        return self.interna.pop()

    def peek(self):
        if not self.interna:
            return None
        return self.interna[-1]

    def reverse(self):
        reversed_pila = []
        while self.interna:
            reversed_pila.append(self.pop())
        return ','.join(map(str, reversed_pila))

if __name__ == '__main__':
    valor = int(input())
    pila = Pila()
    pila.push(valor)
    print(pila.reverse())
