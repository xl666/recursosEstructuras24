def llenardic(n: int, m:int)-> dict:
    diccionario={}
    diccionario2={}
    for _ in range(n):
        key=input()
        value=int(input()) 
        diccionario[key]=value
    for _ in range(m):
        key=input()
        value=int(input()) 
        diccionario2[key]=value
    return diccionario, diccionario2

def combinar(diccionario1, diccionario2):
    diccionario3=diccionario1.copy()
    for i, j in diccionario2.items():
        if i in diccionario3:
            diccionario3[i] += j 
        else: 
            diccionario3[i]=j
    return diccionario3
            
if __name__=='__main__':
    n=int(input())
    m=int(input())
    diccionario1, diccionario2=(llenardic(n, m))
    print (combinar(diccionario1, diccionario2))
    