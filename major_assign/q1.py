"""Write a program that converts a binary (base 2) number to a decimal (base 10). Your program should
begin by reading the binary number from the user as a string. Then, it should compute the equivalent
decimal number by processing each digit in the binary number. Finally, your program should display
the equivalent decimal number with an appropriate message."""

binary_number = input("Enter a binary number: ")
decimal_number = 0

for digit in binary_number:
    decimal_number = decimal_number * 2 + int(digit)

print("The equivalent decimal number is:", decimal_number)
