class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier: int):
        #return self.amount * multiplier
        return Dollar(self.amount * multiplier)
    
    def __eq__(self, money):
        #dollar = money 
        return self.amount == money.amount
