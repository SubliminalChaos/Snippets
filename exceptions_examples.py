try:
    a = 5 / 1
    b = a + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:  # else clause ran when no exception
    print("everything is fine")
finally:  # finally always ran whether exception or not
    print("cleaning up")

print()


class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
    if x < 10:
        raise ValueTooSmallError("value is too small", x)


try:
    test_value(5)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)

print("\nthank you.")
