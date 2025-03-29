# Iterable - a data type that can be used in a for loop
from itertools import product

a = [1, 2]
b = [3, 4]
prod = product(a, b)  # compute the product of iterable
print(prod)
print(list(prod))

a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)  # compute the product of iterable
print(list(prod))
