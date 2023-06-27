from money import Money

class Franc(Money):
    def __init__(self, amount):
        self.__amount = amount

    def times(self, multiplier: int):
        #return self.amount * multiplier
        return Franc(self.__amount * multiplier)