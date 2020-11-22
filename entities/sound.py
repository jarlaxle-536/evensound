from .loader import *

class Sound(Entity):
    track = None
    beat = None
    start_index = 1
    duration = DEFAULT_QUANTIZATION_PARAMETER
    pitches = list()
    fields = [
        'track',
        'beat',
        'start_index',
        'duration',
        'pitches'
    ]
    def get_id(dct):
        return random.getrandbits(128)
    @property
    def note(self):
        return self.pitch if self.pitch is not None else 'R'
    @property
    def end_index(self):
        return self.start_index + self.duration
    def __str__(self):
        return f'<SOUND i={self.start_index} t={self.track} p={self.pitches} d={self.duration}>'
    def __lt__(self, other):
        if isinstance(other, Sound):
            return self.index <= other.index
