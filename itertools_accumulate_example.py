# Iterable - a data type that can be used in a for loop
from itertools import accumulate
import operator

# returns accumulated sums or other operators given as input

a = [1, 2, 3, 4]
acc = accumulate(a)  # default to computeing sums
print(acc)
print(list(acc))

acc = accumulate(a, func=operator.mul)
print(list(acc))

a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(list(acc))
