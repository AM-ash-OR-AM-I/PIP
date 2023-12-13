# Find length of a string without using inbuilt function


def length(s):
    count = 0
    for _ in s:
        count += 1
    return count


print(length(input("Enter string: ")))
