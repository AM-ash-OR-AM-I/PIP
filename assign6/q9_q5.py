# Given a string s and index i, delete ith value from s


def delete(s, i):
    return s[:i] + s[i + 1 :]


s, i = input("Enter string and index: ").split()
print(f"New string: {delete(s, int(i))}")
