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
        
def revisar_expresion(expresion):
     pila=Pila()
     for i in expresion:
         if i=='(':
             pila.push(i)
         elif i==')':
             if pila.peek()=='(':
                 pila.pop()
             else:
              return False
     return pila.interna==[]


if __name__=='__main__':
     expresion=input()
     print(revisar_expresion(expresion))