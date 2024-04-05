#Crea una función (CUIDADO no método) que reciba una cola e imprima todos sus elementos. Sólo podrás usar el método shift para ir sacando un elemento a la vez, deberás tener cuidado de que los elementos de la cola no se pierdan, para esto debes usar el método "copiar" para que sea la cola copia la que descarte elementos.

#Utiliza como base el código adjunto al ejercicio.
#Ejemplo de entrada
#5
#1,2,3,4,5
#Ejemplo de salida
#1,2,3,4,5
class Cola():
    def __init__(self):
        self.interna = []

    def esta_vacia(self):
        return not self.interna

    def append(self, valor):
        self.interna.append(valor)

    def shift(self):
        if self.esta_vacia():
            return None
        val = self.interna[0]
        self.interna = self.interna[1:]
        return val

    def peek(self):
        if self.esta_vacia():
            return None
        return self.interna[0]

    def __repr__(self):
        return str(self.interna)

    def copiar(self):
        nueva_cola = Cola()
        for elemento in self.interna:
            nueva_cola.append(elemento)
        return nueva_cola

def imprimir_cola(cola):
    cola_copia = cola.copiar()  # Crear una copia de la cola para no perder los elementos
    elementos = []
    while not cola_copia.esta_vacia():
        elementos.append(str(cola_copia.shift()))  # Agregar cada elemento de la cola a una lista
    print(",".join(elementos))  # Imprimir los elementos separados por comas

if __name__ == '__main__':
    N = int(input())
    cola = Cola()
    for _ in range(N):
        num = int(input())
        cola.append(num)
    imprimir_cola(cola)