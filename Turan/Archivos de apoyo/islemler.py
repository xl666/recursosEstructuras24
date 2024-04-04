#Aritmatik
print( 456 % 33) #Artani gostermek icin
print(456 // 33) #Tam sayiya kadar birakilan parca
print(x**y) #Ustu sayilari bulmak icin
print(x**0.35) #Kare kokunu bulmak icin
round(obje,-virgulden sonraki basamak sayisi-) #Sayiyi en yakin numaraya yuvarliyor

#indeksler
yazim= 'bunu yazan tosun'
resultado = yazim[5]
yazim.index("obje") #soldan saga ilk zinciri bulur ama (obje, #,#) yazarak belirli bir yerden saymaya baslayabilir ve bitirebiliriz
yazim.rindex("obje") #tersden ariyor
#indeksler kesim
yazim = "ABCDEFGHIJKLM"
frankment = yazim[2-baslama:5-bitis:3-ziplama] #kesim sekli
frankment = yazim[::-1] #tersten yazdirir,eger -2 olsa tersden 1 zipliyarak

Method
yazi.upper() #buyuk harfler yazmak icin, eger indeksi belirtirsen objenin yaninda[] sadece o harfi buyuk yazar
yazi.lower() #kucuk harfle yazmak icin, eger indeksi belirtirsen objenin yaninda[] sadece o harfi buyuk yazar
yazi.split('ayric') #bu stringi ayraca gore bolme
'birlestiri'.join(obje) #birlestirip zincir yazi yapiyor
yazi.find('harf ve obje') # indeksden farki hata vermiyor eger obje yerinde yoksa
yazi.replace('degisen','degistiren') # harfleri veya objeleri degistirmek icin
yazi.count("obje") #bir objenin kac defa kullanildigini gosteriyor
startswith() ve endswith() #zincirin bir karakterle baslayip veya bittigini bulmak icin
#zincirler degistirilemezler. Toplanabilirler.
len(yazim) #zincirin ne uzunlukta oldugunu belirtmek icin
degisken= yazi.split('obje') # yaparak  list haline getirir.
min ve max(zincir) #zincirdeki alfabetik siraya gore en oncekini cikarir.Dikkat et buyuk harfleri once bulur. 
yazi.rstrip('obje') #zincirin solundaki butun ogeleri siler. 


Listeler[]
#listeler bir birine eklenebilirler
#listelerin icindekileri degistirilebilirler, zincirlerde olmadigi gibi
liste.append(obje) # listenin sonuna obje eklemek icin
liste.pop(obje) #eger bos birakirsan en son elementi siler.Indeks belirtebilirsin ve baska bir degiskene kayit edebilirsin.
liste.sort() #numaralari veya harfleri asagidan yukari dogru siralar. Yerinde degistiriyor.
liste.reverse() # Yerinde listeyi ters cevirir. 
enumerate(liste) #siralama ile birlikte elemanlarla calisir.
zincir = "obje".join(liste) #listeyi zincire dondurur.
min ve max(liste) #en kucuk ve en yuksek degeri bulup verir bir listenin icinde.
liste.insert(yer,obje) #listenin her hangi bir yerine birsey eklemek icin.
liste1.extend(liste2)  #Yaparak listeleri birbirine ekleyebilirsin. 
ortak elementler = [x for x in list1 if x in list2]  # ortak elementleri bulmak icin. 
liste3= list(zip(liste1,liste2)) #listeleri eslestirip demet olarka yazdiriyor. 
del kuyruk1[0] yazip listenin veya kuyrugun basindan bor ogeyi atabilirsin ama her zaman index 0daki olmali. 
liste.pop()  #sonuncudan once pop alir.
liste.remove(eleman) #elemani silmek icin. 
from queue import Queue veya lifoqueue k = Queue(maxsize=3) k.put('a') print(k.qsize(),k.queue()) k.get() #kuyruk ekleme ve cikarma
#push ve append aslinda ayni seyler olup ikiside python anadilinde yoktur. Sonradan eklenmislerdir.
from collections import deque #yaparsan eger liste.popleft() yaparak ilk siradaki elementi de silebilirsin. 






Listeleri s1k1st1rmak:
liste = [obje for obje in zincir veya uzunluk] #yapinca kodlamayi kucultmus oluyorsun. 
liste = [n for n in range(0,21,2) if n*2 > 10 ] #yapinca  koşula göre filtrelemeye yarar.
liste = [n if n*2 > 10 else: "bir sey yaz" for in range(a,b,c)]    #koşula göre filtrelemeye yarar.






Sozluk{}
#indekslenemiyorlar.Anahtarlar tekrar edilemezler.
sozluk ={'c1':'isim'} # gibi yazilir.
#sozlukte butun tip degiskenler olabilir.Hatta baska bir sozluk bile.
print(soz["c1"][1].upper()) #tum harfleri buyuk yapmak icin.
#yerinde degistirilebilir veya eklenebilir.
print(soz.keys())
print(soz.values()) 
print(soz.items()) #herseyi yazdirir ve butun sozluk elementlerinin aslinda tuple oldugu gorulur


Tuples
#Listelere cok benziyorlar. Degistirilemezler, modifiye olmuyorlar.
#Zincirlerdeki methodlari burada da kullanabiliriz.

SET 
#setlerin elementleri degistirilemez ve indekslenemezler, ayni elementten bir taneden fazla olamaz.
benim_set = set ([1,2,3,4]) veya {1,2,3,4} #setler sadece bir argumen kabul ediyorlar. 
s1.union(s2) # Bir degiskene  atayarak birlestirilebilir. Ayni elementleri siler. 
s1.add(obje) # Sete yeni bir oge ekler.  Eger varsa eklemiyor.
s1.remove(obje) #elementi siler. Yoksa  hata verir.
s1.discard(obje) #Removedeki gibi bir ogeyi siler lakin yoksa hata vermez. 
s1.pop() #Settedeki  herhangi bir elemani alir.  Rastgele secerek.
s1.intersection(s2) #iki set arasindaki ortak elemanları getirir.
s1.difference(s2) #ikisi arasindaki farkli elemanları getirir.
s1.issubset(s2) #Bir setin dibine gelip gelmedigini kontrol etmek icin
s1.issuperset(s2) #Bir setin diger setinin tamamina gelip gelmediğini kontrol etmek icin.
s1.isdisjoint(s2) #Iki set arasinda ortak bir ogenin olup olmadigini bool olarak geri veriyor.Eger ortak oge varsa false verir. 
s1.clear( ) #Seti temizleye icin. 

kutuphaneler
from random import * #Random kutuphanesinin hepsini cagirir.
from random import randint #Herhangi bir tam sayiyaratmak icin kullanilir. 
randint(1,50) #1 den 50 arasinda rastgele bir sayi cıkarir.
uniform(a,b) #Basamakli , tam olmayan sayi cikarir. 
random() #Herhangi bir parametre girilmezse sifir ve bir arasi basamakli sayi secer.
choice(liste) #listenin icinden herhangi bir ogeyi secer. 
shuffle(liste) #bir listenin ogelerini  karistirmaya yarar. 
