#Crea una función que recibe una pila e imprime sus elementos en orden, empezando por el elemento tope
#Cada elemento debe estar separado por una coma

#Deberás usar el archivo adjunto que define una clase Pila(visto en clase)
#Ejemplo de entrada
#5
#5,4,3,2,1
#Ejemplo de salida
#1,2,3,4,5
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

def imprimir_pila(pila):
    if not pila.peek():
        return
    primero = pila.pop()
    print(primero, end='')
    while pila.peek():
        print(',' + str(pila.pop()), end='')
    print('')

def imprimir_pila2(pila):
    lista = []
    while pila.peek():
        lista.append(str(pila.pop()))
    print(','.join(lista))

if __name__ == '__main__':
    n = int(input())
    pila = Pila()
    for _ in range(n):
        pila.push(int(input()))
    imprimir_pila(pila)
    