import math

class Trigonometry:
    def __init__(self, angle_deg):
        self.angle_deg = angle_deg
        self._rad = math.radians(angle_deg)

    def sin(self):
        return round(math.sin(self._rad), 10)

    def cos(self):
        return round(math.cos(self._rad), 10)

    def tan(self):
        if self.angle_deg % 180 == 90:
            raise ValueError("tan(90°) is undefined.")
        return round(math.tan(self._rad), 10)