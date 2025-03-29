# filter(func, seq)
a = [1, 2, 3, 4, 5]
b = filter(lambda x: x % 2 == 0, a)
print(b)
print(list(b))

c = [x for x in a if x % 2 == 0]
print(c)
