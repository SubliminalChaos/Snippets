# lambda arguments : expression

add10 = lambda x: x + 10
print(add10)
print(add10(5))


def add10_func(x):  # equivilent function
    return x + 10


mult = lambda x, y: x * y
print(mult(2, 7))

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D)
print(points2D_sorted)

points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D_sorted)
