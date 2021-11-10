from random import random

class Vector:
    #just so Python knows this exists
    def __init__(self, x, y):
        pass

class Vector(object):
    """
    Vector(x, y) -> object with x and y
    can be added, multiplied and converted to a string, list or tuple
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def copy(self):
        return Vector(self.x, self.y)

    def random(scale = Vector(1, 1)):
        return Vector(
            scale.x * random(),
            scale.y * random()
        )

    def __str__(self):
        return "(%.0f, %.0f)" % (self.x, self.y)
    def __repr__(self):
        return "V(%.0f, %.0f)" % (self.x, self.y)
    def __list__(self):
        return [self.x, self.y]
    def __tuple__(self):
        return (self.x, self.y)

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self
    def __neg__(self):
        return Vector(self.x, self.y)

    def __mul__(self, factor):
        return Vector(
            self.x * factor,
            self.y * factor,
        )
    def __imul__(self, factor):
        self.x *= factor
        self.y *= factor
        return self
    def __truediv__(self, factor):
        return Vector(
            self.x / factor,
            self.y / factor,
        )
    def __itruediv__(self, factor):
        self.x /= factor
        self.y /= factor
        return self
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** .5
    def __iter__(self):
        for coordinate in [self.x, self.y]:
            yield coordinate

    def combine(self, other, other_proportion):
        keep = 1 - other_proportion
        self.x = self.x * keep + other.x * other_proportion
        self.y = self.y * keep + other.y * other_proportion
