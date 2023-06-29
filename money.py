from abc import ABC, abstractmethod
class Expression(ABC):
    @abstractmethod
    def reduce(self, bank, to: str):
        pass

class Money(Expression):
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency

    def __eq__(self, object):
        # return (self.amount == object.amount and self.currency == object.currency)
        return self.__dict__ == object.__dict__
    
    def times(self, multiplier):
        return Money(self.amount * multiplier, self.__currency)
    
    def __add__(self, addend):
        return Sum(self, addend)
    
    def reduce(self, bank, to: str):
        rate = bank.rate(self.currency, to)
        return Money(self.amount / rate, to)
            
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
    def __init__(self):
        self.rates = {}

    def reduce(self, source: Exception, to: str):
        return source.reduce(self, to)
    
    def addRate(self, fromcurrency: str, to: str, rate: int):
        curr_rate = Pair(fromcurrency, to)
        self.rates[curr_rate] = rate

    def rate(self, fromcurrency: str, to: str):
        curr_rate = Pair(fromcurrency, to)
        if fromcurrency == to:
            return 1
        return self.rates.get(curr_rate)
        #return (2 if fromcurrency == "CHF" and to == "USD" else 1)
    
# --------------------

class Sum(Expression):
    def __init__(self, augend, addend):
        self.__augend = augend
        self.__addend = addend

    def reduce(self, bank, to):
        amount = self.__augend.reduce(bank, to).amount + self.__addend.reduce(bank, to).amount
        return Money(amount, to)

    @property
    def augend(self):
        return self.__augend
    @property
    def addend(self):
        return self.__addend
    
# ---------------------

class Pair:
    def __init__(self, fromcurrency: str, to: str):
        self.fromcurrency = fromcurrency
        self.to = to

    def __eq__(self, something):
        pair = something
        return self.fromcurrency == pair.fromcurrency and self.to == pair.to
    
    def __hash__(self):
        return hash(0)
    
    # def hashCode(self):
    #     return 0
