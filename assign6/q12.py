# Check if a pair of strings are anagram to each other. Example: SILENT and LISTEN are anagrams, without sorting.

s1, s2 = input("Enter string 1 and string2: ").split()

print(
    f"{s1} and {s2} are anagrams"
    if sorted(s1) == sorted(s2)
    else f"{s1} and {s2} are not anagrams"
)
