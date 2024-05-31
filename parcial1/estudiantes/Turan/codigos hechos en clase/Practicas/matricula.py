def constructor(n):
    texto =[]
    sonuc =[]
    for i in range(n):
        cadena = input()
        texto = cadena.split(' ')
        matricula = texto.pop()
        sonuc.append(matricula)
    for _ in range(len(sonuc)):
        print(sonuc[_][1:-1])
    return None    
    
   
    


if __name__== '__main__':
    n = int(input())
    constructor(n)

