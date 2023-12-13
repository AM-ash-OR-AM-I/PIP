import re


def count_words(s):
    return len(re.findall(r"\s", s)) + 1


print(count_words("Hello world this is test"))
