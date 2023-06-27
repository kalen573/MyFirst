from abc import ABC, abstractmethod

class Money:
    @property
    def amount(self):
        return self.__amount
    
    #@property
    def currency(self):
        return self.g_currency
    
    def __init__(self, amount, currency):
        self.__amount = amount
        self.g_currency = currency

    def __eq__(self, object):
        money = object
        return (self.__amount == money.amount and self.__class__.__name__ == object.__class__.__name__)
    
    @abstractmethod
    def times(self, multiplier):
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
        self.__amount = amount

    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier, "USD")
    
class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
        self.__amount = amount

    def times(self, multiplier: int):
        return Franc(self.amount * multiplier, "CHF")
    