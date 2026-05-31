import pytest
from mathlib_evanjjh.trigonometry import Trigonometry

class TestTrigonometry:
    def test_sin(self):
        assert Trigonometry(30).sin() == pytest.approx(0.5)

    def test_cos(self):
        assert Trigonometry(60).cos() == pytest.approx(0.5)

    def test_tan(self):
        assert Trigonometry(45).tan() == pytest.approx(1.0)

    def test_tan_undefined(self):
        with pytest.raises(ValueError):
            Trigonometry(90).tan()