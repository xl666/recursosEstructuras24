import cifrado_cesar_maestro

assert cifrado_cesar_maestro.cifrar(5, 'cazar cuervos') == ''
assert cifrado_cesar_maestro.cifrar(0, 'cazar cuervos') == 'cazar cuervos'
assert cifrado_cesar_maestro.cifrar(26, 'cazar cuervos') == 'cazar cuervos'
assert cifrado_cesar_maestro.cifrar(2600600, 'cazar') == 'ecbct'


