import math


class Circle:
    def __init__(self, r):
        self.radius = r

    def __str__(self):
        return "Circle with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other.radius)

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, d):
        self.radius = d / 2

    @property
    def area(self):
        return round(math.pi * self.radius ** 2, 6)

    @classmethod
    def from_diameter(Circle, d):
        self = Circle(d / 2)
        return self


