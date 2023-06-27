from money import Money

class Dollar(Money):

    def __init__(self, amount):
        self.__amount = amount

    def times(self, multiplier: int):
        return Dollar(self.__amount * multiplier)