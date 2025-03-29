# Iterable - a data type that can be used in a for loop
from itertools import count, cycle, repeat

for i in count(10):  # count up from 10
    print(i)
    if i == 15:
        break

for y in repeat(1, 4):
    print(y)

a = [1, 2, 3]
for x in cycle(a):  # INFINITE LOOP!
    print(x)
