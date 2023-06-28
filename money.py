from abc import ABC, abstractmethod

class Expression(ABC):
    pass

class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency

    def __eq__(self, object):
        return (self.__amount == object.amount and self.currency == object.currency)
    
    def times(self, multiplier):
        return Money(self.amount * multiplier, self.__currency)
    
    def __add__(self, addend):
        return Money(self.__amount + addend.__amount, self.__currency)
            
    @property
    def amount(self):
        return self.__amount
    
    @property
    def currency(self):
        return self.__currency

    @classmethod
    def dollar(cls, amount):
        return Money(amount, "USD")
    
    @classmethod
    def franc(cls, amount):
        return Money(amount, "CHF")
# --------------------
class Bank:
    pass
