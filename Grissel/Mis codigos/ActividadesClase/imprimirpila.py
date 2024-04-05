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
        
def voltear(pila):
        inversa = []
        while pila.peek():
            inversa.append(str(pila.pop()))
        return ','.join(inversa)
        
if __name__ == '__main__':
    longitud_lista = int(input())
    pila = Pila()
    for _ in range (longitud_lista):
        pila.push (int(input()))
print(voltear(pila))