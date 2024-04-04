def cifrar_palabra(shift,palabra):
    cifrada=''
    for letra in palabra:
        if ord(letra)>=ord('a') and ord(letra)<=ord('z'):
            l_cif=chr(((ord(letra)+shift-ord('a'))%26)+ord('a'))
            cifrada+=l_cif
        else:
            cifrada+=' '
    return cifrada
if __name__=='__main__':
    shift=int(input())
    palabra=input()
    print(cifrar_palabra(shift,palabra))
