#Las pilas
#El acceso a los elementos está restringido, sólo se puede tener acceso
#a un elemento a la vez(El tope de la pila)

#El ultimo elemento es el primero que puede salir

#Push: agrega un elemento al tope 
#pop: Saca  y regeresa el lemento al tope 
#Peek: Sólo regresa el valor del elemento al tope sin sacarlo

#Implementación 
pila = []
pila.append(1) #Equivalenete al push
pila.append(2)
pila.append(3)

tope = pila[-1] #Equivalnte de peek
print(tope)

tope = pila.pop() #POP
print(tope)
print(pila)

#Funcionalidades 
class pila():
    def __init__(self):
        self.lista = []

    def push(self,valor):
        self.lista.append(valor)

    def pop(self):
        if not self.lista:
            return False
        return self.lista.pop()
    
    def peek(self):
        if not self.lista:
            return None
        return self.lista[-1]
    
    def __repr__(self):
        return str(self.lista)
    
pila = pila()
pila.push(1)
pila.push(2)
pila.push(3)
print(pila)
tope = pila.peek()
print(tope)
tope = pila.pop()
print(tope)
print(pila)