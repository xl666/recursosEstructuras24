def llenardic(n: int)-> dict:
    diccionario={}
    for _ in range(n):
        key=input()
        value=int(input()) 
        diccionario[key]=value
    return diccionario

def accederdic(dic: dict)->dict:
    accederdi=sorted(dic.keys())
    for k in accederdi:
        print(k, ':', dic[k] + 1)
    return dic
    

if __name__=='__main__':
    n=int(input())
    dic=(llenardic(n))
    accederdic(dic)