# Check if a string contains at least one digit and one alphabet.

s = input("Enter string: ")
digit = False
alpha = False
for x in s:
    if x.isalpha():
        alpha = True
    elif x.isdigit():
        digit = True

print(
    "Contains at least one digit and one alphabet"
    if digit and alpha
    else "Does not contain at least one digit and one alphabet"
)
