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

        def __repr__(self):
            return str(self.interna)
        
def regresar_pila(pila):
     resultado=[]
     while pila.peek():
          resultado.append(str(pila.pop()))
     return ','.join(resultado)
        
if __name__=='__main__':
     longitud_pila=int(input())
     pila=Pila()
     for i in range (longitud_pila):
          pila.push(int(input()))
     print(regresar_pila(pila))