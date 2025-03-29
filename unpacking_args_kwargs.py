# variadic functions


def foo(*args, **kwargs):
    print(f"Positional: {args}")


foo(100, 50, 25)
foo(100, 50, 25, 1)
foo(100)


def bar(*args, **kwargs):
    print(f"Named: {kwargs}")


bar(galleons=100, sickles=50, knuts=25)
bar(galleons=100, sickles=50, knuts=25, pennies=1)
