from money import Money

class Dollar(Money):

    @property
    def amount(self):
        return self.__amount

    def __init__(self, amount):
        self.__amount = amount

    def times(self, multiplier: int):
        #return self.amount * multiplier
        return Dollar(self.__amount * multiplier)
    
    def __eq__(self, money):
        #dollar = money 
        return self.__amount == money.amount