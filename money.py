#from abc import ABC, abstractmethod

class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency

    def __eq__(self, object):
        return (self.__amount == object.amount and self.currency == object.currency)
    
    def times(self, multiplier):
        return Money(self.amount * multiplier, self.__currency)
            
    @property
    def amount(self):
        return self.__amount
    
    @property
    def currency(self):
        return self.__currency

    @classmethod
    def dollar(cls, amount):
        return Dollar(amount, "USD")
    
    @classmethod
    def franc(cls, amount):
        return Franc(amount, "CHF")

   
class Dollar(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
    
class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
