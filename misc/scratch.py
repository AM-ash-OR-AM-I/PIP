# Reduce
from functools import reduce
import operator as op

l = [1, 2, 3, 4]

xor_sum = reduce(op.xor, l)
print(xor_sum)

# zipping multiple lists

l1 = [1, 2, 3, 4]
l2 = [6, 3, 6, 4]
l3 = [7, 3, 4, 5]

print(*zip(l1, l2, l3))


# Set operations

l1 = list(range(1, 10))
l2 = list(range(5, 15))
l3 = list(range(8, 18))
s1 = set(l1)
s2 = set(l2)
s3 = set(l3)

print(s1.intersection(s2, s3))
print(s1.difference(s2))  # Same as s1 - s2
print(s1.symmetric_difference(s2))  # Same as s1 ^ s2
print(s1.union(s2))  # Same as s1 | s2
print(s1.issubset(s2))  # Same as s1 <= s2

s1 -= s2  # Same as s1.difference_update(s2)
s1 &= s2  # Same as s1.intersection_update(s2)
s1 ^= s2  # Same as s1.symmetric_difference_update(s2)
s1 |= s2  # Same as s1.update(s2)
print(s2)
print(s1)
