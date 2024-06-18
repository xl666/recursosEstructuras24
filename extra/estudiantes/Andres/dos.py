f=[]
f=input("")
if len(f)<3:
    print("error")
else:
    if (len(f)%2)==0:
        s=int(len(f)/2)
        d=s-1
        h=(f[d])
        j=(f[s])
        print(h+j)
    else:
        s=int(len(f)/2)
        j=(f[s])
        print(j)