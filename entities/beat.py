from auxiliary import *

class Beat(Root):
    fields = [
        'tempo',
    ]
    tempo = 120
    def setup(self):
        self.time_signature = TimeSignature()

class TimeSignature(Root):
    fields = [
        'ts_numerator',
        'ts_denominator'
    ]
    ts_numerator = 4
    ts_denominator = 4
