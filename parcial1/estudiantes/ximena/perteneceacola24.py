#Crea una función (NO método) que recibe un valor entero y una cola, la función determina si el elemento pertenece a la cola de entrada. 

#Cuidado: has una copia de la cola original antes de procesar (usa el método de copiar)

#- Solo utilizar métodos del objeto (shift, peek, etc.)

#- Utilizar el código adjunto al ejercicio
#Ejemplo de entrada
#77
#5
#1,2,3,4,5
#Ejemplo de salida
#False
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

def pertenece(valor, cola):
    cola = cola.copiar()
    while not cola.esta_vacia():
        if cola.shift() == valor:
            return True
    return False
    

if __name__ == '__main__':
    v = int(input())
    n = int(input())
    cola = Cola()
    for _ in range(n):
        cola.append(int(input()))
    print(pertenece(v, cola))