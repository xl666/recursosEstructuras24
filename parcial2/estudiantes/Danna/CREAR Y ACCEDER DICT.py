def llenardic(n: int)-> dict:
    diccionario={}
    for _ in range(n):
        key=input()
        value=input() 
        diccionario[key]=value
    return diccionario

def accederdic(dic: dict)->dict:
    for k, v in dic.items():
        print(k, ':', v)
        return dic
    

if __name__=='__main__':
    n=int(input())
    dic=(llenardic(n))
    print(accederdic(dic))