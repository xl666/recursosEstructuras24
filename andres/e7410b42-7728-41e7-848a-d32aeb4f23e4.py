def pertenece_a_cola(V, cola):
   if V in cola:
        return True
   else:
       return False

cola=[]
N= int(input())
cola_str=(input())
cola=[int(x) for x in cola_str.split(",")]

V= int(input())
print(pertenece_a_cola(V, cola))
