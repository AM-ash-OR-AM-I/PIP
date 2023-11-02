"""
Write a program that prints Armstrong numbers in the range 1 to 1000. An Armstrong number is a
number whose sum of the cubes of the cubes of the digits is equal to the number itself. For Example,
370 = 33 + 73 + 03
"""


def is_armstrong(n):
    return sum(map(lambda x: x**3, map(int, str(n)))) == n


if __name__ == "__main__":
    for i in range(1, 1001):
        if is_armstrong(i):
            print(i, end=" ")
    print()
