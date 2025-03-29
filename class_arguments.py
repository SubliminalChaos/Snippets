class ObjectCounter:
    num_instances = 0  # class attribute

    def __init__(self):
        ObjectCounter.num_instances += 1


one = ObjectCounter()

print(one)
print(one.num_instances)

two = ObjectCounter()

print(ObjectCounter.num_instances)

# NOTE: 1) objects can have attributes assigned dynamically.
#       2) an attribute with the same name as a class attribute will
#              shadow the class attribute
