# A common pattern you'll find in code:
#
#   Argument to __init__ passes initial value
#   Value is assigned to a private attribute
#   @property method with same name uses the private attribute
#   @.setter method with same name sets the private attribute
#       with error coding
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("Radius must be a positive number")
        self._radius = value


small = Circle(3)
small.radius = 4  # use function as attribute
print(small.radius)  # use function as attribute
