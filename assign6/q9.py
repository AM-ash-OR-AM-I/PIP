# Remove duplicates from a string.


def remove_duplicates(s):
    return "".join(sorted(set(s), key=s.index))


print(remove_duplicates(input("Enter string: ")))
