class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

def print_area(shape):
    print(f'Площадь: {shape.area()}')

shapes = [Rectangle(5, 10), Circle(7)]
for shape in shapes:
    print_area(shape)