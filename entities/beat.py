from .entity import *

class Beat(Entity):
    fields = [
        'tempo',
    ]
    tempo = 120
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time_signature = TimeSignature(**kwargs)

class TimeSignature:
    fields = [
        'ts_numerator',
        'ts_denominator'
    ]
    ts_numerator = 4
    ts_denominator = 4
