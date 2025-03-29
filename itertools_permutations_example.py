# Iterable - a data type that can be used in a for loop
from itertools import permutations

# return all possible orderings of an input

a = [1, 2, 3]
perm = permutations(a)
print(perm)
print(list(perm))

perm = permutations(a, 2)
print(list(perm))
