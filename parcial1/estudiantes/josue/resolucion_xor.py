booleano1 = bool(int(input()))
booleano2 = bool(int(input()))


def xor(booleano1, booleano2):
    if booleano1 == booleano2:
        return False
    return True

print (xor(booleano1, booleano2))