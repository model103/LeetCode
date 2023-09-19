import math


def circle_area(r):
    a = r ** 2

    def get_a():
        return a

    return a * math.pi, get_a


s, get_a = circle_area(5)
print(get_a())
