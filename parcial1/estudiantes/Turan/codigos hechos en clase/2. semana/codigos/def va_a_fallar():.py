def va_a_fallar():
    v = 5/0
    return True





def invocadora():
    b= va_a_fallar()
    return b


print(invocadora())