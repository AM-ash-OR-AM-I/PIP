import re

string1 = """
Python Programming python Le Language
Hello World this
Hi there
"""
print(re.search(r"prog"))
print(re.findall(r"python|Python", string1))
print(re.search(r"Lang|there", string1).group())
print(re.search(r"L.+e", string1).group())
print(re.search(r"(p|P)ython", string1).group())
print(re.search(r"......m?", string1).group())
print(re.search(r"......m{1,3}", string1).group())
print(re.search(r".*Language", string1).group())
print(re.search(r'\w*\s\w*', string1).group())
print(re.search(r".*", string1).group())