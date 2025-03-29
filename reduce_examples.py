from functools import reduce

# reduce(func, seq)
a = [1, 2, 3, 4]

product_a = reduce(lambda x, y: x * y, a)
print(product_a)
