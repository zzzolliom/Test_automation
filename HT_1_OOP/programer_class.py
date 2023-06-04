# Заддание 1 "Работа не волк"
# Рассмотрим объект «Программист», который задаётся именем, должностью и количеством отработанных часов. Каждая должность имеет собственный оклад (заработную плату за час работы). В нашей импровизированной компании существуют 3 должности:
#
# Junior — с окладом 10 тугриков в час;
# Middle — с окладом 15 тугриков в час;
# Senior — с окладом 20 тугриков в час по умолчанию и +1 тугрик за каждое новое повышение.
# Напишите класс Programmer, который инициализируется именем и должностью (отработка у нового работника равна нулю). Класс реализует следующие методы:
#
# work(time) — отмечает новую отработку в количестве часов time;
# rise() — повышает программиста;
# info() — возвращает строку для бухгалтерии в формате: <имя> <количество отработанных часов>ч. <накопленная зарплата>тгр.
salary_dict = {'Junior': 10, 'Middle': 15, 'Senior': 20}


class Programmer:
    def __init__(self, name, grid,salary_dict):
        self.salary_dict = salary_dict
        self.senior_rise_count = 0
        self.name = name
        self.grid = grid
        self.hours_worked = 0
        self.salary = salary_dict.get(self.grid)
        self.count_tugrik = 0
    def work_time(self,hours):
        self.hours_worked += hours

    def rise_grid_or_salary(self):
        if self.grid == 'Junior':
            self.grid = 'Middle'
        elif self.grid == 'Middle':
            self.grid = 'Senior'
        elif self.grid == 'Senior':
            self.senior_rise_count += 1
        else:
            print('Это только для программистов')
        self.salary = salary_dict.get(self.grid)
    def info(self):
        self.count_tugrik = (self.salary + self.senior_rise_count) * self.hours_worked
        print(f'Имя: {self.name}, отработано {self.hours_worked} часов, ЗП: {self.count_tugrik}')


proger1 = Programmer('Вася','Junior',salary_dict)
proger2 = Programmer('Гена','Middle',salary_dict)
proger3 = Programmer('Игнат','Middle',salary_dict)
proger3.work_time(100)
proger2.work_time(130)
proger1.work_time(160)
proger1.rise_grid_or_salary()
print(proger1.grid)
proger1.rise_grid_or_salary()
print(proger1.grid)
proger1.rise_grid_or_salary()
print(proger1.grid)
print(proger1.salary)
proger1.rise_grid_or_salary()
proger1.info()
proger2.info()
proger3.info()