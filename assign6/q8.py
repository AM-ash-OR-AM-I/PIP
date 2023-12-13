import re

string1 = """Python Programming Language"""
print(re.search(r"prog", string1))
print(re.findall(r"python|Python", string1))
print(re.search(r"Lang|there", string1).group())
print(re.search(r"L.+e", string1).group())
print(re.search(r"(p|P)ython", string1).group())
print(re.search(r"......m?", string1).group())
print(re.search(r"......m{1,3}", string1).group())
print(re.search(r".*Language", string1).group())
print(re.search(r"\w*\s\w*", string1).group())
print(re.search(r".*", string1).group())

import re

string2 = "Car Number DL5645"
match1 = re.search(r"\w\w?\d{1,4}", string2)
print(match1.group())
match2 = re.search(".*5", string2)
print(match2.group())
match3 = re.search(".*5?", string2)
print(match3.group())
match4 = re.search(r"\d{3}", string2)
print(match4.group())
match5 = re.search("^C.*5$", string2)
print(match5.group())
