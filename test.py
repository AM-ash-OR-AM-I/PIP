def sum4dig(n):
    a = n % 10
    n //= 10
    b = n % 10
    n //= 10
    c = n % 10
    n //= 10
    d = n % 10
    return a * (a % 2 == 0) + b * (b % 2 == 0) + c * (c % 2 == 0) + d * (d % 2 == 0)


n = int(input())
print(sum4dig(n))
