#
# @mydecorator
# def dosomething():
#     pass
#
# decorator: a func that takes another func as argument, and
#     extends the behavior of this func without explicitly
#     modifying it. in other words, a decorator allows you to
#     add new functionality to an existing function.
#
# dosomething is extended by the functionality of the mydecorator decorator
import functools

# decorator template; for func w/wo return value, w/wo args and more
def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func()
        print('End')
        return result
    return wrapper


def print_name1():
    print('Alex')


@start_end_decorator
def print_name2():
    print('Alex')


print_name1()
print()
print_name2()

def add5(x):
    return x + 5

print(add5(10))
