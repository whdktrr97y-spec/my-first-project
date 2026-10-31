# Принципы ООП - Наследование 

class Devise:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.brand = model
        self.brand = price

        self.has__power = False

    def power(self) -> None:
        self.has__power = not self.has__power
        state = "Включено" if self.has__power else "Выключено"
        print(f"Устройство{self.brand} {self.model}, Состояние {state}")

    def info(self) -> str:
        return f"{self.brand} {self.model} Цена:{self.price:.2f} сом"



class SmartPhone(Devise):
    def __init__(self, brand, model, price, screen_size, camera):
        super().__init__(brand, model, price)

        self.screen_size =  screen_size
        self.camera = camera

    def get_info(self):
        base_info = super().info()
        return f"Смартфон: {base_info}, экран: {self.screen_size}, камера: {self.camera}"


class Laptop(Devise):
    def __init__(self, brand, model, price, cpu, gpu, ram):
        super().__init__(brand, model, price)

        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram

    def get_info(self):
        return f"Ноутбук: {super().info()}, Процессор: {self.cpu}, Озу: {self.ram}, ГПУ: {self.gpu}"   
phone = SmartPhone(
    brand = "Vivo",
    model = "300",
    price = 70000,
    screen_size = "7.1 дюйм",
    camera = "1080px"
)
Laptop = Laptop(
    brand = "Acer",
    model = "Predator Helios",
    price = 4299.999999,
    cpu = "Core Ultra 9, 5.7 ГГц",
    ram = "64 ГБ RAM DDR 5",
    gpu = "RTX 5090 32gb"
)
print(phone.get_info())
print(Laptop.get_info())



# ООП принципы - полиформизм
class DeveLoper:
    def __init__(self, stack):
        self.stack = stack

    def stack_name(self):
        return f"{self.stack}: Разработчик"

class BackEnd(DeveLoper):
    def __init__(self, stack, db):
        super().__init__(stack)
        self.db = db

    def stack_name(self):
        return f"Стек {self.stack} База данных: {self.db}" 


class FrontEnd(DeveLoper):
    def __init__(self, stack, site_element):
        super().__init__(stack)  
        self.site_element = site_element

    def stack_name(self):
         return f"Стек:{self.stack} Элемент сайта: {self.site_element}"  

dev = DeveLoper("JUNIOR") 
back = BackEnd("Python", "django") 
front = FrontEnd("Javascript", "Htm1/Css") 

razrabotchiki = [dev, back, front]

for chelovek in razrabotchiki:
    print(chelovek.stack_name())

#print(dev.stack_name())


  
    


