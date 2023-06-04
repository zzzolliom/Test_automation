# Создайте класс Circle, который имеет атрибут radius и методы класса:
# area() - возвращает площадь круга
# perimeter() - возвращает периметр круга
from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        self.s = pi * (self.radius**2)
        self.s = round(self.s, 4)
        print(self.s)
        return  self.s


    def perimeter(self):
        self.p = 2*pi*self.radius
        self.p = round(self.p, 4)
        print(self.p)
        return self.p

circle1 = Circle(5)
circle1.area()
circle1.perimeter()