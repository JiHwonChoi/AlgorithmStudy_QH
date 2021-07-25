import math

class Circle :
    radius = 2

    def area(self):
        return 3.14 * (self.radius**2)

print("원의 면적: {}".format(Circle().area()))
