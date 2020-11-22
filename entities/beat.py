from .loader import *

from .sound import *

class Beat(Entity, CompositionConnected):
    fields = [
        'starting_index',
        'tempo'
    ]
    tempo = 120
    starting_index = None
    quantization_parameter = MAX_QUANTIZATION_PARAMETER
    def setup(self):
        self.time_signature = TimeSignature()
    def __str__(self):
        return f'<BEAT t={self.tempo}, {self.time_signature}>'
    @property
    def quantum_number(self):
        return int((self.time_signature.ratio) * self.quantization_parameter)

class TimeSignature(Root):
    ts_numerator = 4
    ts_denominator = 4
    fields = [
        'ts_numerator',
        'ts_denominator'
    ]
    def __str__(self):
        return f'{self.ts_numerator}/{self.ts_denominator}'
    @property
    def ratio(self):
        return self.ts_numerator / self.ts_denominator
