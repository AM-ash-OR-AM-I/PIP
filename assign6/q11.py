# Find the character having maximum frequency in a string


def max_freq(s):
    d = {}
    for x in s:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
        # max_freq = max(max_freq, d[x])
    # return max_freq
    char_max_freq = max(d, key=d.get)
    max_freq = d[char_max_freq]
    return char_max_freq, max_freq


print(*max_freq(input("Enter string: ")))
