"9. Write a program to find the maximum of three numbers using a nested function"


def max_of_three(a, b, c):
    def max_of_two(a, b):
        if a > b:
            return a
        else:
            return b

    return max_of_two(a, max_of_two(b, c))


if __name__ == "__main__":
    a, b, c = map(int, input("Enter three numbers: ").split())
    print("The maximum of the three numbers is:", max_of_three(a, b, c))
