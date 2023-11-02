import re

string1 = "Python Programming Language"
print(f"{re.search(r"......m?", string1).group() = }")
print(f"{re.search(r"......m{1,3}", string1).group() = }")
print(f"{re.search(r".*Language", string1).group() = }")
print(f"{re.search(r'\w*\s\w*', string1).group() = }")
print(f"{re.search(r".*", string1).group() = }")
