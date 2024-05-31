import time



def zaman_hesapla(fonk):
    def wrappers(*args,**kwargs):
        baslangic = time.time()
        fonk(*args,**kwargs)
        bitis = time.time()
        print ({bitis - baslangic})
    return wrappers    
        
        
@zaman_hesapla        
def kareleri_al(liste):
    for i in liste:
        print(i*i)
@zaman_hesapla
def kupleri_al(liste):
    for i in liste:
        print(i**3)

@zaman_hesapla
def topla(a,b):
    time.sleep(1)        
kareleri_al(range(100000))