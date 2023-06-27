from money import Money

class Dollar(Money):

    # @property
    # def amount(self):
    #     return self.__amount

    def __init__(self, amount):
        super(Dollar, self).__init__(amount)
        self.__amount = amount

    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)
    
    # def __eq__(self, object):
    #     money = object
    #     return self.__amount == money.amount