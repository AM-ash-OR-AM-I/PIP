# Remove duplicates from a string.
def remove_duplicates(s):
    set_s = set()
    s1 = ""
    for x in s:
        if x not in set_s:
            s1 += x
            set_s.add(x)
    return s1


# Remove duplicates from a list.
def remove_duplicates_from_list(l):
    unique_elements = set()
    indexes_to_remove = []
    for i, x in enumerate(l):
        if x not in unique_elements:
            unique_elements.add(x)
        else:
            indexes_to_remove.append(i)

    for i in indexes_to_remove[::-1]:
        del l[i]


# Don't take extra space.
def remove_duplicates_no_extraspace(l: list):
    for x in l:
        while l.count(x) > 1:
            index = l.index(x, l.index(x) + 1)
            l.pop(index)


# print(remove_duplicates(input("Enter string: ")))
l = eval(input("Enter list: "))
remove_duplicates_no_extraspace(l)
print(l)
