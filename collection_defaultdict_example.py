from collections import defaultdict

# Will have a default value if the key has not been set yet.

d = defaultdict(int)
d['a'] = 1
d['b'] = 2

print(d)
print(d['c'])
