# Check if a string is palindrome.


def is_palindrome(s):
    return s == s[::-1]


s = input("Enter a string: ")
print(f"{s} is{(not is_palindrome(s))*'not'} palindrome")
