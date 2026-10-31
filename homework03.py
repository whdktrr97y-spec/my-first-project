from abc import ABC, abstractmethod
# ЧАСТЬ 1: Класс SmartPhone с инкапсуляцией

class SmartPhone:

    def __init__(self, name: str, battery_level: int, password: str):
        self.name = name  # Публичный атрибут
        self._battery_level = battery_level  # Защищенный атрибут
        self.__password = password  # Приватный атрибут

    # Геттер для получения заряда
    @property
    def battery_level(self) -> int:
        return self._battery_level


    # Сеттер для валидации заряда в пределах 0-100%
    @battery_level.setter
    def battery_level(self, value: int):
        if 0 <= value <= 100:
            self._battery_level = value
        else:
            print(f"❌ Ошибка: неверный заряд ({value}%).")

    # Публичный метод для безопасной проверки скрытого пароля
    def check_password(self, input_password: str) -> bool:
        return self.__password == input_password


# Абстрактный класс-интерфейс
class Notifier(ABC):

    @abstractmethod
    def send(self, message: str):
        pass


class SMSNotifier(Notifier):

    def send(self, message: str):
        print(f"💬 [SMS]: {message}")


class TelegramNotifier(Notifier):

    def send(self, message: str):
        print(f"✈️ [Telegram]: {message}")


if __name__ == "__main__":
    phone = SmartPhone(
        name="iPhone 15", battery_level=50, password="SecretPassword123"
    )

    print(f"Телефон: {phone.name}")

    # Проверка приватности: прямой доступ вызовет ошибку
    try:
        print(phone.__password)
    except AttributeError:
        print("🔒 Доступ к __password ограничен")

    print(f"Пароль '12345': {phone.check_password('12345')}")
    print(
        f"Пароль 'SecretPassword123': {phone.check_password('SecretPassword123')}"
    )

    print(f"\nЗаряд: {phone.battery_level}%")
    phone.battery_level = 75  # Сработает @setter
    print(f"Новый заряд: {phone.battery_level}%")
    phone.battery_level = 120  # Попытка установить некорректный заряд

    print("\nОтправка уведомлений:")
    sms = SMSNotifier()
    tg = TelegramNotifier()

    sms.send("Баланс пополнен.")
    tg.send("Новое сообщение.")
