# Find the character having maximum frequency in a string


def max_freq(s):
    d = {}
    for x in s:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

    char_max_freq = max(d, key=d.get)  # get key of max value
    max_freq = d[char_max_freq]  # get max value
    return char_max_freq, max_freq


print(*max_freq(input("Enter string: ")))
