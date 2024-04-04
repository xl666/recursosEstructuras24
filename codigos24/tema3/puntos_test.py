
import puntos

assert puntos.contar_puntos('...Hola.M.undo..') == 4
assert puntos.contar_puntos('........') == 1
assert puntos.contar_puntos('') == 0
assert puntos.contar_puntos('eueueu return return') == 0

print('todo OK')




