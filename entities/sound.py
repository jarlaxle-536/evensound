from .loader import *

class Sound(Entity):
    """Localized by track (vertical), beat and index (horizontal)"""
    fields = [
        'beat',
        'track',
        'index',
        'duration',
        'pitch'
    ]
    duration = 16
    pitch = None
    track = None
    def get_id(dct):
        return random.getrandbits(128)
    @property
    def note(self):
        return self.pitch if self.pitch is not None else 'R'
    def __str__(self):
        return f'<SOUND t={self.track} n={self.note} d={self.duration / 64}>'
