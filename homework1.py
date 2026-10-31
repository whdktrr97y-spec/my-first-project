class BankCard:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # Проверяем, что сумма больше нуля
        if amount > 0:
            self.balance = self.balance + amount
        else:
            print("Ошибка: сумма пополнения должна быть больше 0")

    def pay(self, amount):
        # Проверяем, хватает ли денег на карте
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Ошибка: недостаточно средств")

    def info(self):
        print("Владелец:", self.owner, "| Баланс:", self.balance)


# Создаем две карты
card1 = BankCard("Азамат", 5000)
card2 = BankCard("Айпери", 3000)

# Выполняем операции примера
card1.deposit(2000)
card1.pay(900)
card2.pay(500)

# Выводим результат
card1.info()
card2.info()
