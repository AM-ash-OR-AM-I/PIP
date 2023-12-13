"""Write two functions, hex2int and int2hex, that convert between hexadecimal digits (0, 1, 2, 3, 4, 5,
6, 7, 8, 9, A, B, C, D, E and F) and decimal (base 10) integers. The hex2int function is responsible
for converting a string containing a single hexadecimal digit to a base 10 integer, while the int2hex
function is responsible for converting an integer between 0 and 15 to a single hexadecimal digit. Each
function will take the value to convert as its only parameter and return the converted value as its only
result. Ensure that the hex2int function works correctly for both uppercase and lowercase letters.
Your functions should display a meaningful error message and end the program if the parameter’s
value is outside of the expected range."""


def hex2int(hex_digit):
    if len(hex_digit) > 1:
        print("Error: Enter single hex digit")
        exit()
    try:
        return int(hex_digit, 16)
    except ValueError:
        print("Error: Invalid hexadecimal digit")
        exit()


def int2hex(decimal):
    if decimal < 0 or decimal > 15:
        print("Error: Decimal value out of range")
        exit()
    return hex(decimal)[2:].upper()


if __name__ == "__main__":
    print("Decimal equivalent:", hex2int(input("Enter a hexadecimal digit: ")))
    print("Hexadecimal equivalent:", int2hex(int(input("Enter a decimal value: "))))
