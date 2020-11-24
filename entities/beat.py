from .loader import *

from .time_signature import *

class Beat(Entity, CompositionConnected):

    tempo = 120
    starting_index = None
    ts_numerator = TimeSignature.numerator
    ts_denominator = TimeSignature.denominator

    fields = [
        'starting_index',
        'tempo',
        'ts_numerator',
        'ts_denominator'
    ]

    quantization_parameter = MAX_QUANTIZATION_PARAMETER
    sounds = list()

    def setup(self):
        self.time_signature = TimeSignature(
            numerator=self.ts_numerator,
            denominator=self.ts_denominator
        )

    def insert_sound(self, position=None, *args, **kwargs):
        kwargs['beat'] = self
        sound_obj = Sound(**kwargs)
        self.sounds = self.sounds[:]
        heapq.heappush(self.sounds, sound_obj)

    @property
    def quantum_number(self):
        return int((self.time_signature.ratio) * self.quantization_parameter)

    @property
    def total_duration(self):
        return 120 / self.tempo * self.time_signature.ratio

    @property
    def quantum_duration(self):
        return self.total_duration / self.quantum_number

    def __str__(self):
        return f'<BEAT t={self.tempo} s={self.time_signature}>'
