# Родительский класс
class Character:

    def __init__(self, name, health):
        self.name = name  # Имя
        self.health = health  # Здоровье

    def attack(self):
        print(self.name, "атакует!")

    # Дополнительное задание
    def show_info(self):
        print(f"Имя: {self.name}, Здоровье: {self.health}")


# Дочерний класс: Воин
class Warrior(Character):

    def attack(self):
        print(self.name, "атакует мечом!")


# Дочерний класс: Маг
class Mage(Character):

    def attack(self):
        print(self.name, "использует заклинание!")


# Дочерний класс: Лучник
class Archer(Character):

    def attack(self):
        print(self.name, "стреляет из лука!")


# Создание персонажей и проверка работы
if __name__ == "__main__":
    # Создаем объекты
    warrior = Warrior("Конан", 150)
    mage = Mage("Гэндальф", 80)
    archer = Archer("Леголас", 110)

    
    warrior.show_info()
    mage.show_info()
    archer.show_info()

    print() 

    # Каждый атакует по-своему (полиморфизм)
    warrior.attack()
    mage.attack()
    archer.attack()
