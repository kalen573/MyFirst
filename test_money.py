from dollar import Dollar
from franc import Franc
from money import Money

class TestMoney:
    def test_DollarMultiplication(self):
        five = Dollar(5)
        assert Dollar(10) == five.times(2)
        assert Dollar(15) == five.times(3)

    def test_equality(self):
        assert Dollar(5) == Dollar(5)
        assert not Dollar(5) == Dollar(6)
        assert Franc(5) == Franc(5)
        assert not Franc(5) == Franc(6)
        # assert not Franc(5) == Dollar(5)

    def test_FrancMultiplication(self):
        five = Franc(5)
        assert Franc(10) == five.times(2)
        assert Franc(15) == five.times(3)