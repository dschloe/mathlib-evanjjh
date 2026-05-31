import pytest
from mathlib_evanjjh.arithmetic import Arithmetic

class TestArithmetic:
    def test_add(self):
        assert Arithmetic(3, 2).add() == 5

    def test_subtract(self):
        assert Arithmetic(10, 4).subtract() == 6

    def test_multiply(self):
        assert Arithmetic(3, 7).multiply() == 21

    def test_divide(self):
        assert Arithmetic(10, 2).divide() == 5.0

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            Arithmetic(5, 0).divide()