class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * 3.14

    def perimeter(self):
        return self.radius * 2 * 3.14


circle1 = Circle(radius=1)
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 18.85
