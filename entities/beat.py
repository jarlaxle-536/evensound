from .loader import *

from .sound import *

class Beat(Entity):
    fields = [
        'composition',
        'starting_index',
        'tempo'
    ]
    tempo = 120
    starting_index = None
    def setup(self):
        self.time_signature = TimeSignature()
    @staticmethod
    def get_id(dct):
        return random.getrandbits(128)
    def __str__(self):
        return f'<BEAT t={self.tempo}, {self.time_signature}>'

class TimeSignature(Root):
    fields = [
        'ts_numerator',
        'ts_denominator'
    ]
    ts_numerator = 4
    ts_denominator = 4
    def __str__(self):
        return f'{self.ts_numerator}/{self.ts_denominator}'
