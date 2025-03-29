# Iterable - a data type that can be used in a for loop
from itertools import combinations, combinations_with_replacement

# combinations vs permutations: AB and BA are
#     different for permutations

a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(comb)
print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))
