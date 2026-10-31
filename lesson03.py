# Урок 3. ООП принципы: инкапсуляция и абстракция
import re
class SecureAccount:
    def __init__(self, username, pin, email, initial_balance):
        self.username = username
        self.pin = pin  # нельзя переписывать 
        self.email = email  # марка что ее нельзя использовать
        self.initial_balance = initial_balance

    @property # декаротар
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, new_email) -> None:
        email_regex = r"^[w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_regex, new_email):
            raise ValueError("Неккоректный имейл адрес!")
        print(f"Имейл успешно изменен {self._email} -> {new_email}")
        self._email = new_email
        
