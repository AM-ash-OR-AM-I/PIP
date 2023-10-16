"""
Write a function that finds the sum of the n terms of the following series:
a.
1 − x2/2! + x4/4! − x6/6! + ...xn/n!
"""

import math


def series(x, n):
    series_sum = 0
    for i in range(n):
        series_sum += ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    return series_sum


if __name__ == "__main__":
    x, n = map(int, input("Enter x and n: ").split())
    print("The sum of the series is:", series(x, n))
