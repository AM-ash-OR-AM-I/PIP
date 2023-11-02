import re

with open("./assign3.txt", "r") as f:
    text = f.read()

# assuming the text is stored in a variable called 'text'
pattern = r"[1-9]\..*\n.*\n.*\nAns:"
pattern = r"^[1-9]\..*\nAns:"
# pattern1 = r"(?:^[1-9]\..*|^[^\d].*)\n((?:.*\n){1,6}Ans:)"
# pattern2 = r"^[1-9]\..*?Ans:$"
# pattern = r"^[1-9]\..*Ans:$"
matches = re.findall(pattern, text, re.MULTILINE)

# print all the matches
for n, match in enumerate(matches):
    print("-" * 50)
    print(f"Match {n+1}:")
    print(match)
    print("-" * 50)
