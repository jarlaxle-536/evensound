from .loader import *

class Sound(Entity):
    """Localized by track (vertical), beat and index (horizontal)"""
    """Beat should be calculated from index as a property"""
    fields = [
        'beat',
        'track',
        'index',
        'duration',
        'pitch'
    ]
    duration = DEFAULT_QUANTIZATION_LEVEL
    pitch = None
    track = None
    index = 1
    def get_id(dct):
        return random.getrandbits(128)
    @property
    def note(self):
        return self.pitch if self.pitch is not None else 'R'
    def __str__(self):
        return f'<SOUND i={self.index} t={self.track} n={self.note} d={self.duration}>'
    def __lt__(self, other):
        if isinstance(other, Sound):
            return self.index <= other.index
