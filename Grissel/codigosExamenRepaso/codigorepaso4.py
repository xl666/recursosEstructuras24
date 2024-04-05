# - - - - X O R - - - -
n1 = int(input())
n2 = int(input()) 
if (n1 == 0) and (n2 == 0) or (n1 == 1) and (n2 == 1):
    print(False)
else:
    if (n1 == 1) and (n2 == 0) or (n1 == 0) and (n2 == 1):
        print(True)
        