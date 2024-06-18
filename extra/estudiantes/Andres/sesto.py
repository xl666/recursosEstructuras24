a=input("")
aa=a.title()
nueva=aa.split()
if "De"in nueva and "La" in nueva:
    f=(nueva.index("De"))
    g=(nueva.index("La"))
    nueva[f]="de"
    nueva[g]="la"
    final="".join(nueva)
    fina=final.split()
    print(fina)
else:
    print(aa)