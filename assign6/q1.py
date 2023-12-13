def replace_successive(s):
    s1 = ""
    prev = ""
    for x in s:
        if x == prev:
            s1 += "*"
        else:
            s1 += x
        prev = x
    return s1


print(replace_successive("Hello Worldd"))
