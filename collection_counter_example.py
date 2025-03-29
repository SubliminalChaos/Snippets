from collections import Counter

a = "aaaaaabbbbbbbccc"  # a can be any iterable
my_counter = Counter(a)

print(my_counter)
print(my_counter.most_common(1))
print(my_counter.most_common(2))
print()
print(my_counter.most_common(1)[0][0])
print(my_counter.elements())
print(list(my_counter.elements()))
