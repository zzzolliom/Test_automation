# Создайте класс BankAccount, который имеет атрибуты owner и balance и методы класса:
# deposit() - позволяет внести деньги на счет
# withdraw() - позволяет снять деньги со счета

class BankAccount:
    def __init__(self, owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_money):
        self.balance += deposit_money

    def withdraw(self, withdraw_money):
        self.balance -= withdraw_money

    def __str__(self):
        return f'Имя:{self.owner}, депозит: {self.balance}'
