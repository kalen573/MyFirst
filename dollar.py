class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)
    
    # 引数moneyを受け取り、その中からDollarオブジェクトを取り出して比較を行う
    def equals(self, money):
        dollar = money # moneyがDollarオブジェクトであることが前提とされている
        return self.amount == dollar.amount
