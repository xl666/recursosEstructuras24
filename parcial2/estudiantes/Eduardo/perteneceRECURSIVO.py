def pertenece(l, e):
    if not l:
        return False
    return l[0] == e or pertenece(l[1:], e)
    
if __name__ == "__main__":
    e = int(input())
    n = int(input())
    l = [int(input()) for _ in range(n)]
    print(pertenece(l, e))
