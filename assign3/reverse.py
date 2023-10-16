"""
Reverse any number without using any string functions
"""


def reverse(n):
    rev_n = 0
    while n != 0:
        n, r = divmod(n, 10)
        rev_n = rev_n * 10 + r
    return rev_n


def palindrome(n):
    return n == reverse(n)


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print("The reverse of the number is:", reverse(n))
    if palindrome(n):
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")
