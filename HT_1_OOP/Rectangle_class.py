# Создайте класс Rectangle, который имеет атрибуты width и height и методы класса:
# area() - возвращает площадь прямоугольника

class Rectangle:
    def __init__(self, width, height):
        self.width = round(width, 2)
        self.height = round(height, 2)

    def area(self):
        self.s = self.width * self.height
        print(self.s)



