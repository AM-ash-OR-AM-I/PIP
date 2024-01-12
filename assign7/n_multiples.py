def make_nlists(n):
    multiples_i = [[(i + 1) * j for j in range(5)] for i in range(n)]
    print(*multiples_i, sep="\n")


make_nlists(10)
