def xor(x, y):
    return (bool(x) or bool(y)) and not (bool(x) and bool(y))

input1 = int(input())
input2 = int(input())


result = xor(input1, input2)
print(result)
