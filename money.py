from abc import ABC, abstractmethod

class Money:
    @property
    def amount(self):
        return self.__amount
    
    def __init__(self, amount):
        self.__amount = amount

    def __eq__(self, object):
        money = object
        return (self.__amount == money.amount and self.__class__.__name__ == object.__class__.__name__)
    
    @abstractmethod
    def times(self, multiplier):
        pass
    
    @classmethod
    def dollar(cls, amount):
        return Dollar(amount)
    
    @classmethod
    def franc(cls, amount):
        return Franc(amount)

   
class Dollar(Money):
    def __init__(self, amount):
        super(Dollar, self).__init__(amount)
        self.__amount = amount

    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)
    
class Franc(Money):
    def __init__(self, amount):
        super(Franc, self).__init__(amount)
        self.__amount = amount

    def times(self, multiplier: int):
        #return self.amount * multiplier
        return Franc(self.amount * multiplier)