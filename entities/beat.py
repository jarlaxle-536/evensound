from auxiliary import *

from .general import *
from .persistent import *

class BeatLayer:
    pass

class Beat(Entity):
    fields = [
        'tempo',
    ]
    tempo = 120
    def setup(self):
        self.time_signature = TimeSignature()
    @staticmethod
    def get_id(dct):
        return dct.get('name')

class TimeSignature(Root):
    fields = [
        'ts_numerator',
        'ts_denominator'
    ]
    ts_numerator = 4
    ts_denominator = 4
