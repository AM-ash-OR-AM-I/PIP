"""
8. Write a function to determine whether a given natural number is perfect. A natural number is said to
be a perfect number if it is the sum of its divisors. For Example, 6 is a perfect number because 6 =
1+2+3, but 15 is not because 15 != 1+3+5.
"""


def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if is_perfect(n):
        print("The number is perfect")
    else:
        print("The number is not perfect")
