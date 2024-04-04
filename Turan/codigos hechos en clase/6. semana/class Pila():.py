class Pila():
        def __init__(self):
            self.interna = []

        def push(self, valor):
            for element in range(valor):
                self.interna.append(element)
            return self.interna

        def pop(self):
            pila =Pila()
            if not self.interna:
                return None
            reverse= ''
            while pila.peek():
                reverse+=pila.pop
            return self.interna.pop()

        def peek(self):
            if not self.interna:
                return None
            while self.peek()== None:
                return not self.interna
            return self.interna[-1]


if __name__=='__main__':
    valor= int(input())
    pila = Pila()
    pila.push(valor)

