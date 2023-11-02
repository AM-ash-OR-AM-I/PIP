# Remove duplicates from a string.


def remove_duplicates_short(s):
    return "".join(sorted(set(s), key=s.index))


def remove_duplicates(s):
    set_s = set()
    s1 = ""
    for x in s:
        if x not in set_s:
            s1 += x
            set_s.add(x)
    return s1


# print(remove_duplicates_short(input("Enter string: ")))
print(remove_duplicates(input("Enter string: ")))
