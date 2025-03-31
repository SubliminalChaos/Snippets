def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()
h = mygenerator()

print(sum(g))
print(sorted(h))
