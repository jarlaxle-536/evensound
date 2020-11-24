from .loader import *

class TimeSignature(Root):

    numerator = 4
    denominator = 4
    fields = ['numerator', 'denominator']

    @property
    def ratio(self):
        return self.numerator / self.denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
