from dollar import Dollar
from franc import Franc
from money import Money

class TestMoney:
    def test_DollarMultiplication(self):
        five = Money.dollar(5)
        assert Money.dollar(10) == five.times(2)
        assert Money.dollar(15) == five.times(3)

    def test_equality(self):
        assert Money.dollar(5) == Money.dollar(5)
        assert not Money.dollar(5) == Money.dollar(6)
        assert Money.franc(5) == Money.franc(5)
        assert not Money.franc(5) == Money.franc(6)
        assert not Money.franc(5) == Money.dollar(5)

    def test_FrancMultiplication(self):
        five = Money.franc(5)
        assert Money.franc(10) == five.times(2)
        assert Money.franc(15) == five.times(3)