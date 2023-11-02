"""5. The following table lists the sound level in decibels for several common noises. Write a program that
reads a sound level in decibels from the user. If the user enters a decibel level that matches one of the
noises in the table then your program should display a message containing only that noise. If the user
enters a number of decibels between the noises listed then your program should display a message
indicating which noises the value is between. Ensure that your program also generates reasonable
output for a value smaller than the quietest noise in the table, and for a value larger than the loudest
noise in the table.
Jackhammer 130 dB
Gas Lawnmower 106 dB
Alarm Clock 70 dB
Quiet Room 40 dB"""

from itertools import pairwise

noises = [
    (40, "Quiet Room"),
    (70, "Alarm Clock"),
    (106, "Gas Lawnmower"),
    (130, "Jackhammer"),
]


def get_noise(decibels):
    for lower, higher in pairwise(noises):
        if decibels == lower[0]:
            return lower[1]
        elif decibels == higher[0]:
            return higher[1]
        elif lower[0] < decibels < higher[0]:
            return f"Between {lower[1]} and {higher[1]}"


if __name__ == "__main__":
    decibels = int(input("Enter the decibel level: "))
    print(get_noise(decibels))
