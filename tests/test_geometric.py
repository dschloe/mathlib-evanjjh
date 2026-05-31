from mathlib_evanjjh.geometric import GeometricSequence

class TestGeometricSequence:
    def test_generate(self):
        assert GeometricSequence(1, 2, 5).generate() == [1, 2, 4, 8, 16]

    def test_nth_term(self):
        assert GeometricSequence(1, 2, 5).nth_term(3) == 4

    def test_sum(self):
        assert GeometricSequence(1, 2, 5).sum() == 31.0

    def test_ratio_one(self):
        assert GeometricSequence(5, 1, 3).generate() == [5, 5, 5]

    def test_empty(self):
        assert GeometricSequence(1, 2, 0).generate() == []