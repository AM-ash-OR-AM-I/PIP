# Count the number of vowels and consonants in a string.


def is_vowel(c):
    return c in "aeiou"


def is_consonant(c):
    return c.isalpha() and not is_vowel(c)


def count_vowels_consonants(s):
    vowels = consonants = 0
    for c in s:
        if is_vowel(c):
            vowels += 1
        elif is_consonant(c):
            consonants += 1
    return vowels, consonants


s = input("Enter string: ")
vowels, consonants = count_vowels_consonants(s)
print(f"Vowels: {vowels}, Consonants: {consonants}")
