class Franc:
    @property
    def amount(self):
        return self.__amount

    def __init__(self, amount):
        self.__amount = amount

    def times(self, multiplier: int):
        #return self.amount * multiplier
        return Franc(self.__amount * multiplier)
    
    def __eq__(self, money):
        franc = money 
        return self.__amount == franc.amount
#　第5章完了