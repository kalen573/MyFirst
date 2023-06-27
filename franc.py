from money import Money

class Franc(Money):
    # @property
    # def amount(self):
    #     return self.__amount

    def __init__(self, amount):
        super(Franc, self).__init__(amount)
        self.__amount = amount

    def times(self, multiplier: int):
        #return self.amount * multiplier
        return Franc(self.amount * multiplier)
    
    # def __eq__(self, object):
    #     money = object
    #     return self.__amount == money.amount