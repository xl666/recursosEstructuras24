#def palindromo(cadena):
 #   pass

#assert palindomo. es_palandrimo('anitalavalatina')

def palindromo(cadena):
    if cadena == cadena[::-1]:
        return True
    else:
        return False
    
if __name__== '__main__':

    cadena=input("")
    print(palindromo(cadena))

