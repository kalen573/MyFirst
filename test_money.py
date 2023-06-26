from dollar import Dollar

class TestMoney:
    def test_multiplication(self):
        five = Dollar(5)
        assert Dollar(10) == five.times(2)
        assert Dollar(15) == five.times(3)

    def test_equals(self):
        assert Dollar(5) == Dollar(5)
        assert not Dollar(5) == Dollar(6)