"""Write a function that generates a random password. The password should have a random length of
between 7 and 10 characters. Each character should be randomly selected from positions 33 to 126
in the ASCII table. Your function will not take any parameters. It will return the randomly generated
password as its only result. Display the randomly generated password in your file’s main program."""

import random


def generate_random_password():
    length = random.randint(7, 10)
    password = ""
    for _ in range(length):
        password += chr(random.randint(33, 126))
    return password


if __name__ == "__main__":
    password = generate_random_password()
    print("Randomly generated password:", password)
