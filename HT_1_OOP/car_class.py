# Напишите программу с классом Car. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
# Напишите пять методов.
# Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# Третий — присвоение автомобилю года выпуска.
# Четвертый метод — присвоение автомобилю типа.
# Пятый — присвоение автомобилю цвета.
class Car:
    def __init__(self, color="белый", type = 'Седан', year = 2023):
        self.color = color
        self.type = type
        self.year = year
        self.is_start = False

    def start_car(self):
        if not self.is_start:
            self.is_start = True
            print("Автомобиль заведен")
        else:
            print("Автомобиль и был заведен")


    def stop_car(self):
        if self.is_start:
            self.is_start = False
            print("Автомобиль заглушен")
        else:
            print("Автомобиль и был заглушен")

    def set_year(self, year):
        self.year = year

    def set_type(self, type):
        self.type = type

    def set_color(self, color):
        self.color = color

    def __str__(self):
        return  f'Тип:{self.type}, цвет:{self.color}, год:{self.year} , {self.is_start}'


if __name__ == "__main__":
    car1 = Car()
    car1.set_year(2020)
    car1.set_color('синий')
    car1.set_type("лимузин")
    car1.start_car()
    car1.stop_car()
    print(car1)