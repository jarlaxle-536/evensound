from logic.loader import *

class TimeSignature(Entity):
    numerator = 4
    denominator = 4
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
