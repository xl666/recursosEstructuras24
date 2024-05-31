class Pila():
    def __init__(self):
        self.interna = []

    def push(self, valor):
        self.interna.append(valor)

    def pop(self):
        if not self.interna:
            return None
        return self.interna.pop()

    def peek(self):
        if not self.interna:
            return None
        return self.interna[-1]

    def __repr__(self):
        return str(self.interna)
    
def voltear(cadena):
    pila = Pila()
    for c in cadena:
        pila.push(c)
    inversa = ''
    while pila.peek(): # si está vacía peek regresa None
        inversa += pila.pop()
    return inversa

def formato(pila):
    res = ','.join(pila)
    return res

if __name__ == '__main__':
    n = int(input())
    pila = [int(input()) for _ in range(n)]
    cadena = [str(ele) for ele in pila]
    res = formato(voltear(cadena))

    print(res)