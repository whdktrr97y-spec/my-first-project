# ООП объектно ориентированное программирование

# Класс это чертеж чего либо, чертеж это макет то есть его нельзя напрямую использовать
# Объект (экземпляр) это полноценная сделанная по чертежу вещь
 
class Cat:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def say_meow(self):
        print(f'{self.name} МЯУ-МЯУ')

cat1 = Cat(name= "Лео", color= "черный")
print(cat1.name, cat1.color)

print(cat1.say_meow)
cat1.say_meow()

cat2 = Cat(name= "лили", color= "белый")
print(cat2.name,cat2.color)



class PiggyBank:
    def __init__(self, owner):
        self.owner = owner
        self.coins = 0

    def add_money(self, amount: int):
        if amount > 0:
            self.coins += amount
            print(f"В копилку {self.owner}, добавлено {amount} монет, Всего {self.coins} денег")
        else:
            print(f"Введите правильную сумму монет в числах(1,2,3,4,5)")    

    def break_piggy(self) -> int:
        saved = self.coins
        self.coins = 0
        print(f"Вы разбили копилку {self.owner}, в ней {saved} монет")
        return saved
    
mr_piggy = PiggyBank("мурзик")
mr_piggy.add_money(100)
mr_piggy.add_money(500)
mr_piggy.add_money(900)

mr_piggy.break_piggy()

cash = mr_piggy.break_piggy()
print(f"У нас на руках теперь: {cash} сом.")
print(f"Остаток в копилке: {mr_piggy.coins} сом.")









