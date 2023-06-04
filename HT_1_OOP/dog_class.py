# Создайте класс Dog, который имеет атрибуты name, breed и age. Методы класса должны быть следующими:
# bark() - выводит на экран ‘Woof!’
# doginfo() - выводит на экран информацию о собаке в формате “name is breed and is age years old”

class Dog:
    def __init__(self,name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print('Woof')

    def doginfo(self):
        print(f'{self.name} is {self.breed} and is {self.age} years old')


