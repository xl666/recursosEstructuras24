class Pila():
        def __init__(self):
            self.interna = []

        def esta_vacia(self):
             return not self.interna

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
        
        def voltear(Pila):
            pila = Pila()
            for c in Pila:
                pila.push(c)
            inversa = ''
            while pila.peek(): # si está vacía peek regresa None
                inversa += pila.pop()
            return inversa

        def __repr__(self):
            return str(self.interna)
        

if __name__ == '__main__':
    n = int(input())
    pila = Pila()
    pila_final = Pila()
    for _ in range(n):
        pila.push(input())
    
    for _ in range(n):
        pila_final = pila.pop()


print(pila)
print(pila_final)

     



