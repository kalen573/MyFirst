
from money import Money
from money import Bank
from money import Sum

class TestMoney:
    def test_DollarMultiplication(self):
        five = Money.dollar(5)
        assert Money.dollar(10) == five.times(2)
        assert Money.dollar(15) == five.times(3)

    def test_equality(self):
        assert Money.dollar(5) == Money.dollar(5)
        assert not Money.dollar(5) == Money.dollar(6)
        assert not Money.franc(5) == Money.dollar(5)

    def test_Currency(self):
        assert "USD" == Money.dollar(1).currency
        assert "CHF" == Money.franc(1).currency

    def test_SimpleAddition(self):
        five = Money.dollar(5)
        sum = five + five
        bank = Bank()
        reduce = bank.reduce(sum, "USD")
        assert Money.dollar(10) == reduce

    def test_PlusReturnSum(self):
        five = Money.dollar(5)
        result = five + five
        sum = result
        assert five == sum.augend
        assert five == sum.addend

    def test_ReduceSum(self):
        sum = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum, "USD")
        assert Money.dollar(7) == result

    def test_ReduceMoney(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        assert Money.dollar(1) == result

    def rest_ReducemoneyDifferentCurrency(self):
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        assert Money.dollar(1) == result