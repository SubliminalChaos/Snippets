try:
    a = 5 / 1
    b = a + "David"
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

print("thank you.")
