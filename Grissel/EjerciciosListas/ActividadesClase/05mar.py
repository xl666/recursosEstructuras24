import cesar 
assert cesar.cifrar(5, 'cazar cuervos') == ''
assert cesar.cifrar(0, 'cazar cuervos') == ''
assert cesar.cifrar(26, 'cazar cuervos') == ''
assert cesar.cifrar(2600600, 'cazar') == 'ecbct'

print('todo OK')