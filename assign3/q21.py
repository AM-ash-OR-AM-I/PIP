def prime_factors(n):
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return factors


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(prime_factors(n))
