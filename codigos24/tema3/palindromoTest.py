
import palindromo


assert palindromo.reversa('') == ''
assert palindromo.reversa('r') == 'r'
assert palindromo.reversa('ab') == 'ba'
assert palindromo.reversa('abCd') == 'dCba'


assert palindromo.es_palindromo('anitalavalatina') == True
assert palindromo.es_palindromo('anitalavalatinA') == False
assert palindromo.es_palindromo('ala') == True
assert palindromo.es_palindromo('') == True
assert palindromo.es_palindromo('a') == True
assert palindromo.es_palindromo('a1') == False
assert palindromo.es_palindromo('queoukrkreturn') == False

print('Todo OK')
