class Money:
    @property
    def amount(self):
        return self.__amount
    
    def __init__(self, amount):
        self.__amount = amount

    # def __eq__(self, object):
    #     money = object
    #     return self.__amount == money.amount
   