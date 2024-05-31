# Bolunebilirlik
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
# Elde edilen sayılar virgülle ayrılarak yazdırılıyor.
print ','.join(l)

#Verilen sayıların faktöriyelini hesaplayan bir program yazın. 
#Sonuçlar tek satırda ve virgülle ayrılmış bir sekans olarak yazdırılmalıdır.
def faktoriyel(x):
    if x == 0:
        return 1
    return x * faktoriyel(x - 1)

# Kullanıcıdan sayı alınıyor ve faktöriyel fonksiyonu çağrılıyor.
x=int(input())
print faktoriyel(x)

#Verilen bir n tam sayısı için, 1'den n'ye (her ikisi dahil) kadar olan sayıları ve bu sayıların karesini içeren bir sözlük oluşturan bir program
n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i
# Oluşturulan sözlük yazdırılıyor.
print d

#Konsoldan virgülle ayrılmış sayı dizisi alarak bir liste ve bir demet oluşturan bir program yazın

# Kullanıcıdan virgülle ayrılmış sayı dizisi alınıyor.
values=input()
l=values.split(",")
t=tuple(l)
# Liste yazdırılıyor.
print l
# Demet yazdırılıyor.
print t

#En az iki metod içeren bir sınıf tanımlayın: getString: Konsol girdisinden bir string alır, printString: Stringi büyük harflerle yazdırır. Ayrıca, sınıf metodlarını test etmek için basit bir test fonksiyonu ekleyin.
class InputOutString(object):
    def __init__(self):
        self.s = ""
    
    def getString(self):
        # Kullanıcıdan bir string alınıyor.
        self.s = input()
    
    def printString(self):
        # Alınan string büyük harflerle yazdırılıyor.
        print self.s.upper()

strObj = InputOutString()
strObj.getString()
strObj.printString()

#Verilen formüle göre bir değer hesaplayan ve yazdıran bir program yazın: Q = [(2 * C * D)/H]'nin karekökü. Burada C ve H sabit değerlerdir, C=50 ve H=30. D, programınıza virgülle ayrılmış bir dizi olarak giriş yapılacak değişkendir.
import math
c=50
h=30
value = []
items=[x for x in raw_input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

# Hesaplanan değerler virgülle ayrılarak yazdırılıyor.
print ','.join(value)

#İki rakam alıp (X ve Y olarak) XY boyutlarında bir 2D dizisi oluşturan bir program yazın. Dizinin i'inci satırı ve j'inci sütunundaki elemanın değeri i*j olmalıdır.
input_str = input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col
print(multilist)        

#Virgülle ayrılmış kelime dizisini alıp kelimeleri alfabetik olarak sıralayarak yazdıran bir program yazın.

items=[x for x in input().split(',')]
items.sort()
print(','.join(items))

#Satırlar halinde verilen metni alıp tüm karakterleri büyük harfe çeviren ve yazdıran bir program yazın.
lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print(sentence)

#Boşlukla ayrılmış kelimeler dizisini girdi olarak kabul eden ve tüm yinelenen kelimeleri kaldırdıktan sonra kelimeleri alfabetik olarak sıralayıp yazdıran bir program

s = input()
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))

#Virgülle ayrılmış 4 basamaklı ikili sayı dizisini girdi olarak kabul eden ve bunları 5'e bölünebilen sayıları bulup yazdıran bir program yazın.

value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print(','.join(value))


#1000 ile 3000 (her ikisi dahil) arasındaki sayıları bulan ve her basamağı çift olan sayıları virgülle ayrılmış bir dizi olarak yazdıran bir program yazın.

values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))

#Bir cümle kabul eden ve bu cümlenin kaç harf ve rakam içerdiğini hesaplayan bir program yazın.

s = input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])

#Bir cümle kabul eden ve bu cümlenin kaç büyük harf ve kaç küçük harf içerdiğini hesaplayan bir program yazın.

