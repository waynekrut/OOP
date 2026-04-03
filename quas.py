class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Внесено {amount}. Баланс: {self.__balance}')
        else:
            print("Сумма должна быть положительной")
    def withdraw(self, amount):
        if self.__balance > amount > 0:
            self.__balance -= amount
            print(f"Выведено {amount}. Баланс: {self.__balance}")
        else:
            print("Сумма должна быть положительной")
acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(800)
print(acc.get_balance())
