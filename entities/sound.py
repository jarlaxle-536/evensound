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
    pitch = 42
    def get_id(dct):
        return 0
    @property
    def note(self):
        return self.pitch if self.pitch is not None else 'R'
    def __str__(self):
        return f'<SOUND {self.note}>'
