"""
3. Check if a string is symmetric or asymmetric
"""

s = input("Enter string: ")
mid = len(s) // 2
symmetric = s[:mid] == s[mid:] if len(s) % 2 == 0 else s[:mid] == s[mid + 1 :]
print("Symmetric" if symmetric else "Asymmetric")
