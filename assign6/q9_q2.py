"""
Reverse a string without reversing the words. Example:
input data: 'welcome to iter'
output: 'iter to welcome'
"""

s = input("Enter string: ")
print(*s.split(" ")[::-1])
