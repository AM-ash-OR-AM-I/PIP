import re

digits = input("Enter digits: ")

if res:=re.search(r"^\d{10}$", digits):
    print(f"{res.group()} is Valid number")
else:
    print("Not a valid number")