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

def es_palindromo(palabra):
    pila = Pila()
    for letra in palabra:
        pila.push(letra)
    palabra_invertida = ""
    while pila.peek():
        palabra_invertida += pila.pop()
    return palabra == palabra_invertida

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    if es_palindromo(palabra):
        print("La palabra es un palíndromo.")
    else:
        print("La palabra no es un palíndromo.")
