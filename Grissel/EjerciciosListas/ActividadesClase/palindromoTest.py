import cadenapalindromo

assert cadenapalindromo.reversa('') == ''
assert cadenapalindromo.reversa('r') == 'r'
assert cadenapalindromo.reversa('ab') == 'ba'
assert cadenapalindromo.reversa('abCd') == 'dCba'

assert cadenapalindromo.es_palindromo('anitalavalatina') == True
assert cadenapalindromo.es_palindromo('ala') == True
assert cadenapalindromo.es_palindromo('') == True
assert cadenapalindromo.es_palindromo('a1') == False
assert cadenapalindromo.es_palindromo('qwEFEFFDFRA') == False

print('Todo OK')