s = input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print("UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])

#Verilen bir rakamla (a olarak) a+aa+aaa+aaaa hesaplamasını yapan bir program yazın. Örneğin, programa 9 girildiğinde, sonuç 11106 olmalıdır.
a = input()
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print(n1+n2+n3+n4)


#Bir dizi içindeki her tek sayıyı kare olarak yazdıran bir program yazın. Dizi, virgülle ayrılmış sayıların bir dizisi olarak konsoldan girilmelidir.

values = input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print(",".join(numbers))

#Konsol girişinden bir işlem kaydı dizisi alarak bir banka hesabının net miktarını hesaplayan bir program yazın. İşlem kaydı formatı aşağıdaki gibidir: D 100 W 200.

netAmount = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print(netAmount)

#Kullanıcıların kayıt olurken kullanıcı adı ve şifre girmelerini gerektiren bir web sitesi için, kullanıcıların girdiği şifrenin geçerliliğini kontrol eden bir program yazın. Şifreler aşağıdaki kriterlere göre kontrol edilmelidir: En az 1 harf [a-z] ve [A-Z] arasında olmalı, en az 1 rakam [0-9] arasında olmalı, en az 1 karakter [$#@] içermeli, işlem şifresinin minimum uzunluğu 6 olmalı, maksimum uzunluğu 12 olmalı.

import re
value = []
items=[x for x in input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))

#(isim, yaş, boy) demetlerini alfabetik sırayla sıralayan bir program yazın. İsim string, yaş ve boy sayılardır. Sıralama kriteri şu şekildedir: 1) Önce isme göre sırala; 2) Sonra yaşa göre sırala; 3) Son olarak boy'a göre sırala. Öncelik sırası isim > yaş > boy'dur.

l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print(sorted(l, key=itemgetter(0,1,2)))

#Verilen bir n aralığında (0 ve n arası), 7'ye bölünebilen sayıları yineleyen bir üreteç (generator) ile bir sınıf tanımlayın.

def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in reverse(100):
    print(i)


#Bir robot, orijinal noktası (0,0) olacak şekilde bir düzlemde hareket eder. Robot, verilen adımlarla YUKARI, AŞAĞI, SOL ve SAĞ hareket edebilir. Robotun bir dizi hareketinden sonra orijinal noktaya olan mesafesini hesaplayan bir program yazın. Eğer mesafe bir ondalık sayı ise, en yakın tam sayıya yuvarlayın.

import math
pos = [0,0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))


#Bir sınıf parametresi olan ve aynı örnek parametresine sahip bir sınıf tanımlayın.

class Person:
    # Define the class parameter "name"
    name = "Person"
    
    def __init__(self, name = None):
        # self.name is the instance parameter
        self.name = name

jeffrey = Person("Jeffrey")
print("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print("%s name is %s" % (Person.name, nico.name))

# iki sayinin toplumunu yapan bir fonksyon belirle
def SumFunction(number1, number2):
	return number1+number2

print(SumFunction(1,2))

#Bir tamsayıyı bir stringe dönüştüren ve konsolda yazdıran bir fonksiyon tanımlayın.

def printValue(n):
    print(str(n))

printValue(3)

#İki stringi girdi olarak kabul eden ve bunları birleştirip konsolda yazdıran bir fonksiyon tanımlayın.

def printValue(s1,s2):
    print(int(s1)+int(s2))

printValue("3","4")

#1'den 3'e (her ikisi de dahil) kadar olan sayıların karelerini içeren bir sözlük yazdıran bir fonksiyon tanımlayın.

def printDict():
    d=dict()
    d[1]=1
    d[2]=2**2
    d[3]=3**2
    print(d)
        
printDict()

# 1 ile 20 arasi numaralari karelerini listele ve son bes numarayi yazdir

def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li[-5:])

printList()


# Bir demetten baska bir demet yaratarak verilen numaralardan sadece cift sayilari yazdir
tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
for i in tp:
	if tp[i]%2==0:
		li.append(tp[i])

tp2=tuple(li)
print(tp2)


# cember sinifi bir  sinif olusturup icinde radius deger ver. 

class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print aCircle.area()
 
# Aynisi ucgen icin yap

class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(2,10)
print(aRectangle.area())

# Bir zinciri unicodea donustur

s = input()
u = unicode( s ,"utf-8")
print(u)

#1/2+2/3+3/4+...+n/n+1 yaparak git

n=int(input())
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print(sum)

#finobacchi formulle birlikte. 

def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
values = [str(f(x)) for x in range(0, n+1)]
print(",".join(values))


#10 ile 100 arasi basamakli bir sayi olustur

import random
print(random.random()*100)


# 0 ile 10 arasi cift sayi buldur. 

import random
print(random.choice([i for i in range(11) if i%2==0]))

# 100 ile 200 arasi rastgele bes numara sec

import random
print(random.sample(range(100), 5))

# 7 ile 15 arasi tam sayi yazdir

import random
print(random.randrange(7,16))


# cift sayilari sil

li = [5,6,77,45,22,12,24]
li = [x for x in li if x%2!=0]
print(li)
