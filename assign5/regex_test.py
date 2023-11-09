import re

s = input("Enter a string: ")
k = int(input("Number of match: "))
n = len(s)

if re.search(r"\d"*k, s):
    print(f"At least {k} digits")
else:
    print(f"less than {k}-digits")