#from abc import ABC, abstractmethod

class Money:
    @property
    def amount(self):
        return self.__amount
    
    def __init__(self, amount, currency):
        self.__amount = amount
        self.g_currency = currency

    def __eq__(self, object):
        return (self.__amount == object.amount and self.g_currency == object.g_currency)
    
    def times(self, multiplier):
        # return Money(self.amount * multiplier, self.g_currency)
        pass
    
    # @property
    def currency(self):
        return self.g_currency

    @classmethod
    def dollar(cls, amount):
        return Dollar(amount, "USD")
    
    @classmethod
    def franc(cls, amount):
        return Franc(amount, "CHF")

   
class Dollar(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
    def times(self, multiplier):
        return Dollar(self.amount * multiplier, self.g_currency)
    
class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
    def times(self, multiplier):
        return Franc(self.amount * multiplier, self.g_currency)
    