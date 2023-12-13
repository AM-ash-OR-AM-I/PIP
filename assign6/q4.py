def capitalize(w):
    w1 = ""
    for i, x in enumerate(w):
        if i == 0:
            if 97 <= ord(x) <= 122:
                w1 += chr(ord(x) - 32)
            else:
                w1 += x
        else:
            if 97 <= ord(x) <= 122:
                w1 += x
            else:
                w1 += chr(ord(x) + 32)
    return w1


print(capitalize("hello"))
print(capitalize("HELLO"))
