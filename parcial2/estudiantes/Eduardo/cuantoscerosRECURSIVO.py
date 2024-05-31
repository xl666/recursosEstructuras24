#contar cuantos ceros tiene una entrada binaria

def contarceros(binario):
    if not binario:
        return 0
    if binario[0] == "0":
      return 1 + contarceros(binario[1:])
    else:
        return contarceros(binario[1:])  #patron utilizable para contar x caracteres o cosas en una cadena
    

if __name__ == "__main__":
    binario = input()
    print(contarceros(binario))