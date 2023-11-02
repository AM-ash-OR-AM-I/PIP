"""
4. A roulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18 are red, and two are green.
The green spaces are numbered 0 and 00. The red spaces are numbered 1, 3, 5, 7, 9, 12, 14, 16, 18,
19, 21, 23, 25, 27, 30 32, 34 and 36. The remaining integers between 1 and 36 are used to number
the black spaces. Many different bets can be placed in roulette. We will only consider the following
subset of them in this exercise:
– Single number (1 to 36, 0, or 00)
– Red versus Black
– Odd versus Even (Note that 0 and 00 do not pay out for even)
– 1 to 18 versus 19 to 36
Write a program that simulates a spin of a roulette wheel by using Python’s random number generator.
Display the number that was selected and all of the bets that must be payed. For example, if 13 is
selected then your program should display:
The spin resulted in 13...
Pay 13
Pay Black
Pay Odd
Pay 1 to 18
If the simulation results in 0 or 00 then your program should display Pay 0 or Pay 00 without any
further output
"""

import random

def spin():
    return random.randint(0, 37)

def get_color(number):
    if number == 0:
        return "Green"
    elif number % 2:
        return "Black"
    else:
        return "Red"

def get_parity(number):
    if number == 0 or number == 37:
        return "Neither"
    elif number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def get_range(number):
    if number == 0 or number == 37:
        return "Neither"
    elif number <= 18:
        return "1 to 18"
    else:
        return "19 to 36"

def main():
    number = spin()
    print("The spin resulted in", (number if number != 37 else "00"))
    print("Pay", number if number != 37 else "00")
    print("Pay", get_color(number))
    print("Pay", get_parity(number))
    print("Pay", get_range(number))

if __name__ == "__main__":
    main()
