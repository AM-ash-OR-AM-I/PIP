"""(Arbitrary Base Conversions) Write a program that allows the user to convert a number from one
base to another. Your program should support bases between 2 and 16 for both the input number
and the result number. If the user chooses a base outside of this range then an appropriate error
message should be displayed and the program should exit. Divide your program into several functions,
including a function that converts from an arbitrary base to base 10, a function that converts from base
10 to an arbitrary base, and a main program that reads the bases and input number from the user."""


def convert_to_base_10(number, base):
    # Convert number from arbitrary base to base 10
    decimal = 0
    power = 0
    while number > 0:
        digit = number % 10
        decimal += digit * (base**power)
        number //= 10
        power += 1
    return decimal


def convert_from_base_10(number, base):
    # Convert number from base 10 to arbitrary base
    result = ""
    while number > 0:
        digit = number % base
        result = str(digit) + result
        number //= base
    return result


def main():
    # Read bases and input number from the user
    input_number = int(input("Enter the number: "))
    input_base = int(input("Enter the base of the input number: "))
    result_base = int(input("Enter the base of the result number: "))

    # Check if bases are within the supported range
    if input_base < 2 or input_base > 16 or result_base < 2 or result_base > 16:
        print("Error: Bases should be between 2 and 16.")
        return

    # Convert input number to base 10
    decimal_number = convert_to_base_10(input_number, input_base)

    # Convert base 10 number to result base
    result_number = convert_from_base_10(decimal_number, result_base)

    # Print the result
    print("Result:", result_number)


if __name__ == "__main__":
    main()
