total = 0
N = 5
for i in range(1, N + 1):
    for j in range(1, i + 1):
        for k in range(1, j + 1):
            total += 1
print(total)
