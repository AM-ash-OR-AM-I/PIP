def check_anagram(s1, s2):
    count = {}

    for x in s1:
        if x not in count:
            count[x] = 1
        else:
            count[x] += 1

    for x in s2:
        if x not in count or count[x] == 0:
            return False
        else:
            count[x] -= 1

    return True


print(check_anagram("silent", "listen"))
print(check_anagram("silent", "listens"))
