# Considera la clase Nodo que define las siguientes propiedades:
#- valor (tipo int)
#- siguiente_nodo (tipo Nodo)

#Para un nodo donde no se define un nodo siguiente tiene None como valor de la propiedad siguiente_nodo

#Así mismo considera la clase Lista que cuenta con las siguientes propiedades:
#- cabeza (tipo Nodo)

#La clase Lista también cuenta con los siguientes métodos:
#__init__(self, valor)  para crear una lista inicial de un valor (crear un nodo con el valor), esto es, la
#cabeza se inicia con un nodo con el valor recibido (None para el nodo siguiente)

#append (self, valor) agrega un valor (crear nodo) al final de la lista (se recorre siguiente desde la cabeza 
#hasta encontrar un valor None)

#get(self, pos) donde posición es un valor de índice (la cabeza es la posición 0). En caso de que la posición sea
#inválida se regresa None

#Tu trabajo consiste en definir tanto la clase Nodo y la clase Lista como se describe.
#Se te proporcionará un número P que representa una posición a recuperar de un objeto Lista
#luego recibirás un número N que representa la cantidad de valores a leer, seguido de N entradas

#Deberás crear un objeto Lista, y utilizando el método append implementado, deberás de agregar cada
#elemento leído. El resultado de tu programa consiste en la impresión del valor en la posición P
#utilizando el método get implementado.

#Nota: se revisará el código para corroborar que se siguió la implementación descrita.
#Entrada
#Un valor P entero positivo que representa una posición de la lista a construir
#Un valor N entero que indica el número de elementos que tendrá el objeto Lista
#N entradas de tipo entero que corresponden a cada valor del objeto Lista.
#Salida
#Un número entero que representa el valor en la posición P
class Nodo():
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Lista():
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza == None

    def append(self, valor):
        nuevo = Nodo(valor)
        # caso especial lista vacía
        if self.esta_vacia():
            self.cabeza = nuevo
            return
        # la lista no está vacía:
        aux = self.cabeza
        while aux.siguiente != None:
            aux = aux.siguiente
        aux.siguiente = nuevo

    def get(self, pos):
        if self.esta_vacia():
            return None
        if pos < 0:
            return None
        cont = 0
        aux = self.cabeza
        while cont < pos:
            cont += 1
            aux = aux.siguiente
            if not aux:
                return None
        return aux.valor

if __name__ == '__main__':
    p = int(input())
    n = int(input())
    l = Lista()
    for _ in range(n):
        l.append(int(input()))

    print(l.get(p))