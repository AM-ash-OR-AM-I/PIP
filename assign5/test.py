import re

special = r"[!@#$%^&*()_+]"
digits = r"\d"
upper = r"[A-Z]"
lower = r"[a-z]"

# pattern = f"^{special}+{digits}+{upper}+{lower}+$"
# How to write a pattern for a string that has at least 1 special char, 1 digit, 1 upper and 1 lower case char anywhere in the string, also the string must be at least 8 char long.

full_pattern = f"^(?=.*{special})(?=.*{digits})(?=.*{upper})(?=.*{lower}).{{8,}}$"
simple_pattern = f"^{special}+{digits}+{upper}+{lower}+$"

string = input("Enter a string: ")
match = re.match(full_pattern, string)
if match:
    print(f"Matched: {match.group()}")
else:
    print("Not Matched")
