class GeometricSequence:
    def __init__(self, first, ratio, n):
        self.first = first
        self.ratio = ratio
        self.n = n

    def generate(self):
        """Return a list of n terms of the geometric sequence."""
        return [self.first * (self.ratio ** i) for i in range(self.n)]

    def nth_term(self, k):
        """Return the k-th term (1-indexed)."""
        return self.first * (self.ratio ** (k - 1))

    def sum(self):
        """Return the sum of the geometric sequence."""
        if self.ratio == 1:
            return self.first * self.n
        return self.first * (1 - self.ratio ** self.n) / (1 - self.ratio)