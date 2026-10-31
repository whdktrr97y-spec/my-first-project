class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    ## стоковые представления
    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    ## Операторы сравнения
    def __eq__(self, other):   ## == 
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency
        return False

    def __it__(self, other): ## сравнение <
        return self.amount < other.amount

    def __gt__(self, other): ## cравнение >
        return self.amount > other.amount


    ## Арифметические операции

    def __add__(self, other):
        return Money(self.amount + other.amount, self.currency)
    
    def __sub__(self, other):
        return Money(self.amount - other.amount, self.currency)

    def __mu1__(self, other):
        return 

    
    

        