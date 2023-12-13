# Count frequency of characters in a string

d = {}


def count_freq(s):
    for x in s:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1


count_freq(input("Enter string: "))

print(*(f"'{k}': {v}" for k, v in d.items()), sep=", ")
