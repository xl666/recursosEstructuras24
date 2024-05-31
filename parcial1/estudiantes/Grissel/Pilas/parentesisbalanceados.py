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

def paréntesis_balanceados(expresión):
    pila = Pila()
    for carácter in expresión:
        if carácter == "(":
            pila.push(carácter)
        elif carácter == ")":
            if pila.peek() == "(":
                pila.pop()
            else:
                return False
    return pila.peek() is None

if __name__ == "__main__":
    expresión = input("Ingrese una expresión matemática: ")
    if paréntesis_balanceados(expresión):
        print("Los paréntesis están balanceados.")
    else:
        print("Los paréntesis no están balanceados.")
