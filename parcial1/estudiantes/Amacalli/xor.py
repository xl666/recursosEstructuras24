def xor (x, y):
    return bool((x and not y) or (not x and y))

x = int(input())
y = int(input())

print(xor(x, y))