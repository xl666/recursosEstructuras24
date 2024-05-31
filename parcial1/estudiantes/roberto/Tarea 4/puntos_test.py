import Puntos

assert Puntos.contar_puntos("...Hola.M.undo..") == 4
assert Puntos.contar_puntos("........") == 1
assert Puntos.contar_puntos(" ") == 0   
assert Puntos.contar_puntos("eueueu return reutrn") == 0

print("todo OK")


