#Colas
#Similares a las pilas 
#son estructuras líneales con acceso restringido
#a diferencia de las pilas son estructuras  FIFO

#   append: agrega un elemento al final 
#   shift: saca el elemento del frente y lo regresa
#   peek: Sólo regresa el valor del elemento al frente sin sacarlo

#Manera básica de implementarlo


cola = []
cola.append(1) # agregar al final
cola.append(3)
cola.append(2)

primero = cola[0] # peek
cola = cola[1:] # se tienen que hacer dos operaciones para shift


#Manera con objetos 

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


cola = Cola()
cola.append(1)
cola.append(2)
cola.append(3)
print(cola)

val = cola.shift()
print(val)
print(cola)

print(cola.peek())

otra = cola.copiar()
print(otra)