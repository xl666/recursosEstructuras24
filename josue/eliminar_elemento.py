if __name__ == '__main__':
    v = int(input())
    n = int(input())
    l1 = [int(input())for _ in range(n)]

    l1 = [num for num in l1 if not num == v]
    print(l1)