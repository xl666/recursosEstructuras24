if __name__ == '__main__':
    n1 = bool(int(input()))
    n2 = bool(int(input()))
    n3 = bool(int(input()))
    
    if n1 == True and n2 == True and n3 == True:
        print(True)
    if n1 == True and n2 == True and n3 == False:
        print(True)
    if n1 == True and n2 == False and n3 == True:
        print(False)    
    if n1 == True and n2 == False and n3 == False:
        print(True)
    if n1 == False and n2 == True and n3 == True:
        print(False)
        
    if n1 == False and n2 == True and n3 == False:
        print(True)
        
    if n1 == False and n2 == False and n3 == True:
        print(False)
    if n1 == False and n2 == False and n3 == False:
        print(True)
        
# 0 - 0 = 1 - 1 = True
# 0 - 1 = 1 - 1 = True
# 1 - 0 = 1 - 1 = True
# 1 - 1 = 0 - 1 = True